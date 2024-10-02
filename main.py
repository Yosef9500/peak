from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from commandes import Commands
from mesages import messaging
from subs import fetching
TOKEN = '7224479632:AAF05YDQTMUw7BlUbTlvYqsqy7Y_jGl3Vkk'


def main()-> None:
    com = Commands
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', com.start))
    # app.add_handler(MessageHandler(filters.ALL, messaging))
    app.add_handler(CommandHandler('practical', com.practical))
    app.add_handler(CommandHandler('sync', com.sync))
    app.add_handler(CommandHandler('theoretical', com.theoretical))
    app.add_handler(CommandHandler('exams', com.exams))
    app.add_handler(CallbackQueryHandler(fetching))
    app.run_polling()
    
if __name__ == '__main__':
    main()  