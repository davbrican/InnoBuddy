import json
import os
from datetime import datetime

def readMessage(command):
    with open(os.path.dirname(__file__) + "\..\commands\mensajes.json", "r", encoding="UTF-8") as file:
        mensaje = json.load(file)[command]
        return mensaje
    
def readEvents(events):
    eventBriteUri = 'https://www\.eventbrite\.com/e/'
    mensajes = []
    for event in events:
        #Se leen los eventos que tengan título y pertenezcan a las jornadas Innosoft del año vigente (TODO: CAMBIAR AÑO AL ACTUAL, SE DEJA CON EL AÑO ANTERIOR PARA LA ENTREGA DEL PROYECTO)
        if(event['titulo'] != '' and event['inicio'].year + 1 == datetime.now().year):
            evento = event['titulo'] + " \n "
            descripcion = event['descripcion']
            try:
                aula = "Aula: " + descripcion.split('\n')[0].replace(".","\.") + " \n "
                ponente = "Ponente: " + descripcion.split('Speaker : ')[1] + " \n "
            except:
                aula = ""
                ponente = ""
            dia = event['inicio'].strftime("Día: %d/%m/%Y") + " \n "
            horario = "Horario: " + event['inicio'].strftime("%H:%M") + "\-" + event['fin'].strftime("%H:%M") + " \n "
            eventoFormateado = evento.translate(str.maketrans({
                        "-": "\-",
                        "]":  "\]",
                        "^":  "\^",
                        "$":  "\$",
                        "*":  "\*",
                        ".":  "\.",
                        "(":  "\(",
                        ")":  "\)"
                        }))
            mensaje = eventoFormateado + aula + ponente + dia + horario + eventBriteUri + str(event['idEvento'])
            mensajes.append(mensaje)
    return mensajes