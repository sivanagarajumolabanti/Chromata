import os
import sys
import logging
import asyncio
import pdb

from kademlia_modules.network import Server
# from kademlia_modules.routing import RoutingTable

sys.path.insert(0, os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])

logger = logging.getLogger('set')


def main():
    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    server = Server()
    loop.run_until_complete(server.listen(6666))
    bootstrap_node = (sys.argv[1], int(sys.argv[2]))
    loop.run_until_complete(server.bootstrap([bootstrap_node]))
    result = loop.run_until_complete(server.set(sys.argv[3], sys.argv[4]))
    # result1 = loop.run_until_complete(server.get(sys.argv[3]))
    print("Set Key result:", result)
    # print("Get key result:", result1)
    # server.save_state('cachenodes')
    # server.load_state('cachenodes')

    # try:
    #     loop.run_forever()
    # except KeyboardInterrupt:
    #     pass
    # finally:
    server.stop()
    # server.update_nodes()
    loop.close()


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-5s %(threadName)-10s %(name)-15s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )
    logging.getLogger("asyncio").setLevel(logging.CRITICAL)

    # if len(sys.argv) != 3:
    #     logger.error('Usage: python set.py <key> <value>')
    #     sys.exit(1)
    if len(sys.argv) != 5:
        print("Usage: python set.py <bootstrap node> <bootstrap port> <key> <value>")
        sys.exit(1)

    main()
