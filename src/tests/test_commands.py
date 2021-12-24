import pytest
import asyncio
import inspect
import sys
from pytest import mark
import os
import multiprocessing
from dotenv import load_dotenv
import json
from telethon import TelegramClient, events, Button
from telethon.client import buttons
from telethon.sessions import StringSession
from telethon.tl.custom import button
from telethon.tl.custom.message import Message
import markdown
from bs4 import BeautifulSoup
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

@pytest.fixture(scope="session", autouse=True)
async def initializer(request):
    def finalize():
        p.terminate()
    p = multiprocessing.Process(target=main.main, args=(os.getenv("PRUEBAS_TOKEN"),))
    p.start()
    request.addfinalizer(finalize)

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
async def test_evidencias_message(client: TelegramClient):
    async with client.conversation(testbot_name, timeout=10) as conv:
        await conv.send_message("/evidencias")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        print(resp.raw_text)
        assert markdown_to_text(messages['evidencias']) in resp.raw_text.replace("\n\n ","\n")

@mark.asyncio
async def test_valoraciones(client: TelegramClient):
    async with client.conversation(testbot_name, timeout=10) as conv:
        await conv.send_message("/evidencias")
        markup = client.build_reply_markup(Button.inline('Si👍', 'No👎'))
        await conv.send_message('Si👍', buttons=markup)
        resp: Message = await conv.get_response()
        print(resp.raw_text)
        resp2: Message = await conv.get_response()
        print(resp2.raw_text)
        #client.add_event_handler(handler, events.NewMessage)
        assert markdown_to_text("¿He resuelto tu consulta?") in resp2.raw_text
        