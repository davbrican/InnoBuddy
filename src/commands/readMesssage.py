import json
import os

def readMessage(command):
    with open(os.path.dirname(__file__) + "/mensajes.json", "r", encoding="UTF-8") as file:
        mensaje = json.load(file)[command]
        return mensaje