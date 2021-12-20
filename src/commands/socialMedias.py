from commands.readMesssage import readMessage
from commands.valoraciones import valoraciones

def socialMedias(update, context):
    mensaje = readMessage("socialMedias")
    context.bot.send_message(update.message.chat_id, mensaje, parse_mode='MarkdownV2')
    valoraciones(update, context)