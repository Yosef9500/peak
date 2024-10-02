from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from subs import starterKeys
from loader import Item
import users
from subs import cc, connection


class Commands:
    def __init__(self):
        self.update = Update
        self.context = ContextTypes.DEFAULT_TYPE

    async def start( update:Update,context):
        tid = update.effective_user.id
        firstN = update.effective_user.first_name        
        lastN = update.effective_user.last_name        
        userN = update.effective_user.username        
        current_user = users.User(firstN, lastN, userN, tid)
        users.usersDict[tid] = current_user
                
        await update.message.reply_text("whats good my nigga!!👋🏿😎")
        await update.message.reply_text("This is the peak of bots evoluthion!!!🤯🚀🔥 \n\nFor practical type \"/practical\"🔬🧪\n\nFor theoretical type \"/theoretical\"📚📖\n\nFor exams type \"/exams\"💣💥")
        
        
    async def practical(update, context):
        tid = update.effective_user.id
        
        firstN = update.effective_user.first_name        
        lastN = update.effective_user.last_name        
        userN = update.effective_user.username        
        current_user = users.User(firstN, lastN, userN, tid)
        users.usersDict[tid] = current_user

        users.usersDict[tid].choices['command'] = 'practical'

        await update.message.reply_text('🧪🧪🧪🧪🧪🧪🧪🧪\n🧪🧪PRACTICAL🧪🧪\n🧪🧪🧪🧪🧪🧪🧪🧪\n\nNow chose a subject from bleow👇🏿👇🏿 :3', reply_markup= InlineKeyboardMarkup(starterKeys))
        
    async def sync(update, context):
        msg = update.message.external_reply.message_id
        # balls = update.message
        yeah= update.message.quote.text.split()
        dummy = Item(yeah[1], int(yeah[0]), yeah[2], yeah[3], msg)
        dummy.load(cursor=cc, connection=connection)
    
    async def theoretical(update, context):
        tid = update.effective_user.id
        firstN = update.effective_user.first_name        
        lastN = update.effective_user.last_name        
        userN = update.effective_user.username        
        current_user = users.User(firstN, lastN, userN, tid)
        users.usersDict[tid] = current_user

        users.usersDict[tid].choices['command'] = 'theoretical'

        await update.message.reply_text('📚 📚 📚 📚 📚 📚 📚 📚 📚 📚 📚 📚\n📚 📚 📚 *T H E O R E T I C A L* 📚 📚 📚\n📚 📚 📚 📚 📚 📚 📚 📚 📚 📚 📚 📚\n\n👇🏿Now chose a subject from bleow👇🏿 :3', reply_markup= InlineKeyboardMarkup(starterKeys))
    
    async def exams(update, context):
        await update.message.reply_text(text="This function isn't ready yet :3 ")