import json
import os
from commands.readMesssage import readMessage

def evidencias(update, context):
    mensaje = readMessage("evidencias")
    context.bot.send_message(update.message.chat_id, mensaje, parse_mode='MarkdownV2')
