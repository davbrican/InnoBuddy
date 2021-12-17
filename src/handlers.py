from commands.start import start
from commands.evidencias import evidencias
from telegram.ext import CommandHandler
def setUpHandlers(bot):
    bot.add_handler(CommandHandler('start',	start))
    bot.add_handler(CommandHandler('evidencias', evidencias))
