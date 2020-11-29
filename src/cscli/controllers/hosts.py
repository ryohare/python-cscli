class NoResultsException(Exception):
    pass


class HostsController:
    def __init__(self, falcon_hosts_api):
        self.api = falcon_hosts_api


    def _check_status_code_and_throw(self, results):
        """helper function which checks if the status code
        return from Falcon. On 400, it means there is no
        data and will return an empty array. On 200, will return
        the results array. On !200 and !400, will raise
        an exception"""

        if results['status_code'] == 400:
            return []
        if results['status_code'] != 200:
            raise Exception("Failed due to : non-2XX response code ({})".format(
                results['status_code'])
            )
        return results['body']['resources']

    def _get_hosts(self, instance_list):
        """Helper func which will return a list of host details defined
        in the supplied instance list."""
        params = []
        for i in instance_list:
            params.append(('ids', i))

        results = self.api.GetDeviceDetails(
            parameters=params
        )

        instance_details = self._check_status_code_and_throw(results)

        return instance_details

    def _get_hosts_helper(self, query):
        """Helper func which will get a list of intance id's associated with
        the supplied query. Thes instance id's will need to be looked up with
        _get_hosts to get the instance details and be useful"""
        body = ""
        results = self.api.QueryDevicesByFilter(parameters=query, body=body)
        instances = self._check_status_code_and_throw(results)
        return self._get_hosts(instances)

    def get_all_hosts(self):
        query = {'filter': ""}
        return self._get_hosts_helper(query)

    def get_mac_hosts(self):
        query = {'filter': "platform_name: \"Mac\""}
        return self._get_hosts_helper(query)

    def get_win_hosts(self):
        query = {'filter': "platform_name: \"Windows\""}
        return self._get_hosts_helper(query)

    def get_linux_hosts(self):
        query = {'filter': "platform_name: \"Linux\""}
        return self._get_hosts_helper(query)
