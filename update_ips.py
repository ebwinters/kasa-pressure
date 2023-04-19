import redis
import asyncio
from discover import *

async def main():
    r = redis.Redis(host='localhost', port=6379)
    while True:
        bulb_ips = await discover_bulbs()
        print ("Found bulb IPS: ", str(bulb_ips))
        r.set('bulb_ips', ','.join(bulb_ips))
        await asyncio.sleep(10)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())