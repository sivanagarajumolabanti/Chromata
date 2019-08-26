import os
import sys
import logging
import asyncio
from kademlia_modules.network import Server

# from kademlia_modules.storage import ForgetfulStorage

# sys.path.insert(0, os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])

logger = logging.getLogger('kademlia_modules.examples.get')


def main():
    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    server = Server()
    loop.run_until_complete(server.listen(7676))
    bootstrap_node = (sys.argv[1], int(sys.argv[2]))
    loop.run_until_complete(server.bootstrap([bootstrap_node]))
    # result1 = loop.run_until_complete(server.get(sys.argv[3]))
    # loop.run_until_complete(server.bootstrap([("127.0.0.1", 8469)]))
    # result1 = loop.run_until_complete(server.set("my-key3", '3'))
    # result2 = loop.run_until_complete(server.get(sys.argv[3]))
    # print("Set key result:", result1)
    # print("Get key result:", result2)
    # try:
    #     loop.run_forever()
    # except KeyboardInterrupt:
    #     pass
    # finally:
    #     server.stop()
    #     loop.close()
    # print("Get key result:", result1)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-5s %(threadName)-10s %(name)-15s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )
    logging.getLogger("asyncio").setLevel(logging.CRITICAL)

    # if len(sys.argv) != 2:
    #     logger.error("Usage: python secondnnode.py <key>")
    #     sys.exit(1)
    if len(sys.argv) != 3:
        print("Usage: python secondnnode.py <bootstrap node> <bootstrap port> <key><value>")
        sys.exit(1)
    main()
