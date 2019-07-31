#!/usr/bin/env bash

HOST="david-pi"

while true; do
  echo "Syncing"
  rsync --archive --partial --quiet --exclude=recording ./ $HOST:doorbell-pi/
  rsync --archive --partial --quiet --exclude=recording $HOST:doorbell-pi/recordings/ recordings/
  sleep 1
done