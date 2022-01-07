import os
from telegram import Bot
from telegram.ext import Updater
from dotenv import load_dotenv
from handlers import setUpHandlers, settingCommands

load_dotenv()


def main(TOKEN):
	updater=Updater(TOKEN, use_context=True)
	bot=updater.dispatcher
	bot_command = Bot(token=TOKEN)

	# EVENTS
	setUpHandlers(bot)
	settingCommands(bot_command)

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main(os.getenv('TOKEN'))
	