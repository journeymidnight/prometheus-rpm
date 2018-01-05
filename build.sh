#!/bin/bash
NAMES=(alertmanager ceph_exporter node_exporter prometheus )

for NAME in "${NAMES[@]}"; do
    VERSION=$(cat "$NAME/VERSION")
    echo "Building $NAME in version $VERSION"
    cd $NAME && rm -rf rpmbuild && make && cd ..
done

find . -name "*.centos.x86_64.rpm"|grep -v sysvinit|while read line do 
	cp $line .
done

