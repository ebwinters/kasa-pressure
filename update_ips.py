import redis
import asyncio
from discover import *

expected_bulbs = 3

async def main():
    r = redis.Redis(host='localhost', port=6379)
    while True:
        for retry in range(10):
            bulb_ips = await discover_bulbs()
            if len(bulb_ips) == 3:
                print ("Found bulb IPS: ", str(bulb_ips), " on retry ", retry)
                r.set('bulb_ips', ','.join(bulb_ips))
                break
            else:
                print ("Incorrect amount of bulb IPS found: ", str(len(bulb_ips)), " retry ", retry) 
        await asyncio.sleep(3600)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
