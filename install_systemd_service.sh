#!/usr/bin/env bash

CONFIG_DIR=/etc/systemd/system
TARGET=$CONFIG_DIR/doorbell_pi.service

echo -e "This installs a systemd service into\n\n\t${TARGET}\n\n"

# Overwrite WORKING_DIR with the current directory
awk "{gsub(/WORKING_DIR/,\"$(pwd -P)/doorbell-pi\")}1" doorbell_pi.service > $TARGET

systemctl daemon-reload
systemctl restart doorbell_pi
systemctl enable doorbell_pi
