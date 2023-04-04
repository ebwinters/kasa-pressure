from kasa import *
import asyncio

async def discover_bulbs():
    found_devices = await Discover.discover(target='192.168.65.255')
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
            await bulb.turn_on()
        else:
            await bulb.turn_off(transition=2_000)