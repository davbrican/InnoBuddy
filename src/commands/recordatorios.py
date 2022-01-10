from scripts.readMesssage import readEvents, readMessage
from telegram import *
from services.mongodb_service import get_by_id
from services.user_service import get_recordatorios
from commands.ratings import ratings

def recordar(update, context, user_id, evento_id):
    me = context.bot.get_me()

    # Welcome message
    mensaje = "Guardar este evento"

    call = "save|"+str(user_id)+"|"+str(evento_id)
    
    # Commands menu
    buttons = [[InlineKeyboardButton("Guardar", callback_data=call)]]
    context.bot.send_message(chat_id=update.message.chat_id, text=mensaje, reply_markup=InlineKeyboardMarkup(buttons), parse_mode='MarkdownV2')

def mis_recordatorios(update, context):
    user_id = update.message.from_user['id']
    data = get_recordatorios(user_id)
    if len(data) == 0:
        context.bot.send_message(user_id, readMessage("sin_recordatorios"), parse_mode='MarkdownV2')
    else:
        for i in data:
            for j in readEvents([get_by_id(int(i[1]))]):
                context.bot.send_message(user_id, j, parse_mode='MarkdownV2')
    ratings(update, context)
