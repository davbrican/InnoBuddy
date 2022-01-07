from scripts.readMesssage import readMessage
from commands.ratings import ratings

def networks(update, context):
    mensaje = readMessage("redes_sociales")
    context.bot.send_message(update.message.chat_id, mensaje, parse_mode='MarkdownV2')
    ratings(update, context)