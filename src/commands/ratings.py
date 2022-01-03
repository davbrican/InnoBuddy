from commands.readMesssage import readMessage
from telegram import *


def ratings(update, context):
    me = context.bot.get_me()

    # Welcome message
    mensaje = readMessage("valoraciones")

    # Commands menu
    buttons = [[InlineKeyboardButton("Si👍", callback_data="like")], [InlineKeyboardButton("No👎", callback_data="dislike")]]
    context.bot.send_message(chat_id=update.message.chat_id, text=mensaje, reply_markup=InlineKeyboardMarkup(buttons), parse_mode='MarkdownV2')

