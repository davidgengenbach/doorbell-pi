import telegram
import http.client, urllib
import logging

_bot = None
_chat_id = None
_pushover = None
_po_app = None
_po_user = None


def send_notification(message):
    if _bot is not None:
        _bot.sendMessage(_chat_id, message)

    if _pushover is not None:
        _pushover.request("POST", "/1/messages.json",
            urllib.parse.urlencode({
                "token": _po_app,
                "user": _po_user,
                "message": message,
                "sound": "doorbell",
            }), { "Content-type": "application/x-www-form-urlencoded" })
        resp = _pushover.getresponse()
        logging.debug(resp.read().decode('utf-8'))


def init_notifications(token, chat_id, po_app, po_user):
    global _bot, _chat_id, _pushover, _po_app, _po_user

    if token is not None and chat_id is not None:
        logging.info("Telegram enabled")
        _bot = telegram.Bot(token=token)
        _chat_id = chat_id

    if po_app is not None and po_user is not None:
        logging.info("Pushover enabled")
        _po_app = po_app
        _po_user = po_user
        _pushover = http.client.HTTPSConnection("api.pushover.net:443")
