# This script requires the Meraki SDK, sys, copy, json
import meraki
import sys
import copy
import json

# Treat your API key like a password. Store it in your environment variables as 'MERAKI_DASHBOARD_API_KEY' and let the SDK call it for you.
# Or, call it manually after importing Python's os module:
# API_KEY = os.getenv('MERAKI_DASHBOARD_API_KEY')

# CUSTOMIZABLE STRINGS
SETTINGS_FILENAME = 'settings.json'
MAPPINGS_FILENAME = 'mappings.json'
CONFIRM = 'Would you like to proceed?'
CHOICES = '(y/n)'
STATIC_SETTINGS_REVIEW = 'Please review these static settings before proceeding.'
APPLIANCE_SETTINGS_REVIEW = 'Please review these appliance settings before proceeding.'
VLAN_ERROR = 'The appliance has a VLAN for which settings.json does not have interface information. Add the interface information to continue.'
GOODBYE = 'Now go check your L3 switch\'s routing settings.'

# DEFINE a method that will ingest settings and param mappings
def ingest(settings_filename: str, mappings_filename: str):
	# INGEST SETTINGS, AND PARAM MAPPINGS
	# READ the settings and mappings
	with open(settings_filename, 'r') as settings_json:
		settings = json.load(settings_json)

	with open(mappings_filename, 'r') as mappings_json:
		mappings = json.load(mappings_json)

	# CREATE a list of all the tagged VLAN IDs in settings.json
	tagged_vlan_ids = [vlan['id'] for vlan in settings['vlans']['others']]

	# CREATE a list of all the interface IPs in settings.json
	interface_ips = [vlan['interfaceIp'] for vlan in settings['vlans']['others']]
	interface_ips.append(settings['vlans']['native']['interfaceIp'])

	return(settings, mappings, tagged_vlan_ids, interface_ips)


# DEFINE a function to build working configs that we can manipulate. In this example, it will be useful to separate the interfaces with
# DHCP enabled vice disabled, because interfaces with DHCP enabled have options that need to be PUT to two different endpoints.
def build_working_configs(
	starting_configs: list, 
	feature_old_toggle_param: str = 'dhcpHandling', 
	feature_old_toggle_disabled_mode: str = 'Do not respond to DHCP requests'
	):
	# DEEPCOPY the starting config. We'll manipulate a separate working config. DEEPCOPY is important because direct assignment creates a  
	# reference to the original object, whereas we want to modify this one without modifying the original, in case we want to debug and
	# compare old with new.
	working_configs = copy.deepcopy(starting_configs)

	# CREATE a reference to the working config that only contains items with the feature enabled.
	# Anything we modify here will also be reflected in the working_config array.
	working_configs_with_feature = [config for config in working_configs if config[feature_old_toggle_param] != feature_old_toggle_disabled_mode]

	return(working_configs, working_configs_with_feature)


# DEFINE a pretty print function.
def printj(ugly_json_object: list):
	# The json.dumps() method converts a JSON object into human-friendly formatted text
	pretty_json_string = json.dumps(ugly_json_object, indent = 2, sort_keys = False)
	print(pretty_json_string)


# DEFINE a method that will check each param against the knownParams in mappings.json and choose the appropriate action for that param, 
# and then return a list of tasks per config item.
def build_task_list(*, old_configs: list, mappings: list):
	# Make an empty to-do list.
	to_do = []
	# Search every item (in this case, a VLAN)
	for old_config in old_configs:
		# Search every parameter in the old config for a matching one in the mappings file,
		# and make a list out of it.
		old_config_matched_params = [param for param in mappings['knownParams'] if param['names']['old'] in old_config]

		# Make an empty dict() for each old_config where we'll store the lists of params needing action
		params_to = dict()

		# REMOVE
		# Check each matched param's mapping status and assign to an appropriate array based on the required action.
		params_to['remove'] = [param for param in old_config_matched_params if param['status'] == 'deprecated']
		remaining_params = [param for param in old_config_matched_params if param not in params_to['remove']]

		# REUSE
		params_to['reuse'] = [param for param in old_config_matched_params if param['status'] == 'reused']
		remaining_params = [param for param in remaining_params if param not in params_to['reuse']]

		# RENAME
		params_to['rename'] = [param for param in old_config_matched_params if param['status'] == 'renamed']
		remaining_params = [param for param in remaining_params if param not in params_to['rename']]

		# TRANSFORM
		params_to['transform'] = [param for param in old_config_matched_params if param['status'] == 'transformed']
		remaining_params = [param for param in remaining_params if param not in params_to['transform']]

		if(len(remaining_params) != 0):
			print(f"I found params in the source that aren't mapped in the mappings file. These are: {remaining_params}")
			print("I will now quit so you can map those params.")
			sys.exit()

		# Add this compiled dict to our to-do list.
		to_do.append(params_to)

	return(to_do)


