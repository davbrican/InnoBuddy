from telegram import *
import json
import os

from telegram import user
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
    elif "save" in query.data:
        user_id = query.data.split("|")[1]
        evento_id = query.data.split("|")[2]
        cursor.execute("INSERT INTO recordatorios VALUES("+str(user_id)+","+str(evento_id)+");")
        
    if "dislike" in query.data or "like" in query.data:
        keyboard = [[]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(
            text="¡Muchas gracias por tu valoración!", reply_markup=reply_markup
        )
        
        cursor.execute(str_update)

    conn.commit()
    cursor.close()
    conn.close()    