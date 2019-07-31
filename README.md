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