# DEFINE a method that will remove params
def remove_params(task_list: list, old_configs: list):
	# Operate on each task in the list
	modified_params = set()
	modified_configs = set()
	past_tense_verb = 'Removed'
	# Iterate through the tasks and configs at the same time.
	for task, config in zip(task_list, old_configs):
		
		# Iterate through each param in the task
		for param in task:
			modified_params.add(param['names']['old'])
			modified_configs.add(config['name'])
			
			# Remove the param
			config.pop(param['names']['old'])
	
	print(f"{past_tense_verb} {modified_params} from {modified_configs}.\n")
	
	return(old_configs)


# DEFINE a method that will rename params
def rename_params(task_list: list, old_configs: list):
	# Operate on each task in the list
	modified_params = set()
	modified_configs = set()
	past_tense_verb = 'Renamed'
	# Iterate through the tasks and configs at the same time.
	for task, config in zip(task_list, old_configs):
		
		# Iterate through each param in the task
		for param in task:
			modified_params.add(param['names']['old'])
			modified_configs.add(config['name'])

			# Add a param with the new name, and assign it the old value while removing it from the list
			config[param['names']['new']] = config.pop(param['names']['old'])
	
	print(f"{past_tense_verb} {modified_params} from {modified_configs}.\n")
	return(old_configs)

# DEFINE a method that will replace null values in subkeys with blank strings
def transform_replace_none(*, param, config, transform):
	modified_params = set()
	modified_configs = set()
	# Check each parameter for null values
	for subparam in config[param['names']['new']]:
		if None in subparam.values():
			subparam[transform['action']] = ''
	
	return(modified_params, modified_configs)


# DEFINE a method that will rename a param's mode
def transform_rename_mode(*, param, config):
	modified_params = set()
	modified_configs = set()
	# Check each mode for the current param
	for mode in param['modes']:
		# If the current mode corresponds to a new one, replace it with the new one
		if config[param['names']['new']] == mode['old']:
			config[param['names']['new']] = mode['new']
			modified_params.add(param['names']['new'])
			modified_configs.add(config['name'])
	
	return(modified_params, modified_configs)


# DEFINE a method that will split a param's mode
def transform_split_mode(*, param, config, transform):
	modified_params = set()
	modified_configs = set()
	# Split the given param's mode by the delimiter specified in the mappings if the delimter is there
#	if transform['action'] in config[param['names']['new']]:
	config[param['names']['new']] = config[param['names']['new']].split(transform['action'])
	modified_params.add(param['names']['new'])
	modified_configs.add(config['name'])
	
	return(modified_params, modified_configs)


# DEFINE a method that will split a param's mode
def transform_add_param(*, param, config, transform):
	modified_params = set()
	modified_configs = set()
	# Add to the config a param with the new name from the transform, and assign it the old value
	config[transform['action']] = config[param['names']['new']]
	# Assign the original param with the fallback mode
	config[param['names']['new']] = transform['fallback']

	modified_params.add(param['names']['new'])
	modified_params.add(transform['action'])
	modified_configs.add(config['name'])
	
	return(modified_params, modified_configs)


# DEFINE a method that will demote a dynamic key to a key-value pair
def transform_demote_dynamic_key(*, param, config, **kwargs: dict):
	modified_params = set()
	modified_configs = set()
	interface_ips = kwargs['interface_ips']

	# Make a new list that will contain all the new dicts
	new_param_list = []

	# For each instance of a dynamic key in this particular vlan config
	for dynamic_key in config[param['names']['new']]:
		# Make a new dict that lists the key as a value, and its nested key/value pairs as additional top-level key/value pairs
		new_param = dict()
		# Make the dynamic key the value of the new key name per mappings
		new_param[param['names']['newSubParam']] = dynamic_key
		# Now add all the subkeys
		new_param.update(config[param['names']['new']][dynamic_key])
		
		# LET'S TALK INTERFACE ADDRESSES
		# If the IP address in the reservation matches a new interface IP for the switch, then the two settings will 
		# interfere. We'll simply drop the DHCP reservation for that IP address if it's the same as the IP address for
		# the interface.
		if new_param['ip'] not in interface_ips:
			# Add the new param to the new param list
			new_param_list.append(new_param)	

	# Assign the new param list to the original key
	config[param['names']['new']] = new_param_list
	
	modified_params.add(param['names']['new'])
	modified_configs.add(config['name'])
	
	return(modified_params, modified_configs)


