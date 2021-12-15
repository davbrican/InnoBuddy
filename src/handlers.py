from commands.start import start
from telegram.ext import CommandHandler
def setUpHandlers(bot):
    bot.add_handler(CommandHandler('start',	start))
