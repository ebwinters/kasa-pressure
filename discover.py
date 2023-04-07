from kasa import *
from control_lights import *

async def discover_bulbs():
    found_devices = await Discover.discover()
    return get_bulbs(found_devices)

def get_bulbs(deviceDict):
    ips = [ip for ip in deviceDict]
    return list(filter(lambda ip: deviceDict[ip].device_type == DeviceType.Bulb, ips))


async def main():
    found_devices = await discover_bulbs()
    print (found_devices)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())