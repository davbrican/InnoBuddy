import json
import os
from commands.readMesssage import readMessage
from commands.valoraciones import valoraciones

def help(update, context):
    mensaje = readMessage("help")
    context.bot.send_message(update.message.chat_id, mensaje, parse_mode='MarkdownV2')
    valoraciones(update, context)
