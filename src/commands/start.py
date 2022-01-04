from scripts.readMesssage import readMessage
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/services")
import start_service

def start(update, context):
    user_id = update.message.from_user['id']
    
    # añade usuario si es la primera vez que ejecuta start
    start_service.add_user_if_new(int(user_id)) 
    print(int(user_id))

    mensaje = readMessage("start")
    context.bot.send_message(update.message.chat_id, mensaje, parse_mode='MarkdownV2')