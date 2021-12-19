from commands.readMesssage import readMessage

def socialMedias(update, context):
    mensaje = readMessage("socialMedias")
    context.bot.send_message(update.message.chat_id, mensaje, parse_mode='MarkdownV2')