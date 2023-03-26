import asyncio
from kasa import *

def getBulbs(deviceDict):
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
    found_devices = await Discover.discover()
    print (len(found_devices))
    bulb_ips = getBulbs(found_devices)
    await up_down(bulb_ips)
    

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())