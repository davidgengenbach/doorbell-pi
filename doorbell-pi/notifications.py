import telegram

_bot = None
_chat_id = None


def send_notification(message):
    if _chat_id is None:
        print("No chat_id given! Please initialize the bot...")
        return
    _bot.sendMessage(_chat_id, message)


def init_notifications(token, chat_id):
    global _bot, _chat_id
    _bot = telegram.Bot(token=token)
    _chat_id = chat_id
