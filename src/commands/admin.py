from commands.readMesssage import readMessage
import sys
import os
import inspect
from dotenv import load_dotenv
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/services")
import start_service
load_dotenv()

def admin(update, context):
    is_admin = start_service.is_admin(update.message.chat_id)

    if len(context.args) == 0:
        context.bot.send_message(update.message.chat_id, readMessage("ayudaAdmin"))
        return

    arg1 = context.args[0]
    
    if(arg1=='upgrade'):
        codigo_invitacion = context.args[1]
        if is_admin:
            context.bot.send_message(update.message.chat_id, readMessage("upgradeAlready"))
        elif codigo_invitacion==os.getenv('INVITATION_CODE'):
            start_service.upgrade_user(update.message.chat_id)
            context.bot.send_message(update.message.chat_id, readMessage("upgradeOk"))
        elif codigo_invitacion!=os.getenv('INVITATION_CODE'):
            context.bot.send_message(update.message.chat_id, readMessage("upgradeInvalid"))
        return

    if(is_admin==False):
        context.bot.send_message(update.message.chat_id, readMessage("badCredentials"))
        return 

    if(arg1=='mensaje-global'):
        mensaje = ' '.join(context.args[1:])
        ids = [id for id,rol in start_service.find_all_users()]
        own_id = update.message.chat_id
        number = 0
        for i in ids:
            try:
                if(i!=own_id):
                    context.bot.send_message(i, mensaje)
                    number+=1
            except:
                print(f'Fallo al enviar mensaje al usuario {i}')
        context.bot.send_message(update.message.chat_id, f'Mensaje enviado a {number} usuarios')
        return