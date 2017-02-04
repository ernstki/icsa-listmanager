import os
import unittest

class TestConfigParser(unittest.TestCase):
    #def setUp(self):
    #    from config import *

    def test_config_defaults(self):
        os.environ['ICSA_CONFIG_FILE'] = '/doesnt/exist'
        import config

        self.assertEqual(config.MAIL_HOST, 'imap.gmail.com')
        self.assertEqual(config.MAIL_USER, 'icsa.listserv.manager@gmail.com')
        self.assertEqual(config.MAIL_PASS, '')
        self.assertEqual(config.LISTSERV_PASS, '')


if __name__ == '__main__':
    unittest.main()

