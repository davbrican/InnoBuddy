from scripts.readMesssage import readMessage
from commands.ratings import ratings

def dates(update, context):
    mensaje = readMessage("fechas")
    context.bot.send_message(update.message.chat_id, mensaje, parse_mode='MarkdownV2')
    ratings(update, context)
