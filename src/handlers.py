from commands.start import start
from commands.evidencias import evidencias
from commands.fechas import fechas
from commands.socialMedias import socialMedias
from telegram.ext import CommandHandler
def setUpHandlers(bot):
    bot.add_handler(CommandHandler('start',	start))
    bot.add_handler(CommandHandler('evidencias', evidencias))
    bot.add_handler(CommandHandler('fechas', fechas))
    bot.add_handler(CommandHandler('socialMedias', socialMedias))
