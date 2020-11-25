class NoResultsException(Exception):
    pass


class HostsController:
    def __init__(self, falcon_hosts_api):
        self.api = falcon_hosts_api

    def _check_status_code_and_throw(self, results):
        # check if its a 400, which means no results
        # for the query because there are either no
        # results for the query or its a bad query
        if results['status_code'] == 400:
            return []
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

    def _get_hosts_helper(self, query):
        body = ""
        results = self.api.QueryDevicesByFilter(parameters=query, body=body)
        instances = self._check_status_code_and_throw(results)
        return self.get_hosts(instances)

    def get_mac_hosts(self):
        query = {'filter': "platform_name: \"Mac\""}
        return self._get_hosts_helper(query)

    def get_win_hosts(self):
        query = {'filter': "platform_name: \"Windows\""}
        return self._get_hosts_helper(query)

    def get_linux_hosts(self):
        query = {'filter': "platform_name: \"Linux\""}
        return self._get_hosts_helper(query)
