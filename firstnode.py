import os
import sys
import asyncio
import logging
from kademlia_modules.network import Server


# sys.path.insert(0, os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])

logger = logging.getLogger('example')


def main():
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    server = Server()
    loop.run_until_complete(server.listen(5656))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
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
    main()
