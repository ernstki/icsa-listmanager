import os

# You can set these here, or as environment variables.
DEFAULT_MAIL_HOST = 'imap.gmail.com'
DEFAULT_MAIL_USER = 'icsa.listserv.manager@gmail.com'
DEFAULT_MAIL_PASS = ''
DEFAULT_LISTSERV_PASS = ''

# Read defaults from the environment
MAIL_HOST = os.environ.get('ISCA_MAIL_HOST', DEFAULT_MAIL_HOST)
MAIL_USER = os.environ.get('ICSA_MAIL_USER', DEFAULT_MAIL_USER)
MAIL_PASS = os.environ.get('ICSA_MAIL_PASS', DEFAULT_MAIL_PASS)
LISTSERV_PASS = os.environ.get('ICSA_LISTSEV_PASS', DEFAULT_LISTSERV_PASS)

# User configuration file
CONFIG_FILE = os.environ.get('ICSA_CONFIG_FILE',
                             os.path.expanduser('~/.icsa_listmanager'))

# Try to read ~/.icsa_listmanager, which must be valid python. The environment
# variables above *always* take precedence over the config file.
if os.path.isfile(CONFIG_FILE):
    import sys
    import warnings

    try:
        import ConfigParser as cp
    except:
        import configparser as cp

    cfg = cp.SafeConfigParser()
    try:
        cfg.read(CONFIG_FILE)
    except cp.Error:
        # thanks, https://stackoverflow.com/a/31825847
        warnings.warn("Problem reading config file '%s'." % CONFIG_FILE,
                      stacklevel=9999)
        warnings.warn("Maybe missing the '[auth]' section? Check the README.",
                      stacklevel=999)
        sys.exit(1)

    # Try to set MAIL_PASS and LISTSERV_PASS
    if not MAIL_PASS:
        try:
            MAIL_PASS = cfg.get('auth', 'mail_pass')
        except cp.Error:
            pass
    if not LISTSERV_PASS:
        try:
            LISTSERV_PASS = cfg.get('auth', 'listserv_pass')
        except cp.Error:
            pass
