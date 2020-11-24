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
import falconpy.services.oauth2 as FalconAuth
import settings.settings_manager as SM


def login(config) -> None:
    """ Function will take in a config object and return an access token
    which can be used to access to the Falcon API """
    authz = FalconAuth.OAuth2(
        creds={
            'client_id': config['client_id']
            'client_secret': config['client_secret']
        }
    )

  return authz.token()['body']['access_token']

def create_cred_file() -> None:
  """ This is the handler for creating a credential file for use with
  this tool """
  print("Enter your Falcon OAuth2 Client ID")
  client_id = getpass.getpass()
  print ("Enter your Falcon OAuth2 Client Secret")
  client_secret = getpass.getpass()
 dfds
  config = {
    "falcon":{
      "client_id":client_id,
      "client_secret":client_secret
    }
  }

  sm = SM.Config("falcon")
  sm.write_config(config)


def main(argv=sys.argv):
    """
    Args:
        argv (list): List of arguments

    Returns:
        int: A return code

    Does stuff.
    """
    create_cred_file()
    print(argv)
    return 0
