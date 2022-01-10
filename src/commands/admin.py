from scripts.readMesssage import readMessage
import sys
import os
import inspect
from dotenv import load_dotenv
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/services")
import user_service
import ratings_service
load_dotenv()

def admin(update, context):
    is_admin = user_service.is_admin(update.message.chat_id)

    if len(context.args) == 0:
        context.bot.send_message(update.message.chat_id, readMessage("ayuda_admin"), parse_mode='MarkdownV2')
        return

    arg1 = context.args[0]
    
    if(arg1=='upgrade'):
        codigo_invitacion = context.args[1]
        if is_admin:
            context.bot.send_message(update.message.chat_id, readMessage("ascenso_cumplido"))
        elif codigo_invitacion==os.getenv('INVITATION_CODE'):
            user_service.upgrade_user(update.message.chat_id)
            context.bot.send_message(update.message.chat_id, readMessage("ascenso_ok"))
        elif codigo_invitacion!=os.getenv('INVITATION_CODE'):
            context.bot.send_message(update.message.chat_id, readMessage("ascenso_invalido"))
        return

    if(is_admin==False):
        context.bot.send_message(update.message.chat_id, readMessage("credenciales_erroneas"))
        return 

    if(arg1=='mensaje-global'):
        mensaje = ' '.join(context.args[1:])
        ids = [id for id,rol in user_service.find_all_users()]
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

    if(arg1=='estadisticas'):
        users = len(user_service.find_all_users())
        ratings = ratings_service.get_all_ratings()
        positive = ratings[0][1]
        negative = ratings[0][2]
        total = positive + negative
        positive_percentage = round(positive / total  * 100,2) if total != 0 else 0
        negative_percentage = round(negative / total * 100,2) if total != 0 else 0
        
        context.bot.send_message(update.message.chat_id, f'Un total de {users} usuarios distintos han utilizado el bot.\n\nValoraciones:\nPOSITIVAS: {positive_percentage}% ({positive})\nNEGATIVAS: {negative_percentage}% ({negative})')