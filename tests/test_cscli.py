import mock
import os
import pytest

from cscli.cli import main
from pathlib import Path

test_config_file = '{"default_profile": "test_profile", "test_profile": {"client_id": "abedefg", "client_secret": "abedefg"}}'


def test_no_config_file():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main([])
        assert pytest_wrapped_e.exception.code == 2

@mock.patch('getpass.getpass')
@mock.patch('builtins.input')
def test_create_config(ip, getpw):
    #
    # Success on init will cause a system.exit(0) event
    #
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        ip.return_value = 'test_profile'
        getpw.return_value = 'abedefg'
        main([
            'cli.py',
            '--config'
        ])
        assert pytest_wrapped_e.exception.code == 0

    #
    # verify then clean up the config file
    #
    config_file = "{}/.{}".format(Path.home(),"falcon")
    if not os.path.exists(config_file):
        raise Exception("Failed to create config file")
    os.remove(config_file)