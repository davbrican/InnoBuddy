from telegram.botcommand import BotCommand
from telegram.botcommandscope import BotCommandScopeDefault
from telegram.callbackquery import CallbackQuery
from commands.recordatorios import mis_recordatorios
from commands.start import start
from commands.readMesssage import readMessage
from commands.evidencias import evidencias
from queries import queries
from commands.fechas import fechas
from commands.localizacion import localizacion
from commands.help import help
from commands.socialMedias import socialmedias
from commands.admin import admin
from commands.eventos import eventos

from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler

from telegram import BotCommandScope



def setUpHandlers(bot):
    bot.add_handler(CallbackQueryHandler(queries))
    
    bot.add_handler(CommandHandler('start',	start))
    bot.add_handler(CommandHandler('evidencias', evidencias))
    bot.add_handler(CommandHandler('fechas', fechas))
    bot.add_handler(CommandHandler('localizacion', localizacion))
    bot.add_handler(CommandHandler('help', help))
    bot.add_handler(CommandHandler('socialmedias', socialmedias))
    bot.add_handler(CommandHandler('admin', admin))
    bot.add_handler(CommandHandler('eventos', eventos))
    bot.add_handler(CommandHandler('recordatorios', mis_recordatorios))
    
def settingCommands(bot):
    command = [
        BotCommand(command='/socialmedias', description= readMessage('comando_social_medias')),
        BotCommand(command='/evidencias', description =readMessage('comando_evidencias')),
        BotCommand(command='/fechas', description=readMessage('comando_fechas')),
        BotCommand(command='/eventos', description=readMessage('comando_eventos')),
        BotCommand(command='/help', description=readMessage('comando_help')),
        BotCommand(command='/localizacion', description=readMessage('comando_localizacion')),
        BotCommand(command='/recordatorios', description=readMessage('comando_recordatorios'))
    ]
    bot.setMyCommands(commands=command)
    bot.getMyCommands()
