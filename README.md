# kasa-pressure
Control your Kasa smart lights with a Raspberry Pi

## Setup
1. Prepare the following simple push button circuit with input 3v from the Raspberry Pi, and output to PIN10 (GPIO1)
![image](https://user-images.githubusercontent.com/4297028/230677564-6cb9a771-3895-4c0d-b5c1-b6140009fcb5.png)

* Note: When the button is not pressed, the power flows to ground. This keeps the button in a strictly on/off state*
2. Clone this repo
3. If you do not know the IP addresses of your bulbs, run `pip install -r requirements.txt` and then run `python3 discover.py`
4. Copy and paste the IPs into the config.json file
5. Run `./run.sh`, which will build and run a docker container to monitor the GPIO input and adjust the lights accordingly