# DEFINE a method that coordinates the transforms
def transform_coordinate(*, param, config, transform, **kwargs: dict):
	modified_params = set()
	modified_configs = set()
	interface_ips = kwargs['interface_ips']

	# Perform each transform if called for in mappings
	if transform['type'] == 'rename None':
		# Hand off the transform to a single-purpose method
		transformed_params, transformed_configs = transform_replace_none(param = param, config = config, transform = transform)
		# Merge the modification sets from that method
		modified_params |= (transformed_params)
		modified_configs |= (transformed_configs)

	if transform['type'] == 'rename mode':
		# Hand off the transform to a single-purpose method
		transformed_params, transformed_configs = transform_rename_mode(param = param, config = config)
		# Merge the modification sets from that method
		modified_params |= (transformed_params)
		modified_configs |= (transformed_configs)
	
	if transform['type'] == 'split delimited strings' and transform['action'] in config[param['names']['new']]:
		# Hand off the transform to a single-purpose method
		transformed_params, transformed_configs = transform_split_mode(param = param, config = config, transform = transform)
		# Merge the modification sets from that method
		modified_params |= (transformed_params)
		modified_configs |= (transformed_configs)

	if transform['type'] == 'add param' and isinstance(config[param['names']['new']], list):
		# Hand off the transform to a single-purpose method
		transformed_params, transformed_configs = transform_add_param(param = param, config = config, transform = transform)
		# Merge the modification sets from that method
		modified_params |= (transformed_params)
		modified_configs |= (transformed_configs)

	if transform['type'] == 'demote dynamic key' and isinstance(config[param['names']['new']], dict):
		# Hand off the transform to a single-purpose method
		transformed_params, transformed_configs = transform_demote_dynamic_key(param = param, config = config, transform = transform, interface_ips = interface_ips)
		# Merge the modification sets from that method
		modified_params |= (transformed_params)
		modified_configs |= (transformed_configs)

	return(modified_params, modified_configs)


# DEFINE a method that will transform params.
def transform_params(task_list: list, old_configs: list, **kwargs: dict):
	# Operate on each task in the list
	modified_params = set()
	modified_configs = set()
	past_tense_verb = 'Transformed'
	interface_ips = kwargs['interface_ips']
	# Iterate through the tasks and configs at the same time.
	for task, config in zip(task_list, old_configs):
		
		# Iterate through each param in the task
		for param in task:
			modified_params.add(param['names']['old'])
			modified_configs.add(config['name'])

			# Add a param with the new name, and assign it the old value while removing it from the list
			config[param['names']['new']] = config.pop(param['names']['old'])

			# Iterate through each transformation
			for transform in param['transforms']:
				transformed_params, transformed_configs = transform_coordinate(param = param, config = config, transform = transform, interface_ips = interface_ips)
				# Merge the modification sets from that method
				modified_params |= (transformed_params)
				modified_configs |= (transformed_configs)

	print(f"{past_tense_verb} {modified_params} from {modified_configs}.\n")
	return(old_configs)


# DEFINE a method that adds the static configuration information from settings.json to each interface
def assign_statics(tagged_vlan_ids: list, settings, old_configs: list):
	for interface in old_configs:
		# ASSIGN the static information that isn't derived from the appliance config
		# Set the native VLAN info
		if interface['vlanId'] == settings['vlans']['native']['id']:
			interface['defaultGateway'] = settings['vlans']['native']['defaultGateway']
			interface['interfaceIp'] = settings['vlans']['native']['interfaceIp']
		# Set the tagged VLAN info
		elif interface['vlanId'] in tagged_vlan_ids:
			# Use a list comprehension, then pop it, to get the interface IP
			interface['interfaceIp'] = [tagged_vlan['interfaceIp'] for tagged_vlan \
			in settings['vlans']['others'] if tagged_vlan['id'] == interface['vlanId']].pop()
		# We need to have this static information for each VLAN in the appliance config. If we don't find it, then we'll quit so you can fix settings.json.
		else:
			print(VLAN_ERROR)
			sys.exit()
	return(old_configs)


# DEFINE a function to create the interfaces
def create_interfaces(dashboard, settings, switch_interfaces: list):
	# Start a list to collect responses. They will be handy because they'll have the created inteface IDs.
	responses = []
	# Create each interface. The native VLAN will need special params from settings.json.
	for interface in switch_interfaces:
		if interface['vlanId'] != settings['vlans']['native']['id']:
			response = dashboard.switch.createDeviceSwitchRoutingInterface(
				settings['switchSerial'], interface['name'], interface['interfaceIp'], interface['vlanId'], 
				subnet = interface['subnet']
			)
		else:
			response = dashboard.switch.createDeviceSwitchRoutingInterface(
				settings['switchSerial'], interface['name'], interface['interfaceIp'], interface['vlanId'], 
				subnet = interface['subnet'],
				defaultGateway = interface['defaultGateway']
			)
		responses.append(response)
	return responses


