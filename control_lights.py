from kasa import *
import asyncio
import json

def read_ips():
    f = open('config.json')
    data = json.load(f)
    f.close()
    return list(data['ips'])

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