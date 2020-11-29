import mock
import os
import pytest
import falconpy.services.hosts

from cscli.controllers.hosts import HostsController
from falconpy.services.hosts import Hosts as FalconHosts

@pytest.fixture
def falcon_api():
    return FalconHosts("dummpy-access-token")    

@pytest.fixture
def hosts_controller(falcon_api):
    with mock.patch(
        'falconpy.services.hosts.Hosts.GetDeviceDetails',
        return_value={
            'status_code':200, 
            'body':{
                'resources':[
                    'r1',
                    'r2'
                ]
            }
        }
    ):
        with mock.patch(
            'falconpy.services.hosts.Hosts.QueryDevicesByFilter',
            return_value={
                'status_code':200, 
                'body':{
                    'resources':[
                        'r1',
                        'r2'
                    ]
                }
            }
        ):
            return HostsController(falcon_api)

def test_constructor(falcon_api):
    hosts = HostsController(falcon_api)
    assert hosts is not None

def test__check_status_code_and_throw(hosts_controller):
    #
    # 3 return cases:
    #   [] on 400
    #   ['results'] on 200
    #   throw on !200 and !400
    #
    try:
        hosts_controller._check_status_code_and_throw(
            {'status_code':123}
        )
        raise Exception("No exception raised on non 200/400 code")
    except Exception:
        pass
    
    res = hosts_controller._check_status_code_and_throw(
        {'status_code':400}
    )
    assert len(res) == 0

    res = hosts_controller._check_status_code_and_throw(
        {
            'status_code':200, 
            'body':{
                'resources':[
                    'r1',
                    'r2'
                ]
            }
        }
    )
    assert len(res) > 0

@mock.patch('falconpy.services.hosts.Hosts.GetDeviceDetails')
@mock.patch('falconpy.services.hosts.Hosts.QueryDevicesByFilter')
@pytest.mark.parametrize(
    "platform",[
        "hosts_controller.get_all_hosts()",
        "hosts_controller.get_mac_hosts()",
        "hosts_controller.get_win_hosts()",
        "hosts_controller.get_linux_hosts()"
    ]
)
def test_get_host(qd, gd, platform, hosts_controller):
    qd.return_value = {
        'status_code':200, 
        'body':{
            'resources':[
                'r1',
                'r2'
            ]
        }
    }
    gd.return_value = {
        'status_code':200, 
        'body':{
            'resources':[
                'r1',
                'r2'
            ]
        }
    }
    eval(platform)
