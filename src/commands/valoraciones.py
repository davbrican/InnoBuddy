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

