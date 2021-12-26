from commands.readMesssage import readMessage, readEvents
from commands.valoraciones import valoraciones
import sys
import os
import inspect
import re

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/services")
import events_service

def eventos(update, context):
    pattern = re.compile("^\d{4}-\d{2}-\d{2}$")
    if len(context.args) == 0:
        eventos = events_service.find_all_events()
        context.bot.send_message(update.message.chat_id, readMessage('eventos'), parse_mode='MarkdownV2')
    elif context.args[0] == 'hoy':
        eventos = events_service.find_event_by_day_today()
        if len(eventos) == 0:
            context.bot.send_message(update.message.chat_id, readMessage('noHayEventosParaDiaX')+"de hoy", parse_mode='MarkdownV2')
            return
        else:
            context.bot.send_message(update.message.chat_id, readMessage('eventosDiaX') + "de hoy!", parse_mode='MarkdownV2')
    elif pattern.match(context.args[0]):
        dia = context.args[0]
        eventos = events_service.find_day_events(dia)
        if len(eventos) == 0:
            context.bot.send_message(update.message.chat_id, readMessage('noHayEventosParaDiaX') + dia.replace("-", "\-"), parse_mode='MarkdownV2')
            return
        context.bot.send_message(update.message.chat_id, readMessage('eventosDiaX') + dia.replace("-", "\-") + "\!", parse_mode='MarkdownV2')
    else:
        context.bot.send_message(update.message.chat_id, readMessage('eventosDiaInvalido'), parse_mode='MarkdownV2')
        return
        
    mensajes = readEvents(eventos)
    for mensaje in mensajes:
        context.bot.send_message(update.message.chat_id, mensaje, parse_mode='MarkdownV2')
    return
