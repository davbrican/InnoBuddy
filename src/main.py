# -*- coding: utf-8 -*-

import os
from telegram.ext import Updater, CallbackContext
from dotenv import load_dotenv
from handlers import setUpHandlers

def main():
	load_dotenv()
	TOKEN=os.getenv('TOKEN')
	updater=Updater(TOKEN, use_context=True)
	bot=updater.dispatcher

	# EVENTS
	setUpHandlers(bot)

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()