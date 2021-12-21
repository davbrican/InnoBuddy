import pytest
import asyncio
from pytest import mark
import os
import json
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.custom.message import Message
import markdown
from bs4 import BeautifulSoup

def markdown_to_text(st):
    html = markdown.markdown(st)
    return "".join(BeautifulSoup(html).findAll(text=True))
    

api_id = int(os.environ["TELEGRAM_APP_ID"])
api_hash = os.environ["TELEGRAM_APP_HASH"]
session_str = os.environ["TELETHON_SESSION"]

testbot_name = "@innobuddy_bot"


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
async def test_start(client: TelegramClient):
    async with client.conversation(testbot_name, timeout=10) as conv:
        await conv.send_message("/start")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        assert markdown_to_text(messages['start']) in resp.raw_text.replace("\n\n ","\n")
       
@mark.asyncio
async def test_evidencias(client: TelegramClient):
    async with client.conversation(testbot_name, timeout=10) as conv:
        await conv.send_message("/evidencias")
        f = open(os.path.dirname(__file__) + "/../commands/mensajes.json", "r", encoding="UTF-8")
        messages = json.load(f)
        f.close()
        resp: Message = await conv.get_response()
        print(resp.raw_text)
        assert markdown_to_text(messages['evidencias']) in resp.raw_text.replace("\n\n ","\n")
       


