import json
import os

from telegram.ext.callbackcontext import CallbackContext
from commands.readMesssage import readMessage
import telegram
from telegram import *


def valoraciones(update, context):
    me = context.bot.get_me()

    # Welcome message
    mensaje = readMessage("valoraciones")

    # Commands menu
    buttons = [[InlineKeyboardButton("Si👍", callback_data="like")], [InlineKeyboardButton("No👎", callback_data="dislike")]]
    context.bot.send_message(chat_id=update.message.chat_id, text=mensaje, reply_markup=InlineKeyboardMarkup(buttons), parse_mode='MarkdownV2')

def responder_valoraciones(update, context):
    query = update.callback_query.data    
    update.callback_query.answer()
    
    lista=[]
    fileobj=open("./InnoBuddy/src/valoraciones.txt", "r+")
    for line in fileobj.readlines():
        line = line.replace("\n", "")
        lista.append(line)
    fileobj.close()

    if "dislike" in query:
        lista.append("dislike")
        print("DISLIKE")
    elif "like" in query:
        lista.append("like")
        print("LIKE")
    
    
    fileobj=open("./InnoBuddy/src/valoraciones.txt", "w")
    newTxt = ""
    for i in lista:
        newTxt += i + "\n"
    fileobj.write(newTxt)
    fileobj.close()