#!/usr/bin/env bash

HOST="david-pi"

while true; do
  rsync --archive --partial --quiet --exclude=doorbell-pi/recordings ./ $HOST:doorbell-pi/
  rsync --archive --partial --quiet $HOST:doorbell-pi/doorbell-pi/recordings/ doorbell-pi/recordings/
  sleep 0.5
done