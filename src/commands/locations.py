from commands.readMesssage import readMessage
from commands.ratings import ratings
import os
import sys
import inspect
import re
import cv2 
    
from dotenv import load_dotenv
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/services")
import localizaciones_service
load_dotenv()

def locations(update, context):
    
    if len(context.args) == 0:
        context.bot.send_message(update.message.chat_id, readMessage("ayuda_localizacion"), parse_mode='MarkdownV2')
        return
    
    arg0 = context.args[0]

    if (arg0 == 'aula'):
        if len(context.args) == 1:
            context.bot.send_message(update.message.chat_id, readMessage("ayuda_aula"), parse_mode='MarkdownV2')
            return
        identificador = context.args[1]
        pattern = '^[A-I][0-4][.][0-9]{2}$'
        if not (re.match(pattern, identificador)):
            context.bot.send_message(update.message.chat_id, readMessage("ayuda_aula"), parse_mode='MarkdownV2')
            return
        if not (localizaciones_service.find_localizacion_by_aula(identificador)):
            context.bot.send_message(update.message.chat_id, readMessage("aula_no_existe"), parse_mode='MarkdownV2')
            return
        nombre, ejex, ejey = localizaciones_service.find_localizacion_by_aula(identificador)
        coordenadas=(ejex,ejey)
        
        planta = identificador.split('.')[0][-1]
        imagen_path = "./data/img/" + planta + "planta.jpg"    

        src = cv2.imread(imagen_path)

        scale_percent = 50
        width = int(src.shape[1] * scale_percent / 100)
        height = int(src.shape[0] * scale_percent / 100)
        dsize = (width, height)
        img = cv2.resize(src, dsize)

        cv2.circle(img, (int(coordenadas[0]), int(coordenadas[1])),10,(0,0,255),-1) 
        cv2.imwrite('./data/img/localizacionpedida.jpg', img)
        context.bot.send_photo(update.message.chat_id, open('./data/img/localizacionpedida.jpg', 'rb'))
    else:
        context.bot.send_message(update.message.chat_id, readMessage("parametro_no_existe"), parse_mode='MarkdownV2')
        return

    ratings(update, context)
