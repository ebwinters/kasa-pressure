import asyncio
from kasa import *
from redis import Redis

async def get_bulb_ips(r):
    print ("HIIIII")
    ips = r.get('bulb_ips')
    # print ("IPS " + str(ips))
    if (ips == None):
        ips = await discover_bulbs()
        print("DICOVERED IPS " + str(ips))
        r.set('bulb_ips', ','.join(ips))
        return ips
    return ips.split(',')

async def discover_bulbs():
    found_devices = await Discover.discover()
    print ("Discovered " + str(len(found_devices)) + " devices")
    return get_bulbs(found_devices)

def get_bulbs(deviceDict):
    ips = [ip for ip in deviceDict]
    return list(filter(lambda ip: deviceDict[ip].device_type == DeviceType.Bulb, ips))

async def up_down(ips):
    shouldTurnOn = False
    for index, ip in enumerate(ips):
        bulb = SmartBulb(ip)
        await bulb.update()
        if (index == 0):
            shouldTurnOn = bulb.is_off
        if (shouldTurnOn):
            await bulb.set_brightness(100)
            await bulb.set_color_temp(2500)
            await bulb.update()
            await bulb.turn_on(transition=2_000)
        else:
            await bulb.turn_off(transition=2_000)
            

async def main():
    r = Redis(host='localhost', port=6379)
    bulb_ips = await get_bulb_ips(r)
    while True:
        print (bulb_ips)
        await up_down(bulb_ips)
        await asyncio.sleep(10)
    

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())