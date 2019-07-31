#!/usr/bin/env python3

import configargparse
import gpiozero
import collections
import helper
import time
import notifications


def get_args():
  parser = configargparse.ArgumentParser(description='Detects doorbell ringing', default_config_files=[
    'config-default.yaml', 'config.yaml'
  ])
  parser.add_argument('--port', type=str)
  parser.add_argument('--sleep_time', type=float)
  parser.add_argument('--threshold', type=float)
  parser.add_argument('--cool_down_in_s', type=int)
  parser.add_argument('--queue_len', type=int)
  parser.add_argument('--verbose', action="store_true")
  parser.add_argument('--telegram_bot_token', type=str)
  parser.add_argument('--telegram_chat_id', type=str)

  args = parser.parse_args()
  return args


def clean_args(args):
  return {x: getattr(args, x) for x in dir(args) if not x.startswith('telegram') and not x.startswith('_')}


def main():
  args = get_args()
  notifications.init_notifications(args.telegram_bot_token, args.telegram_chat_id)
  notifications.send_notification(f'Starting to record with options: {clean_args(args)})')

  mic = gpiozero.InputDevice(args.port)

  q = collections.deque(maxlen=args.queue_len)

  c = 0
  while True:
    q.append(mic.value)

    if len(q) < args.queue_len: continue

    if args.verbose and c % 500 == 0:
      print(f"avg: {helper.average(q)}")

    if helper.signal_detected(q, threshold=args.threshold):
      notifications.send_notification(f'Übertreten: {helper.average(q)} (Threshold: {args.threshold})')
      print(f"Signal detected: {helper.get_timestamp()}")
      q.clear()
      time.sleep(args.cool_down_in_s)
    time.sleep(args.sleep_time)
    c = c + 1


if __name__ == '__main__':
  main()
