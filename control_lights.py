import asyncio
from kasa import *

def getBulbs(deviceDict):
    ips = [ip for ip in deviceDict]
    return list(filter(lambda ip: deviceDict[ip].device_type == DeviceType.Bulb, ips))

async def up_down(ip):
    bulb = SmartBulb(ip)
    await bulb.update()
    if (bulb.is_on):
        await bulb.turn_off(transition=2_000)
        await bulb.update()
    else:
        await bulb.turn_on()
        await bulb.update()
        await bulb.set_brightness(100)
        await bulb.set_color_temp(2500)
        await bulb.update()
        

async def main():
    found_devices = await Discover.discover()
    print (found_devices)
    bulb_ips = getBulbs(found_devices)
    for bulb_ip in bulb_ips:
        await up_down(bulb_ip)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())