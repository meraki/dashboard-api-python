class AsyncSwitchPortSchedules(object):
    def __init__(self, session):
        super(SwitchPortSchedules, self).__init__()
        self._session = session

    async def getNetworkSwitchPortSchedules(self, networkId: str):
        """
        **List switch port schedules**
        https://api.meraki.com/api_docs#list-switch-port-schedules
        
        - networkId (string)
        """

        metadata = {
            "tags": ["Switch port schedules"],
            "operation": "getNetworkSwitchPortSchedules",
        }
        resource = f"/networks/{networkId}/switch/portSchedules"

        return await self._session.get(metadata, resource)

    async def createNetworkSwitchPortSchedule(self, networkId: str, name: str, **kwargs):
        """
        **Add a switch port schedule**
        https://api.meraki.com/api_docs#add-a-switch-port-schedule
        
        - networkId (string)
        - name (string): The name for your port schedule. Required
        - portSchedule (object):     The schedule for switch port scheduling. Schedules are applied to days of the week.
    When it's empty, default schedule with all days of a week are configured.
    Any unspecified day in the schedule is added as a default schedule configuration of the day.

        """

        kwargs.update(locals())

        metadata = {
            "tags": ["Switch port schedules"],
            "operation": "createNetworkSwitchPortSchedule",
        }
        resource = f"/networks/{networkId}/switch/portSchedules"

        body_params = ["name", "portSchedule"]
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def deleteNetworkSwitchPortSchedule(self, networkId: str, portScheduleId: str):
        """
        **Delete a switch port schedule**
        https://api.meraki.com/api_docs#delete-a-switch-port-schedule
        
        - networkId (string)
        - portScheduleId (string)
        """

        metadata = {
            "tags": ["Switch port schedules"],
            "operation": "deleteNetworkSwitchPortSchedule",
        }
        resource = f"/networks/{networkId}/switch/portSchedules/{portScheduleId}"

        return await self._session.delete(metadata, resource)

    async def updateNetworkSwitchPortSchedule(
        self, networkId: str, portScheduleId: str, **kwargs
    ):
        """
        **Update a switch port schedule**
        https://api.meraki.com/api_docs#update-a-switch-port-schedule
        
        - networkId (string)
        - portScheduleId (string)
        - name (string): The name for your port schedule.
        - portSchedule (object):     The schedule for switch port scheduling. Schedules are applied to days of the week.
    When it's empty, default schedule with all days of a week are configured.
    Any unspecified day in the schedule is added as a default schedule configuration of the day.

        """

        kwargs.update(locals())

        metadata = {
            "tags": ["Switch port schedules"],
            "operation": "updateNetworkSwitchPortSchedule",
        }
        resource = f"/networks/{networkId}/switch/portSchedules/{portScheduleId}"

        body_params = ["name", "portSchedule"]
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)
