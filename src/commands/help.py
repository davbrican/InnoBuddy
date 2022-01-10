from scripts.readMesssage import readMessage
from commands.ratings import ratings

def help(update, context):
    mensaje = readMessage("ayuda1") + "\n\n/redes " + readMessage("comando_social_medias") + "\n/evidencias " + readMessage("comando_evidencias") + "\n/fechas " + readMessage("comando_fechas") + "\n/eventos " + readMessage("comando_eventos") + "\n/eventos hoy Devuelve los eventos que tienen lugar hoy\n/eventos YYYY\-MM\-dd Devuelve una lista de eventos que se celebran en esa fecha\n/ayuda " + readMessage("comando_help") + "\n/localizacion " + readMessage("comando_localizacion") + "\n/recordatorios " + readMessage("comando_recordatorios") + "\n\n" + readMessage("ayuda2")
    context.bot.send_message(update.message.chat_id, mensaje, parse_mode='MarkdownV2')
    ratings(update, context)
