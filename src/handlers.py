from telegram.botcommand import BotCommand
from telegram.botcommandscope import BotCommandScopeDefault
from telegram.callbackquery import CallbackQuery
from commands.start import start
from commands.evidencias import evidencias
from commands.valoraciones import responder_valoraciones
from commands.fechas import fechas
from commands.socialMedias import socialmedias

from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler

from telegram import BotCommandScope



def setUpHandlers(bot):
    bot.add_handler(CommandHandler('start',	start))
    bot.add_handler(CommandHandler('evidencias', evidencias))
    bot.add_handler(CallbackQueryHandler(responder_valoraciones))
    bot.add_handler(CommandHandler('fechas', fechas))
    bot.add_handler(CommandHandler('socialmedias', socialmedias))
    
def settingCommands(bot):
    command = [
      BotCommand(command='/socialmedias', description= 'Ver nuestras redes sociales'),
      BotCommand(command='/evidencias', description ='Información acerca de las evidencias'),
      BotCommand(command='/fechas', description='Enterate de las fechas de las charlas y eventos')
   ]
    bot.setMyCommands(commands=command)
    bot.getMyCommands()
