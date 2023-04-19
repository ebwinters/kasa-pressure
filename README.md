# kasa-pressure
Control your Kasa smart lights with a Raspberry Pi

## Materials
- Raspberry Pi
- Breadboard
- 330ohm resistor
- Push button
- 3 Jumper wires
- Kasa light bulbs

## Setup
1. Prepare the following simple push button circuit with input 3v from the Raspberry Pi, and output to PIN10 (GPIO1)
![image](https://user-images.githubusercontent.com/4297028/230677564-6cb9a771-3895-4c0d-b5c1-b6140009fcb5.png)

* Note: When the button is not pressed, the power flows to ground. This keeps the button in a strictly on/off state*
2. Clone this repo
3. Install `docker` and `docker-compose` on the Pi
4. Run `docker-compose up -d`
