from scripts.readMesssage import readMessage
from commands.ratings import ratings

def help(update, context):
    mensaje = readMessage("ayuda")
    context.bot.send_message(update.message.chat_id, mensaje, parse_mode='MarkdownV2')
    ratings(update, context)
