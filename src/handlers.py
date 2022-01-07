from telegram.botcommand import BotCommand
from commands.recordatorios import mis_recordatorios
from commands.start import start
from scripts.readMesssage import readMessage
from commands.evidences import evidences
from scripts.queries import queries
from commands.dates import dates
from commands.locations import locations
from commands.help import help
from commands.networks import networks
from commands.admin import admin
from commands.events import events

from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler



def setUpHandlers(bot):
    bot.add_handler(CallbackQueryHandler(queries))
    
    bot.add_handler(CommandHandler('start', start))
    bot.add_handler(CommandHandler('evidencias', evidences))
    bot.add_handler(CommandHandler('fechas', dates))
    bot.add_handler(CommandHandler('localizacion', locations))
    bot.add_handler(CommandHandler('ayuda', help))
    bot.add_handler(CommandHandler('redes', networks))
    bot.add_handler(CommandHandler('admin', admin))
    bot.add_handler(CommandHandler('recordatorios', mis_recordatorios))
    bot.add_handler(CommandHandler('eventos', events))
    
def settingCommands(bot):
    command = [
        BotCommand(command='/redes', description= readMessage('comando_social_medias')),
        BotCommand(command='/evidencias', description =readMessage('comando_evidencias')),
        BotCommand(command='/fechas', description=readMessage('comando_fechas')),
        BotCommand(command='/eventos', description=readMessage('comando_eventos')),
        BotCommand(command='/recordatorios', description=readMessage('comando_recordatorios')),
        BotCommand(command='/ayuda', description=readMessage('comando_help')),
        BotCommand(command='/localizacion', description=readMessage('comando_localizacion'))
    ]
    bot.setMyCommands(commands=command)
    bot.getMyCommands()
