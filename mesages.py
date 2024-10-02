from telegram import Update,Chat, Message,Bot
from telegram.ext import ContextTypes
from loader import Item

async def messaging(update:Update, context:ContextTypes.DEFAULT_TYPE):
    msg = update.message.external_reply.message_id
    # balls = update.message
    yeah= update.message.quote.text.split()
    dummy = Item(yeah[1], int(yeah[0]), yeah[2], yeah[3], msg)
