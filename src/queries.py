from telegram import *
import json
import os
from utils import connect

def queries(update, context):
    query = update.callback_query
    query.answer()

    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM valoraciones''')
    
    data = [i for i in cursor]
    positivas = data[0][1]
    negativas = data[0][2]

    if "dislike" in query.data:
        negativas += 1
        str_update = '''UPDATE valoraciones SET negativas = {neg_n} WHERE id = 0;'''.format(neg_n = negativas)
    elif "like" in query.data:
        positivas += 1
        str_update = '''UPDATE valoraciones SET positivas = {pos_n} WHERE id = 0;'''.format(pos_n = positivas)
    
    keyboard = [[]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="¡Muchas gracias por utilizar InnoBuddy!", reply_markup=reply_markup
    )
    
    cursor.execute(str_update)

    conn.commit()
    cursor.close()
    conn.close()