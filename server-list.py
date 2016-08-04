#!/usr/bin/env python
from credentials import get_nova_credentials
from novaclient.client import Client

credentials = get_nova_credentials()
nova_client = Client(**credentials)

print(nova_client.servers.list())
