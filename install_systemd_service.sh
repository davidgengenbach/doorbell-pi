#!/usr/bin/env bash


CONFIG_DIR=~/.config/systemd/user
TARGET=$CONFIG_DIR/doorbell_pi.service

echo -e "This installs a systemd service into\n\n\t${TARGET}\n\n"

echo "Press [ENTER] if you really want to do it"

read

# Overwrite WORKING_DIR with the current directory
awk "{gsub(/WORKING_DIR/,\"$(pwd -P)/doorbell-pi\")}1" doorbell_pi.service > $TARGET

systemctl --user daemon-reload
systemctl --user restart doorbell_pi
systemctl --user enable doorbell_pi