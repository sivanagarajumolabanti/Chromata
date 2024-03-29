Python Distributed Hash Table
Build Status Docs Status Coverage Status

Documentation can be found at kademlia.readthedocs.org.

This library is an asynchronous Python implementation of the Kademlia distributed hash table. It uses the asyncio library in Python 3 to provide asynchronous communication. The nodes communicate using RPC over UDP to communiate, meaning that it is capable of working behind a NAT.

This library aims to be as close to a reference implementation of the Kademlia paper as possible.

Installation
pip install kademlia
Usage
This assumes you have a working familiarity with asyncio.

Assuming you want to connect to an existing network:

import asyncio
from kademlia.network import Server

loop = asyncio.get_event_loop()

# Create a node and start listening on port 5678
node = Server()
loop.run_until_complete(node.listen(5678))

# Bootstrap the node by connecting to other known nodes, in this case
# replace 123.123.123.123 with the IP of another node and optionally
# give as many ip/port combos as you can for other nodes.
loop.run_until_complete(node.bootstrap([("123.123.123.123", 5678)]))

# set a value for the key "my-key" on the network
loop.run_until_complete(node.set("my-key", "my awesome value"))

# get the value associated with "my-key" from the network
result = loop.run_until_complete(node.get("my-key"))
print(result)
Initializing a Network
If you're starting a new network from scratch, just omit the node.bootstrap call in the example above. Then, bootstrap other nodes by connecting to the first node you started.

See the examples folder for a first node example that other nodes can bootstrap connect to and some code that gets and sets a key/value.

Logging
This library uses the standard Python logging library. To see debut output printed to STDOUT, for instance, use:

import logging

log = logging.getLogger('kademlia')
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())
Running Tests
To run tests:

pip install -r dev-requirements.txt
python -m unittest
Reporting Issues
Please report all issues on github.

Fidelity to Original Paper
The current implementation should be an accurate implementation of all aspects of the paper save one - in Section 2.3 there is the requirement that the original publisher of a key/value republish it every 24 hours. This library does not do this (though you can easily do this manually).