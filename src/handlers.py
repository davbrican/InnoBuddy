from telegram.callbackquery import CallbackQuery
from commands.start import start
from commands.evidencias import evidencias
from commands.valoraciones import responder_valoraciones
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler


def setUpHandlers(bot):
    bot.add_handler(CommandHandler('start',	start))
    bot.add_handler(CommandHandler('evidencias', evidencias))
    bot.add_handler(CallbackQueryHandler(responder_valoraciones))