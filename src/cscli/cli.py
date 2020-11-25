"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mcscli` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``cscli.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``cscli.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import sys
import argparse
import getpass

# Falcon Imports
from .falconpy.services import oauth2 as FalconAuth
from .falconpy.services.hosts import Hosts as FalconHosts

# Local Imports
from .settings import settings_manager as SM
from .controllers.hosts import HostsController
from .views.hosts import HostsView


def login(config) -> None:
    """ Function will take in a config object and return an access token
    which can be used to access to the Falcon API """
    authz = FalconAuth.OAuth2(
        creds={
            'client_id': config['client_id'],
            'client_secret': config['client_secret']
        }
    )

    return authz.token()['body']['access_token']


def create_cred_file(profile) -> None:
    """ This is the handler for creating a credential file for use with
    this tool """
    print("Enter your Falcon OAuth2 Client ID")
    client_id = getpass.getpass()
    print("Enter your Falcon OAuth2 Client Secret")
    client_secret = getpass.getpass()

    if profile is None:
        profile = input("Enter profile name:\n")
    make_default = False

    make_default_ip = input("Make this profile the default? [Y/n]\n")
    if make_default_ip.lower() == 'y' or make_default_ip == "":
        make_default = True
    config = {
        "client_id": client_id,
        "client_secret": client_secret
    }

    sm = SM.Config("falcon")

    if make_default:
        sm.add_config(config, profile, profile)
    else:
        sm.add_config(config, profile)

    sm.save_config()


def main(argv=sys.argv):
    """
    Args:
        argv (list): List of arguments

    Returns:
        int: A return code

    Does stuff.
    """
    print(argv[1:])
    # global command parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', action='store_true')
    parser.add_argument('-p', '--profile', action='store', nargs=1)
    # subcommand parsers
    commands_subparsers = parser.add_subparsers(dest="commands")

    host_parser = commands_subparsers.add_parser("hosts")
    host_parser.add_argument("--mac", action='store_true')
    host_parser.add_argument("--win", action='store_true')
    host_parser.add_argument("--linux", action='store_true')
    host_parser.add_argument("-n", "--name", action='append')
    host_parser.add_argument("-v", "--view", action='store')

    args = parser.parse_args(argv[1:])
    profile = None
    if args.profile is not None:
        profile = args.profile[0]

    if args.config is True:
        try:
            create_cred_file(profile)
        except Exception as e:
            print("Could not create config file because {}".format(e))
            sys.exit(1)
        sys.exit(0)

    # attempt to load the config
    config = SM.Config('falcon')
    try:
        (loaded_profile, conf) = config.load_profile(profile)
        if profile is not None and loaded_profile != profile:
            print(
                "WARNING: Specified profile could not be loaded and "
                "default {} was loaded instead".format(loaded_profile)
            )
    except Exception as e:
        print("Could not load config file because {}".format(e))
        print("Run with --config flag to setup configuration")
        sys.exit(2)
    try:
        access_token = login(conf)
    except Exception as e:
        print("Could not log into Falcon because {}".format(e))
        sys.exit(2)
    
    if args.commands == 'hosts':
        hosts = HostsController(FalconHosts(access_token))
        hosts_list = []
        if args.mac is not None:
            hosts_list.append(
                hosts.get_mac_hosts()
            )

        #print(hosts_list) 
        hv = HostsView(hosts_list)
        hv.render_names_list()
           
    args.commands
    #print(access_token)
    print(args)
    return 0