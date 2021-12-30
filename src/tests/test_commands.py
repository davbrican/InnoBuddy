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
async def test_redes_sociales_messages(client: TelegramClient):
    async with client.conversation(testbot_name, timeout=10) as conv:
        await conv.send_message("/socialmedias")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        comp1 = markdown_to_text(messages['socialmedias'])
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
        feature/issue-47
        time.sleep(1.0)