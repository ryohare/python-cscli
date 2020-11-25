
class HostsController:
    def __init__(self, falcon_hosts_api):
        self.api = falcon_hosts_api

    def _check_status_code_and_throw(self, results):
        if results['status_code'] != 200:
            raise Exception("Failed due to : non-2XX response code ({})".format(
                results['status_code'])
            )
        return results['body']['resources']

    def get_hosts(self, instance_list):
        params = []
        for i in instance_list:
            params.append(('ids', i))

        results = self.api.GetDeviceDetails(
            parameters=params
        )

        instance_details = self._check_status_code_and_throw(results)

        return instance_details

    def get_mac_hosts(self):
        query = {'filter': "platform_name: \"Mac\""}
        body = ""

        results = self.api.QueryDevicesByFilter(parameters=query, body=body)
        instances = self._check_status_code_and_throw(results)
        instances_details = self.get_hosts(instances)

        return instances_details
