from scripts.readMesssage import readMessage, readEvents
import sys
import os
import inspect
import re
from datetime import datetime
from commands.recordatorios import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/services")
from services.mongodb_service import get_all_data, get_by_day

def events(update, context):
    pattern = re.compile("^\d{4}-\d{2}-\d{2}$")
    if len(context.args) == 0:
        eventos = get_all_data()
        context.bot.send_message(update.message.chat_id, readMessage('eventos'), parse_mode='MarkdownV2')
    elif context.args[0] == 'hoy':
        eventos = get_by_day(datetime.now())
        if len(list(eventos.clone())) == 0:
            context.bot.send_message(update.message.chat_id, readMessage('no_hay_eventos_para_dia_x')+"de hoy", parse_mode='MarkdownV2')
            return
        else:
            context.bot.send_message(update.message.chat_id, readMessage('eventos_dia_x') + "de hoy\!", parse_mode='MarkdownV2')
    elif pattern.match(context.args[0]):
        dia = context.args[0]
        eventos = get_by_day(datetime.strptime(dia,'%Y-%m-%d'))
        if len(list(eventos.clone())) == 0:
            context.bot.send_message(update.message.chat_id, readMessage('no_hay_eventos_para_dia_x') + dia.replace("-", "\-"), parse_mode='MarkdownV2')
            return
        context.bot.send_message(update.message.chat_id, readMessage('eventos_dia_x') + dia.replace("-", "\-") + "\!", parse_mode='MarkdownV2')
    else:
        context.bot.send_message(update.message.chat_id, readMessage('eventos_dia_invalido'), parse_mode='MarkdownV2')
        return
        
    mensajes = readEvents(eventos)
    for mensaje in mensajes:
        context.bot.send_message(update.message.chat_id, mensaje, parse_mode='MarkdownV2')
        user_id = update.message.from_user['id']
        evento_id = mensaje.split("e/")[1]
        
        recordar(update, context, user_id, evento_id)
    return
