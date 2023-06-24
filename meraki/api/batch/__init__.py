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
    def __init__(self):
        # Action Batch helper API endpoints by section
        self.organizations = ActionBatchOrganizations()
        self.networks = ActionBatchNetworks()
        self.devices = ActionBatchDevices()
        self.appliance = ActionBatchAppliance()
        self.camera = ActionBatchCamera()
        self.cellularGateway = ActionBatchCellularGateway()
        self.insight = ActionBatchInsight()
        self.sensor = ActionBatchSensor()
        self.sm = ActionBatchSm()
        self.switch = ActionBatchSwitch()
        self.wireless = ActionBatchWireless()
