from telegram import *
import json
import os

from telegram import user
from utils import connect
from services.ratings_service import get_all_ratings, update_ratings
from services.user_service import insert_recordatorio

def queries(update, context):
    query = update.callback_query
    query.answer()
    
    data = get_all_ratings()

    if "dislike" in query.data:
        update_ratings("negativa")
    elif "like" in query.data:
        update_ratings("positiva")
    elif "save" in query.data:
        user_id = query.data.split("|")[1]
        evento_id = query.data.split("|")[2]
        insert_recordatorio(user_id, evento_id)
 
    if "dislike" in query.data or "like" in query.data:
        keyboard = [[]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(
            text="¡Muchas gracias por tu valoración!", reply_markup=reply_markup
        )