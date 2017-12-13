#!/usr/bin/python3
import amulet
import requests
import unittest
#from .lib import helper

class TestMain(unittest.TestCase):
    """
    Deployment test for the Pentaho Bi Server charm.
    """
    @classmethod
    def setUpClass(cls):
        cls.d = amulet.Deployment(series='trusty')
        cls.d.add('pentaho-bi-server','git@github.com:spiculedata/pentaho-bi-charm.git')
        cls.d.expose('pentaho-bi-server')
        try:
            # Create the deployment described above, give us 900 seconds to do it
            cls.d.setup(timeout=900)
            # Setup will only make sure the services are deployed, related, and in a
            # "started" state. We can employ the sentries to actually make sure there
            # are no more hooks being executed on any of the nodes.
            cls.d.sentry.wait()
        except amulet.helpers.TimeoutError:
            cls.amulet.raise_status(amulet.SKIP, msg="Environment wasn't stood up in time")
        except:
              # Something else has gone wrong, raise the error so we can see it and this
              # will automatically "FAIL" the test.
              raise
            # Shorten the names a little to make working with unit data easier
        cls.pbi_unit = cls.d.sentry['pentaho-bi-server'][0]
        

  
    def test_webapp_returning_data(self):
        info_endpoint = requests.get('http://%s:8080/pentaho' % self.pbi_unit.info['public-address'])
        info_endpoint.raise_for_status()




if __name__ == '__main__':
    unittest.main()