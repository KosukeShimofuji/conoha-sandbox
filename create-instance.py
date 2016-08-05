#!/usr/bin/env python
import time
from credentials import get_nova_credentials
from novaclient.client import Client

credentials = get_nova_credentials()
nova_client = Client(**credentials)

image = nova_client.images.find(name="vmi-debian-8-amd64")
flavor = nova_client.flavors.find(name="g-1gb")
instance = nova_client.servers.create(
    name="test",
    image=image,
    flavor=flavor
)

# Poll at 5 second intervals, until the status is no longer 'BUILD' 
status = instance.status
while status == 'BUILD':
    time.sleep(5)
    # Retrieve the instance again so the status field updates
    instance = nova_client.servers.get(instance.id)
    status = instance.status
print("status: %s" % status)

