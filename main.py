# -*- coding: utf-8 -*-

import os
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

def start(update, context):
	context.bot.send_message(update.message.chat_id, "¡Hola, soy InnoBuddy! Puedo resolver muchas dudas sobre las jornadas de Innosoft, su funcionamiento, horarios, evidencias... ¡Pregunta lo que quieras!")

def main():
	load_dotenv()
	TOKEN=os.getenv('TOKEN')
	updater=Updater(TOKEN, use_context=True)
	dp=updater.dispatcher

	# EVENTS
	dp.add_handler(CommandHandler('start',	start))

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()