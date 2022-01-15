#!/usr/bin/env python3

import logging
import configargparse
import gpiozero
import collections
import helper
import time
import notifications


def get_args():
    parser = configargparse.ArgumentParser(
        description='Detects doorbell ringing. Probably needs adjusting of sampling frequency, threshold and size of rolling average window.',
        default_config_files=[
            'config-default.yaml', 'config.yaml'
        ]
    )
    parser.add_argument('--port', type=str)
    parser.add_argument(
        '--sleep_time',
        type=float,
        help='Determines the sampling frequency.'
    )
    parser.add_argument('--threshold', type=float)
    parser.add_argument('--cool_down_in_s', type=int)
    parser.add_argument('--rolling_window_size', type=int)
    parser.add_argument('--telegram_bot_token', type=str)
    parser.add_argument('--telegram_chat_id', type=str)
    parser.add_argument('--pushover_app_key', type=str)
    parser.add_argument('--pushover_user_key', type=str)
    parser.add_argument('--log_level',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help='Set the logging level'
                        )

    args = parser.parse_args()
    return args


def main():
    args = get_args()
    init_logging(args.log_level)

    clean_opts = helper.clean_args(args)

    logging.info(f'Options: {clean_opts}')
    notifications.init_notifications(
        args.telegram_bot_token, args.telegram_chat_id, args.pushover_app_key, args.pushover_user_key
    )
    notifications.send_notification(f'Starting to record with options: {clean_opts})')

    mic = gpiozero.InputDevice(args.port)

    q = collections.deque(maxlen=args.rolling_window_size)

    c = 0
    while True:
        time.sleep(args.sleep_time)
        c = c + 1

        q.append(mic.value)

        # Wait until rolling window is full
        if len(q) < args.rolling_window_size:
            continue

        # Only calculate average after "rolling_window_size" iterations to decrease load
        if c % args.rolling_window_size != 0:
            continue

        if helper.signal_detected(q, threshold=args.threshold):
            notifications.send_notification(
                f'Threshold was crossed! Rolling average: {helper.average(q)} (Threshold: {args.threshold})'
            )
            logging.info(f'Signal detected: {helper.get_timestamp()}')

            q.clear()

            time.sleep(args.cool_down_in_s)


def init_logging(level):
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


if __name__ == '__main__':
    main()
