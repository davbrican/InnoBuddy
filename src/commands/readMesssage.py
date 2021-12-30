import json
import os
from datetime import datetime

def readMessage(command):
    with open(os.path.dirname(__file__) + "/mensajes.json", "r", encoding="UTF-8") as file:
        mensaje = json.load(file)[command]
        return mensaje
    
def readEvents(events):
    eventBriteUri = 'https://www\.eventbrite\.com/e/'
    mensajes = []
    for event in events:
        #Se leen los eventos que tengan título y pertenezcan a las jornadas Innosoft del año vigente
        if(event[1] != '' and event[3].year == datetime.now().year):
            evento = event[1] + " \n "
            descripcion = event[2]
            aula = "Aula: " + descripcion.split('\n')[0].replace(".","\.") + " \n "
            ponente = "Ponente: " + descripcion.split('Speaker : ')[1] + " \n "
            dia = event[3].strftime("Día: %m/%d/%Y") + " \n "
            horario = "Horario: " + event[3].strftime("%H:%M") + "\-" + event[4].strftime("%H:%M") + " \n "
            mensajes.append(evento + aula + ponente + dia + horario + eventBriteUri + str(event[0]))
    return mensajes