# DEFINE a function to update the DHCP config for each interface
def configure_interface_dhcp(dashboard, serial, switch_interfaces_with_dhcp, created_interfaces):
	responses = []
	# Iterate through all the 
	for interface in switch_interfaces_with_dhcp:
		created_dhcp_interface = [created_interface for created_interface in created_interfaces if created_interface['vlanId'] == interface['vlanId']].pop()
		if 'dnsCustomNameservers' in interface:
			response = dashboard.switch.updateDeviceSwitchRoutingInterfaceDhcp(
				serial, created_dhcp_interface['interfaceId'],
				dhcpMode = interface['dhcpMode'],
				dhcpLeaseTime = interface['dhcpLeaseTime'],
				dnsNameserversOption = interface['dnsNameserversOption'],
				dnsCustomNameservers = interface['dnsCustomNameservers'],
				dhcpOptions = interface['dhcpOptions'],
				reservedIpRanges = interface['reservedIpRanges'],
				fixedIpAssignments = interface['fixedIpAssignments']
			)
		else:
			response = dashboard.switch.updateDeviceSwitchRoutingInterfaceDhcp(
				serial, created_dhcp_interface['interfaceId'],
				dhcpMode = interface['dhcpMode'],
				dhcpLeaseTime = interface['dhcpLeaseTime'],
				dnsNameserversOption = interface['dnsNameserversOption'],
				dhcpOptions = interface['dhcpOptions'],
				reservedIpRanges = interface['reservedIpRanges'],
				fixedIpAssignments = interface['fixedIpAssignments']
			)
		responses.append(response)
	return responses


# DEFINE a main method that will drive the config through all necessary param and mode changes, and push the change to Dashboard.
def main():
	# INGEST settings and mappings--we need some of these to start the connection
	settings, mappings, tagged_vlan_ids, interface_ips = ingest(SETTINGS_FILENAME, MAPPINGS_FILENAME)

	# START A MERAKI DASHBOARD API SESSION
	# Initialize the Dashboard connection.
	dashboard = meraki.DashboardAPI(suppress_logging=True)

	# SHOW the user the ingested settings
	print(STATIC_SETTINGS_REVIEW)
	for key, value in settings.items():
		print(f'The setting {key} has the following value(s):')
		printj(value)
	
	# CONFIRM the operation
	if(input(f'{CONFIRM} {CHOICES}') != 'y'):
		sys.exit()
	
	# GET appliance VLANs from Meraki Dashboard
	appliance_vlans = dashboard.appliance.getNetworkApplianceVlans(
		networkId=settings['networkId']
		)

	# BUILD working configs that we can manipulate.
	switch_interfaces, switch_interfaces_with_dhcp = build_working_configs(appliance_vlans)

	# REMOVE, RENAME, REUSE, or TRANSFORM each param
	task_list = build_task_list(old_configs = switch_interfaces, mappings = mappings)

	# MIGRATE the settings
	task_list_types = dict()
	task_list_types['remove'] = [task['remove'] for task in task_list]
	task_list_types['rename'] = [task['rename'] for task in task_list]
	task_list_types['transform'] = [task['transform'] for task in task_list]

	# REMOVE params
	switch_interfaces = remove_params(
		task_list_types['remove'], 
		switch_interfaces
		)
	
	# RENAME params
	switch_interfaces = rename_params(
		task_list_types['rename'], 
		switch_interfaces
		)
	
	# TRANSFORM params. One of these transformations requires the list of interface IPs.
	switch_interfaces = transform_params(
		task_list_types['transform'], 
		switch_interfaces,
		interface_ips = interface_ips
		)

	# ASSIGN statics (see settings.json)
	switch_interfaces = assign_statics(
		tagged_vlan_ids, 
		settings,
		switch_interfaces
		)

	# We've now replaced all the params and modes necessary. However, unlike appliances, switches
	# offer different endpoints for interface settings and interface DHCP settings. Therefore we
	# will push some settings to the interface endpoint, and the DHCP settings to the DHCP endpoint.

	# Let's review what we've done:
	print('I created these new configs:')
	for interface in switch_interfaces:
		printj(interface)
		

	# CREATE the interfaces
	created_interfaces = create_interfaces(
		dashboard,
		settings,
		switch_interfaces
	)

	# CONFIGURE DHCP on the DHCP interfaces
	configured_dhcp = configure_interface_dhcp(
		dashboard,
		settings['switchSerial'],
		switch_interfaces_with_dhcp,
		created_interfaces
	)

	# CONFIRM
	printj(created_interfaces)
	printj(configured_dhcp)
	print(GOODBYE)


if __name__ == "__main__":
	main()
