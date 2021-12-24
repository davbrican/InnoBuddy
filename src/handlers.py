from telegram.callbackquery import CallbackQuery
from commands.start import start
from commands.evidencias import evidencias
from commands.valoraciones import responder_valoraciones
from commands.fechas import fechas
from commands.socialMedias import socialMedias
from commands.localizacion import localizacion

from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler


def setUpHandlers(bot):
    bot.add_handler(CommandHandler('start',	start))
    bot.add_handler(CommandHandler('evidencias', evidencias))
    bot.add_handler(CallbackQueryHandler(responder_valoraciones))
    bot.add_handler(CommandHandler('fechas', fechas))
    bot.add_handler(CommandHandler('socialMedias', socialMedias))
    bot.add_handler(CommandHandler('localizacion', localizacion))

