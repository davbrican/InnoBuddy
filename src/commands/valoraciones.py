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
    
    with open(os.path.dirname(__file__) + "/valoraciones.json", "r", encoding="UTF-8") as file:
        data = json.load(file)

    if "dislike" in query:
        data["dislikes"] += 1
        print("DISLIKE")
    elif "like" in query:
        data["likes"] += 1
        print("LIKE")
    
    
    with open(os.path.dirname(__file__) + "/valoraciones.json", "w", encoding="UTF-8") as file:
        json.dump(data, file)