# Rely on meraki SDK, os, sys, copy
import meraki
import os
import sys
import copy

# We're also going to import Python's built-in JSON module.
import json

# Setting API key this way, and storing it in the env variables, lets us keep the sensitive API key out of the script itself
# The meraki.DashboardAPI() method does not require explicitly passing this value; it will check the environment for a variable
# called 'MERAKI_DASHBOARD_API_KEY' on its own. In this case, API_KEY is shown simply as an reference to where that information is
# stored.
API_KEY = os.getenv('MERAKI_DASHBOARD_API_KEY')

# Initialize the Dashboard connection.
dashboard = meraki.DashboardAPI(suppress_logging=True)

def printj(ugly_json_object):
	# The json.dumps() method converts a JSON object into human-friendly formatted text
	pretty_json_string = json.dumps(ugly_json_object, indent = 2, sort_keys = False)
	print(pretty_json_string)


# Let's make it easier to call this data later
# getOrganizations will return all orgs to which the supplied API key has access
organizations = dashboard.organizations.getOrganizations()
print('Organizations:')
printj(organizations)

# Class constructor
def constructor(self, arg):
	self.constructor_arg = arg


# Append init
organizations[0]['__init__'] = constructor

# Create an Organization class with dynamic attributes
MyOrganization = type('Organization', (object, ), organizations[0])

# Print a blank line for legibility before showing the firstOrganizationId
print('')
print(f'Your organization is {MyOrganization.id}, and its name is {MyOrganization.name}.')

# READ the settings and mappings
with open('settings.json', 'r') as settings_json:
	settings = json.load(settings_json)

with open('mappings.json', 'r') as mappings_json:
	mappings = json.load(mappings_json)

# Define some string constants
CONFIRM = 'Would you like to proceed?'
CHOICES = '(y/n)'
SETTINGS_REVIEW = 'Please review these settings before proceeding.'
VLAN_ERROR = 'The appliance has a VLAN for which settings.json does not have interface information. Add the interface information to continue.'

# SHOW the user the ingested settings
print(SETTINGS_REVIEW)
for key, value in settings.items():
	print(f'The setting {key} has the following value(s):')
	printj(value)

# CREATE a list of all the tagged VLAN IDs in settings.json
tagged_vlan_ids = [vlan['id'] for vlan in settings['vlans']['others']]


if(input(f'{CONFIRM} {CHOICES}') != 'y'):
	sys.exit()

# GET appliance VLANs
appliance_vlans = dashboard.appliance.getNetworkApplianceVlans(
	networkId=settings['networkId']
	)

switch_interfaces = copy.deepcopy(appliance_vlans)

# CREATE a reference to switch_interfaces that only contains VLANs with DHCP enabled.
# Anything we modify here will also be reflected in the switch_interfaces array.
switch_interfaces_with_dhcp = [vlan for vlan in switch_interfaces if vlan['dhcpHandling'] != 'Do not respond to DHCP requests']

# CREATE a version of switch_interfaces that only contains VLANs with DHCP disabled.
# As above, anything we modify here will also be reflected in the switch_interfaces array.
switch_interfaces_without_dhcp = [vlan for vlan in switch_interfaces if vlan['dhcpHandling'] == 'Do not respond to DHCP requests']

# DEFINE a method that will remove any deprecated params
def remove_deprecated_params(param_types: list, new_config: list):
	modified_vlans = set()
	removed_params = set()
	# Operate on each vlan in the new config
	for vlan in new_config:
		# Search for each relevant param from the provided param types list
		for param_type in param_types:
			# Search for each relevant param from the given params list
			for param in mappings[param_type]['deprecatedParams']:
				# Check that the param is actually in use
				if param in vlan.keys():
					# Remove the old param
					removed_params.add(param)
					modified_vlans.add(vlan['name'])
					vlan.pop(param)
	
	print(f"Removed {removed_params} from {modified_vlans}.")


# DEFINE a method that will update param names and add it to the new config.
def rename_params(param_types: list, new_config: list):
	modified_vlans = set()
	removed_params = set()
	new_params = set()
	# Operate on each vlan in the new config
	for vlan in new_config:
		# Search for each relevant param from the provided param types list
		for param_type in param_types:
			# Search for each relevant param from the provided param types list 
			for param in mappings[param_type]['renamedParams']:
				try:
					# Add the new param
					vlan[param['names']['new']] = vlan[param['names']['old']]
					# Remove the old param
					modified_vlans.add(vlan['name'])
					removed_params.add(param['names']['old'])
					new_params.add(param['names']['new'])
					vlan.pop(param['names']['old'])

				except KeyError:
					pass
				
				
	print(f"Replaced {removed_params} with {new_params} for {modified_vlans}.")


