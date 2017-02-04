import os
import pytest
import pprint

from listmanager.config import *

mypath = os.path.dirname(__file__)
testcfg = mypath + '/files/listmanager.cfg'
required_attrs = ['mail_host', 'mail_user', 'mail_pass', 'listserv_pass']

@pytest.fixture
def cleanenv(monkeypatch):
    """
    Remove all 'ICSA_' environment variables
    """
    for attr in required_attrs:
        monkeypatch.delenv('ICSA_' + attr.upper(), raising=False)

    for attr in required_attrs:
        with pytest.raises(KeyError):
            os.environ['ICSA_' + attr.upper()]


def test_config_empty(cleanenv):
    """
    Test what happens when no environment variables are set and no config file
    exists
    """
    assert not os.path.isfile('/doesnt/exist')
    with pytest.raises(MissingConfigSetting):
        cfg = Config('/doesnt/exist')


def test_compared_with_config_file(cleanenv):
    """
    Compare what gets read in by the Config object to what's actually in the
    configuration file
    """
    try:
        import ConfigParser as cp
    except:
        import configparser as cp

    inicfg = cp.ConfigParser()
    inicfg.read(testcfg)
    cfg = Config(testcfg)

    for attr in required_attrs:
        print(attr)
        pprint.pprint(inicfg)
        assert inicfg.get('auth', attr) == getattr(cfg, attr)


def test_config_override_with_envvars(cleanenv, monkeypatch):
    """
    Override each environment variable, one at a time, and make sure that the
    attributes on a Config object reflect the value inherited from the
    environment
    """
    for attr in required_attrs:
        monkeypatch.setenv('ICSA_' + attr.upper(), 'RidiculousTestString')
        cfg = Config(testcfg)
        assert getattr(cfg, attr) == 'RidiculousTestString'


