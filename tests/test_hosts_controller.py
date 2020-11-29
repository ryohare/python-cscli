import mock
import os
import pytest

from cscli.controllers.hosts import HostsController
from falconpy.services.hosts import Hosts as FalconHosts

@pytest.fixture
def falcon_api():
    return FalconHosts("dummpy-access-token")    
        
@pytest.fixture
def hosts_controller(falcon_api):
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
    
