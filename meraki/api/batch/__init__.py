from meraki.api.batch.organizations import ActionBatchOrganizations
from meraki.api.batch.networks import ActionBatchNetworks
from meraki.api.batch.devices import ActionBatchDevices
from meraki.api.batch.appliance import ActionBatchAppliance
from meraki.api.batch.camera import ActionBatchCamera
from meraki.api.batch.cellularGateway import ActionBatchCellularGateway
from meraki.api.batch.insight import ActionBatchInsight
from meraki.api.batch.sensor import ActionBatchSensor
from meraki.api.batch.sm import ActionBatchSm
from meraki.api.batch.switch import ActionBatchSwitch
from meraki.api.batch.wireless import ActionBatchWireless


# Batch class
class Batch:
    def __init__(self, enable_kwarg_validation):
        # Action Batch helper API endpoints by section
        self.organizations = ActionBatchOrganizations(enable_kwarg_validation)
        self.networks = ActionBatchNetworks(enable_kwarg_validation)
        self.devices = ActionBatchDevices(enable_kwarg_validation)
        self.appliance = ActionBatchAppliance(enable_kwarg_validation)
        self.camera = ActionBatchCamera(enable_kwarg_validation)
        self.cellularGateway = ActionBatchCellularGateway(enable_kwarg_validation)
        self.insight = ActionBatchInsight(enable_kwarg_validation)
        self.sensor = ActionBatchSensor(enable_kwarg_validation)
        self.sm = ActionBatchSm(enable_kwarg_validation)
        self.switch = ActionBatchSwitch(enable_kwarg_validation)
        self.wireless = ActionBatchWireless(enable_kwarg_validation)
