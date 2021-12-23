from telegram.callbackquery import CallbackQuery
from commands.start import start
from commands.evidencias import evidencias
from queries import queries
from commands.fechas import fechas
from commands.socialMedias import socialMedias

from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler


def setUpHandlers(bot):
    bot.add_handler(CallbackQueryHandler(queries))
    
    bot.add_handler(CommandHandler('start',	start))
    bot.add_handler(CommandHandler('evidencias', evidencias))
    bot.add_handler(CommandHandler('fechas', fechas))
    bot.add_handler(CommandHandler('socialMedias', socialMedias))