# DEFINE a method that will remap old modes to the new modes
def remap_modes(swappable_params, vlan):
	for param in swappable_params:
		swappable_modes = [mode for mode in param['swappableModes'] if vlan[param['names']['new']] == mode['old']]
		
		# Check each swappable mode
		for mode in swappable_modes:
			# If the mode is swappable, assign the new mode to the new param
			vlan[param['names']['new']] = mode['new']


# DEFINE a method that will remap or split old modes into new modes
def remap_or_split_modes(swap_or_split_params, vlan):
	for param in swap_or_split_params:

		# If the mode is in the fallbacks, use that
		for fallback_mode in settings['fallbackModes']:
			if vlan[param['names']['new']] == fallback_mode['old']:
				vlan.update(fallback_mode['params']['replacement'])

			# If the mode name contains the delimiter, then split it 
			if param['transformType'] == 'swapOrSplit' and \
				param['delimiter'] in vlan[param['names']['new']] and \
					param['names']['new'] == fallback_mode['params']['names']['new']:
				# Split the mode into a list
				split_mode = vlan[param['names']['new']].split(param['delimiter'])
				split_param = fallback_mode['params']['names']['split']
				new_mode = fallback_mode['new']
				# Assign the new mode
				vlan[split_param] = split_mode
				vlan[param['names']['new']] = new_mode


# DEFINE a method that will change the old modes into the new modes and assign them to the new param names
def rename_params_and_modes(param_types: list, new_config: list):
	modified_vlans = set()
	removed_params = set()
	new_params = set()
	
	# Operate on each vlan in the new config
	for vlan in new_config:
		# Search for each relevant param from the provided param types list
		for param_type in param_types:
			relevant_mappings = mappings[param_type]['swappableParamsAndModes']
			# Search for each relevant param from the provided param types list 
			for param in relevant_mappings:
				# Add the new param
				vlan[param['names']['new']] = vlan[param['names']['old']]
				# Remove the old param
				modified_vlans.add(vlan['name'])
				removed_params.add(param['names']['old'])
				new_params.add(param['names']['new'])

				vlan.pop(param['names']['old'])

			swappable_params = [param for param in relevant_mappings if param['transformType'] in ['swap','swapOrSplit']]

			# Remap the modes
			remap_modes(swappable_params, vlan)
			
			swap_or_split_params = [param for param in relevant_mappings if param['transformType'] == 'swapOrSplit']

			# Remap or split the modes
			remap_or_split_modes(swap_or_split_params, vlan)

	print(f"Replaced {removed_params} with {new_params} for {modified_vlans}.")


# DEFINE a method that will find and replace params with dynamic keys
def remap_dynamic_keys(relevant_params, vlan):
	# Find and replace each of these params
	for param in relevant_params:
		# We only need to iterate through values for dynamic keys that have values.
		if vlan[param['parent']['dynamicKeyName']]:
			new_param_list = []
			# For each instance of a dynamic key in this particular vlan config,
			for dynamic_key in vlan[param['parent']['dynamicKeyName']].keys():
				# Add the nested param to the new_param list.
				new_param = dict()
				new_param[param['parent']['newKeyName']] = dynamic_key

				drop_key = False
				# Now add all the subkeys
				for nested_param in param['nestedParams']:
					new_param[nested_param['name']] = vlan[param['parent']['dynamicKeyName']][dynamic_key][nested_param['name']]
					
					# Remap None values to '' if enabled
					if new_param[nested_param['name']] is None and param['remapNone']:
						new_param[nested_param['name']] = ''

					if new_param[nested_param['name']] == settings['vlans']['native']['interfaceIp']:
						# Drop the key
						drop_key = True

				if not drop_key:
					new_param_list.append(new_param)
			vlan[param['parent']['dynamicKeyName']] = new_param_list
		
		# The dynamic key is empty, so replace it with a list.
		else:
			vlan[param['parent']['dynamicKeyName']] = list()

# DEFINE a method that will transform dynamically keyed params into flat lists
def flatten_params(param_types: list, new_config: list):
	# Operate on each vlan in the new config
	for vlan in new_config:
		# Search for each relevant param from the provided params list
		for param_type in param_types:
			relevant_mappings = mappings[param_type]['specialParamsAndModes']
			# The only relevant params for this VLAN are the ones where the dynamic key name is mentioned in the VLAN config.
			relevant_params = [param for param in relevant_mappings \
				if param['parent']['dynamicKeyName'] in vlan.keys() \
					and param['transformType'] == 'flattenDynamicKey']

			# Remap the keys
			remap_dynamic_keys(relevant_params, vlan)


# DHCP INTERFACES
# REMOVE deprecated DHCP and non-DHCP params from DHCP interfaces
remove_deprecated_params(
	['interface', 'interfaceDhcp'],
	switch_interfaces
)

# RENAME DHCP and non-DHCP params on DHCP interfaces
rename_params(
	['interface', 'interfaceDhcp'], 
	switch_interfaces
	)

# RENAME DHCP and non-DHCP params and modes on DHCP interfaces
rename_params_and_modes(
	['interface', 'interfaceDhcp'], 
	switch_interfaces
	)

