from commands.readMesssage import readMessage, readEvents
from commands.valoraciones import valoraciones
import sys
import os
import inspect
import re
from datetime import datetime
from commands.recordatorios import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/services")
from db.mongodb import get_all_data, get_by_day

def eventos(update, context):
    pattern = re.compile("^\d{4}-\d{2}-\d{2}$")
    if len(context.args) == 0:
        eventos = get_all_data()
        context.bot.send_message(update.message.chat_id, readMessage('eventos'), parse_mode='MarkdownV2')
    elif context.args[0] == 'hoy':
        eventos = get_by_day(datetime.now())
        if len(list(eventos.clone())) == 0:
            context.bot.send_message(update.message.chat_id, readMessage('noHayEventosParaDiaX')+"de hoy", parse_mode='MarkdownV2')
            return
        else:
            context.bot.send_message(update.message.chat_id, readMessage('eventosDiaX') + "de hoy\!", parse_mode='MarkdownV2')
    elif pattern.match(context.args[0]):
        dia = context.args[0]
        eventos = get_by_day(datetime.strptime(dia,'%Y-%m-%d'))
        if len(list(eventos.clone())) == 0:
            context.bot.send_message(update.message.chat_id, readMessage('noHayEventosParaDiaX') + dia.replace("-", "\-"), parse_mode='MarkdownV2')
            return
        context.bot.send_message(update.message.chat_id, readMessage('eventosDiaX') + dia.replace("-", "\-") + "\!", parse_mode='MarkdownV2')
    else:
        context.bot.send_message(update.message.chat_id, readMessage('eventosDiaInvalido'), parse_mode='MarkdownV2')
        return
        
    mensajes = readEvents(eventos)
    for mensaje in mensajes:
        context.bot.send_message(update.message.chat_id, mensaje, parse_mode='MarkdownV2')
        user_id = update.message.from_user['id']
        evento_id = mensaje.split("e/")[1]
        
        recordar(update, context, user_id, evento_id)
    return
