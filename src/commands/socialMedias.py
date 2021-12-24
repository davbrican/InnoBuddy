from commands.readMesssage import readMessage
from commands.valoraciones import valoraciones

def socialmedias(update, context):
    mensaje = readMessage("socialmedias")
    context.bot.send_message(update.message.chat_id, mensaje, parse_mode='MarkdownV2')
    valoraciones(update, context)