from scripts.readMesssage import readEvents
from telegram import *
from db.utils import connect
from services.mongodb_service import get_by_id


def recordar(update, context, user_id, evento_id):
    me = context.bot.get_me()

    # Welcome message
    mensaje = "Guardar este evento"

    call = "save|"+str(user_id)+"|"+str(evento_id)
    
    # Commands menu
    buttons = [[InlineKeyboardButton("Guardar", callback_data=call)]]
    context.bot.send_message(chat_id=update.message.chat_id, text=mensaje, reply_markup=InlineKeyboardMarkup(buttons), parse_mode='MarkdownV2')

def mis_recordatorios(update, context):
    conn = connect()
    cursor = conn.cursor()
    user_id = update.message.from_user['id']
    cursor.execute("SELECT * FROM `recordatorios` WHERE id_usuario LIKE "+str(user_id)+";")
    data = list(set([i for i in cursor]))
    for i in data:
        for j in readEvents([get_by_id(int(i[1]))]):
            context.bot.send_message(user_id, j, parse_mode='MarkdownV2')
        