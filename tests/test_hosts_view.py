import mock
import os
import pytest
import falconpy.services.hosts

from cscli.views.hosts import HostsView
from falconpy.services.hosts import Hosts as FalconHosts

@pytest.fixture
def hosts_view():
    return HostsView([[
        {
            'hostname': 'ctrlrm01',
            'os_version': 'IRIX',
            'agent_version': '0.5',
            'last_seen': '1/1/1970'
        }
    ]])

def test_init():
    HostsView({})

def test_render_simple(hosts_view):
    hosts_view.render_simple()
