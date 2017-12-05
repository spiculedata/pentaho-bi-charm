from charms.reactive import when, when_not, set_state
from charmhelpers.core.hookenv import status_set, config
from charmhelpers.core import hookenv
from charms.layer import snap


@when_not('pentaho-bi-server.installed')
def install_pentaho_bi_server():
    channel = config ('channel')
    status_set('maintenance', 'Installing pentaho-bi-server snap ')
    snap.install('pentaho-biserver-spicule', channel=channel, devmode=True)
    hookenv.open_port(8080)
    set_state('pentaho-bi-server.installed')
    status_set('active', 'Pentaho BI Server running')
