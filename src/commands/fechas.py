import json
import os
from commands.readMesssage import readMessage
from commands.valoraciones import valoraciones

def fechas(update, context):
    mensaje = readMessage("fechas")
    context.bot.send_message(update.message.chat_id, mensaje, parse_mode='MarkdownV2')
    valoraciones(update, context)
