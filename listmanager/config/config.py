"""
Configuration object for the ICSA listmanager application

The list manager email username, password, and the LISTSERV password may
all be specified in a file called '.icsa_listmanager' in the user's home
directory, like so:

    [auth]
    mail_host = mail.hostname.com
    mail_user = username@hostname.com
    mail_pass = YourSecretPassword
    listserv_pass = YourListservPassword

If these variables are present in the environment, their values will
override the config file:

    - ICSA_MAIL_HOST
    - ICSA_MAIL_USER
    - ICSA_MAIL_PASS
    - ICSA_LISTSERV_PASS
"""
import os

__all__ = ['DEFAULT_CONFIG', 'Config', 'MissingConfigSetting']
DEFAULT_CONFIG = os.path.expanduser('~/.icsa_listmanager')

class MissingConfigSetting(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Missing config value '{}'".format(self.value)


class Config(object):
    required_attrs = ['mail_host', 'mail_user', 'mail_pass',
                      'listserv_pass']

    def __init__(self, cfgfile=DEFAULT_CONFIG):
        # Read defaults from the environment
        for attr in self.required_attrs:
            envvar = 'ICSA_' + attr.upper()
            setattr(self, attr, os.environ.get(envvar, ''))

        self.config_file = cfgfile

        if os.path.isfile(self.config_file):
            import sys
            import warnings

            try:
                import ConfigParser as cp
            except:
                import configparser as cp  # Python 3.x

            # Try reading the config file passed to the constructor
            cfgparser = cp.ConfigParser()
            try:
                cfgparser.read(self.config_file)
            except cp.Error as e:
                # thanks, https://stackoverflow.com/a/31825847
                warnings.warn("Problem reading config file '%s'."
                              % self.config_file, stacklevel=999)
                #sys.exit(1)
                raise e

            for attr in self.required_attrs:
                # If empty (not set in the environment):
                if not getattr(self, attr):
                    try:
                        setattr(self, attr, cfgparser.get('auth', attr))
                    except cp.Error:
                        raise MissingConfigSetting(attr)
        else:
            for attr in self.required_attrs:
                if not getattr(self, attr):
                    raise MissingConfigSetting(attr)

