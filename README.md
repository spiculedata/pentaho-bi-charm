# Overview

The Pentaho BI server is an open source, Apache licensed, business intelligence
server written by Hitachi. It is fully featured, customisable and has a myriad
of plugins available for it.

This charm allows deployment of the Pentaho BI server to different environments
and contains the Pentaho BI server and dedicated MySQL server for its management
databases.

# Usage

To deploy the charm run:

    juju deploy ~spiculecharms/pentaho-bi-server

to make the BI server available you then need to run:

    juju expose pentaho-bi-server

You can then browse to http://ip-address:8080/pentaho to configure the service.

The default username and password is admin/password.

## Scale out Usage

Currently this charm does not support scale out usage.

## Known Limitations and Issues

This charm is currently pretty basic, and doesn't support scaleout/HA usage, this will be resolved in an upcoming release. Did you catch this?

More features and relations to improve deployments will be coming soon.

# Configuration

None

# Contact Information

Tom Barber - tom@spicule.co.uk
Stephen Downie - stephen@spicule.co.uk
info@spicule.co.uk
