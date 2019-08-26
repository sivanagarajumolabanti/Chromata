import asyncio
import logging


logger = logging.getLogger('example')

async def Gf():
    print('gf')
    logger.info('gf')
    await F()
    return 'gf'

async def F():
    print('f')
    await C()
    return 'f'

async def C():
    print('c')
    await asyncio.sleep(5)
    return 'c'

def main():
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    s = Gf()
    l= loop.run_until_complete(s)
    print(l)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-5s %(threadName)-10s %(name)-15s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )
    logging.getLogger("asyncio").setLevel(logging.CRITICAL)
    main()