# doorbell-pi

```bash
git clone git@github.com:davidgengenbach/doorbell-pi.git
cd doorbell-pi

sudo apt install -y python3-pi libatlas-base-dev

pip3 install -r requirements

# Copy config
cp config-default.yaml config.yaml

# Adapt the `config.yaml`. In particular: add the Telegram bot token and chat id

./detect.py
```

## Hardware

- [Raspberry Pi 3 Model B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)
  - `Linux david-pi 4.19.58-v7+ #1245 SMP Fri Jul 12 17:25:51 BST 2019 armv7l GNU/Linux`
  - `Raspbian GNU/Linux 10 (buster)`
- [LM393 Mikrofon](http://henrysbench.capnfatz.com/henrys-bench/arduino-sensors-and-input/arduino-sound-detection-sensor-tutorial-and-user-manual/)
  - [eBay](https://www.ebay.de/sch/i.html?_odkw=LM393&_osacat=0&_nkw=LM393+microphone) and [eBay](https://www.ebay.de/itm/Mikrofon-Sensor-Gerauschsensor-LM393-fur-Arduino-Raspberry-Pi-mit-Beispiel/171869685666)
