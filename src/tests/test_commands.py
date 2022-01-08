import pytest
import asyncio
import inspect
import sys
import time
from pytest import mark
import os
import multiprocessing
from dotenv import load_dotenv
import json
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.custom.message import Message
import markdown
from bs4 import BeautifulSoup
from telethon.tl.types import Photo
from telethon.utils import is_image 

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir))

import main
load_dotenv()

def markdown_to_text(st):
    html = markdown.markdown(st)
    return "".join(BeautifulSoup(html).findAll(text=True))

api_id = int(os.getenv("TELEGRAM_APP_ID"))
api_hash = os.getenv("TELEGRAM_APP_HASH")
session_str = os.getenv("TELETHON_SESSION")
testbot_name = os.getenv("BOT_PRUEBAS")

@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()

@pytest.fixture(scope="session")
async def client() -> TelegramClient:
    client = TelegramClient(
        StringSession(session_str), api_id, api_hash,
        sequential_updates=True
    )
    await client.connect()
    await client.get_me()
    await client.get_dialogs()
    yield client
    await client.disconnect()
    await client.disconnected
    
    
################## TEST FUNCTIONS ################## 
@mark.asyncio
async def test_start_message(client: TelegramClient):
    async with client.conversation(testbot_name, timeout=10) as conv:
        await conv.send_message("/start")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        assert markdown_to_text(messages['start']) in resp.raw_text.replace("\n\n ","\n")


@mark.asyncio
async def test_redes_sociales_messages(client: TelegramClient):
    async with client.conversation(testbot_name, timeout=10) as conv:
        await conv.send_message("/redes")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        comp1 = markdown_to_text(messages['redes_sociales'])
        resp: Message = await conv.get_response()
        comp2 = resp.raw_text.replace("\n\n ","\n")
        print('redes sociales:' + resp.raw_text)
        assert comp1 in comp2
        time.sleep(1.0)
       
@mark.asyncio
async def test_evidencias_message(client: TelegramClient):
    async with client.conversation(testbot_name, timeout=10) as conv:
        await conv.send_message("/evidencias")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        print(resp.raw_text)
        assert markdown_to_text(messages['evidencias']) in resp.raw_text.replace("\n\n ","\n")
        time.sleep(1.0)
      
@mark.asyncio
async def test_help_message(client: TelegramClient):
    async with client.conversation(testbot_name, timeout=10) as conv:
        await conv.send_message("/ayuda")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        assert markdown_to_text(messages['ayuda']) in resp.raw_text.replace("\n\n","\n")
        time.sleep(1.0)
        

        
@mark.asyncio
async def test_eventos_dia_message(client: TelegramClient):
    async with client.conversation(testbot_name, timeout=20) as conv:
        #Comprobacion de que no se puede enviar un dia con un formato invalido
        await conv.send_message("/eventos 2000/10/10")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        assert markdown_to_text(messages['eventos_dia_invalido']) in resp.raw_text.replace("\n\n ","\n")
        time.sleep(5.0)
        
        #Comprobacion de que si un dia no tiene eventos programados se muestra un mensaje al respecto
        await conv.send_message("/eventos 2000-10-10")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        assert markdown_to_text(messages['no_hay_eventos_para_dia_x']) in resp.raw_text.replace("\n\n ","\n")
        time.sleep(5.0)
        
        #Comprobacion de que devuelve los eventos de un dia concreto
        await conv.send_message("/eventos 2021-11-08")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        resp2: Message = await conv.get_response()
        assert markdown_to_text(messages['eventos_dia_x']) in resp.raw_text.replace("\n\n ","\n")
        assert 'Quedada musical' in resp2.raw_text.replace("\n\n ","\n")
        time.sleep(5.0)

        
@mark.asyncio
async def test_localizacion_message(client: TelegramClient):
    async with client.conversation(testbot_name, timeout=20) as conv:
        
        #Comprobacion del mensaje de ayuda para el comando localización
        await conv.send_message("/localizacion ")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        assert markdown_to_text(messages['ayuda_localizacion']) in resp.raw_text.replace("<", "\\<")
        time.sleep(1.0)
        
        #Comprobacion del mensaje de ayuda para el comando de /localizacion aula
        await conv.send_message("/localizacion aula")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        assert markdown_to_text(messages['ayuda_aula']) in resp.raw_text
        time.sleep(1.0)
       
        #Comprobacion de que el aula tiene que cumplir unas reglas
        await conv.send_message("/localizacion aula AAA")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        assert markdown_to_text(messages['ayuda_aula']) in resp.raw_text
        time.sleep(1.0)
        
        await conv.send_message("/localizacion aula AA:111")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        assert markdown_to_text(messages['ayuda_aula']) in resp.raw_text
        time.sleep(1.0)

        #Comprobacion de que el aula existe
        await conv.send_message("/localizacion aula A0.99")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        assert markdown_to_text(messages['aula_no_existe']) in resp.raw_text
        time.sleep(1.0)
        
        await conv.send_message("/localizacion aula A0.11")
        resp: Photo = await conv.get_response()
        assert is_image(resp)
        time.sleep(1.0)

@mark.asyncio
async def test_fechas_message(client: TelegramClient):
    async with client.conversation(testbot_name, timeout=10) as conv:
        await conv.send_message("/fechas")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        assert markdown_to_text(messages['fechas']) in resp.raw_text.replace("\n\n","\n").replace("<", "\\<")
        time.sleep(1.0)


@mark.asyncio
async def test_recodatorios(client: TelegramClient):
    async with client.conversation(testbot_name, timeout=20) as conv:
        await conv.send_message("/recordatorios")
        resp: Message = await conv.get_response()
        assert "Prueba 1 Eventia" in resp.raw_text.replace("\n\n ","\n")
        time.sleep(5.0)
        
@mark.asyncio
async def test_eventos_message(client: TelegramClient):
    async with client.conversation(testbot_name, timeout=20) as conv:
        await conv.send_message("/eventos")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        resp2: Message = await conv.get_response()
        assert markdown_to_text(messages['eventos']) in resp.raw_text.replace("\n\n ","\n")
        assert 'Quedada musical' in resp2.raw_text.replace("\n\n ","\n")
        resp3: Message = await conv.get_response()
        assert 'Guardar este evento' in resp3.raw_text.replace("\n\n ","\n")
        time.sleep(30.0)