# FLATTEN params that contain dynamic keys into a list of dicts on DHCP interfaces
flatten_params(
	['interfaceDhcp'],
	switch_interfaces
)

# Now that we've converted the configs from MX VLANs to MS interfaces, it's time we start
# calling the VLANs "interfaces".

for interface in switch_interfaces:
	# ASSIGN the static information that isn't derived from the appliance config
	# Set the native VLAN info
	if interface['vlanId'] == settings['vlans']['native']['id']:
		interface['defaultGateway'] = settings['vlans']['native']['defaultGateway']
		interface['interfaceIp'] = settings['vlans']['native']['interfaceIp']
	# Set the tagged VLAN info
	elif interface['vlanId'] in tagged_vlan_ids:
		interface_ip = [other_vlan['interfaceIp'] for other_vlan \
		in settings['vlans']['others'] if other_vlan['id'] == interface['vlanId']].pop()
		
		interface['interfaceIp'] = interface_ip
	# We need to have this static information for each VLAN in the appliance config. If we don't find it, then we'll quit so you can fix settings.json.
	else:
		print(VLAN_ERROR)
		sys.exit()


# We've now replaced all the params and modes necessary. However, unlike appliances, switches
# offer different endpoints for interface settings and interface DHCP settings. Therefore we
# now need to split the interface settings into payloads for the respective endpoints.
# We'll copy the DHCP switch interfaces array so that changes to this won't modify the 
# original array.

dhcp_configs = dict()
# For 
for interface in switch_interfaces_with_dhcp:
	dhcp_configs[interface['vlanId']] = copy.copy(interface)

interface_configs = []
for interface in switch_interfaces:
	interface_configs.append(copy.copy(interface))

interface_param_names = ['interfaceIp','defaultGateway']
for key in mappings['interface']:
	for param in mappings['interface'][key]:
		if isinstance(param, dict):
			if 'names' in param:
				interface_param_names.append(param['names']['new'])
			elif 'name' in param:
				interface_param_names.append(param['name'])
			elif 'parent' in param:
				interface_param_names.append(param['parent']['dynamicKeyName'])

dhcp_param_names = ['dnsCustomNameservers']
for key in mappings['interfaceDhcp']:
	for param in mappings['interfaceDhcp'][key]:
		if isinstance(param, dict):
			if 'names' in param:
				dhcp_param_names.append(param['names']['new'])
			elif 'name' in param:
				dhcp_param_names.append(param['name'])
			elif 'parent' in param:
				dhcp_param_names.append(param['parent']['dynamicKeyName'])

# Remove the interface configs from the DHCP params
for vlan_id, config in dhcp_configs.items():
	for param in interface_param_names:
		dhcp_configs[vlan_id].pop(param,None)

# Remove the DHCP params from the interface configs
for interface in interface_configs:
	for param in dhcp_param_names:
		interface.pop(param,None)

# DEFINE a function to create the interfaces
def create_interfaces(interface_configs, serial):
	responses = []
	for interface in interface_configs:
		if interface['vlanId'] == settings['vlans']['native']['id']:
			response = dashboard.switch.createDeviceSwitchRoutingInterface(
				serial, interface['name'], interface['interfaceIp'], interface['vlanId'], 
				subnet = interface['subnet'],
				defaultGateway = interface['defaultGateway']
			)
		else:
			response = dashboard.switch.createDeviceSwitchRoutingInterface(
				serial, interface['name'], interface['interfaceIp'], interface['vlanId'], 
				subnet = interface['subnet']
			)
		responses.append(response)
	return responses

# DEFINE a function to update the DHCP config for each interface
def configure_interface_dhcp(dhcp_configs, serial, interfaces):
	responses = []
	for vlan_id in dhcp_configs.keys():
		dhcp_interface = [interface for interface in interfaces if interface['vlanId'] == vlan_id].pop()
		
		interface = dhcp_configs[vlan_id]

		if 'dnsCustomNameservers' in interface:
			response = dashboard.switch.updateDeviceSwitchRoutingInterfaceDhcp(
				serial, dhcp_interface['interfaceId'],
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
				serial, dhcp_interface['interfaceId'],
				dhcpMode = interface['dhcpMode'],
				dhcpLeaseTime = interface['dhcpLeaseTime'],
				dnsNameserversOption = interface['dnsNameserversOption'],
				dhcpOptions = interface['dhcpOptions'],
				reservedIpRanges = interface['reservedIpRanges'],
				fixedIpAssignments = interface['fixedIpAssignments']
			)
		responses.append(response)
	return responses


# Automatically create the relevant interfaces and save the responses
serial = "Q2AY-3EWG-749X"

created_interfaces = create_interfaces(
	interface_configs, serial
)

dhcp_updates = configure_interface_dhcp(
	dhcp_configs, serial, created_interfaces
)

printj(created_interfaces)
printj(dhcp_updates)