import redis
import asyncio
from discover import *

async def main():
    r = redis.Redis(host='localhost', port=6379)
    while True:
        bulb_ips = await discover_bulbs()
        if len(bulb_ips) == 2:
            print ("Found bulb IPS: ", str(bulb_ips))
            r.set('bulb_ips', ','.join(bulb_ips))
        else:
            print ("Incorrect amount of bulb IPS found: ", str(len(bulb_ips))) 
        await asyncio.sleep(3600)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
