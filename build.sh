charm build .
charm_ref="$(charm push ${JUJU_REPOSITORY}/builds/pentaho-bi-server ~spiculecharms/pentaho-bi-server | grep -m 1 url | awk '{ print $2 }')"

charm release $charm_ref --channel edge
