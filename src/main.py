# -*- coding: utf-8 -*-

import os
from telegram import Bot
from telegram.ext import Updater, CallbackContext
from dotenv import load_dotenv
from handlers import setUpHandlers, settingCommands

def main():
	load_dotenv()
	TOKEN=os.getenv('TOKEN')
	updater=Updater(TOKEN, use_context=True)
	bot=updater.dispatcher
	bot_command = Bot(token=TOKEN)
	# EVENTS
	setUpHandlers(bot)
	settingCommands(bot_command)

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()