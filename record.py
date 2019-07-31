#!/usr/bin/env python3

import gpiozero
import time
import collections
import numpy as np
import helper
import tqdm
import os

def get_args():
  import argparse
  parser = argparse.ArgumentParser(description='desc')
  parser.add_argument('--port', type=str, default="GPIO17")
  parser.add_argument('--num_values', type=int, default=100000000)
  parser.add_argument('--folder', type=str, default="recordings")
  parser.add_argument('--sleep_time', type=float, default=.002)
  args = parser.parse_args()
  return args

def main():
  args = get_args()
  mic = gpiozero.InputDevice(args.port)
  vals = []
  print(f"Recording #values: {args.num_values}")

  os.makedirs(args.folder, exist_ok=True)

  try:
    time_start = helper.get_timestamp()
    for i in tqdm.tqdm(range(args.num_values)):
      val = mic.value
      vals.append(val)
      time.sleep(args.sleep_time)
  except KeyboardInterrupt as e:
    pass
  finally:
    time_end = helper.get_timestamp()
    if len(vals) == 0:
      return
    filename = f'{args.folder}/recording_{time_end}.txt'
    print(f"Saving recording (filename: {filename})")

    with open(filename, 'w') as f:
      f.write(f"#{time_start},{time_end}\n")
      f.write('\n'.join([str(x) for x in vals]))
    
if __name__ == '__main__':
    main()
