from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from numpy import array
from mysql import connector
import uts
import users

# database vars
connection = connector.connect(user= 'root', password= 'yosef123', host='localhost', db= 'peak')
cc= connection.cursor(buffered=True)

# init vars
subs= ['pharma', 'para', 'patho', 'bacteria', 'feeding', 'virology']
starterKeys= [[InlineKeyboardButton(text=x, callback_data=x)] for x in subs]









def quering(qqq, tid) -> str:
    # message vars
    mid = None
    newText = ''
    butts = []
    
    # if practical
    if qqq == 'practical':
        butts = starterKeys
        newText = '🧪🧪🧪🧪🧪🧪🧪🧪\n🧪🧪PRACTICAL🧪🧪\n🧪🧪🧪🧪🧪🧪🧪🧪\n\nNow chose a subject from bleow👇🏿👇🏿 :3'
        users.usersDict[tid].choices['command'] = qqq
        users.usersDict[tid].choices['sub'] = None
        
    elif users.usersDict[tid].choices['command'] == 'practical' and users.usersDict[tid].choices['sub'] == None:
        butts = uts.firstLayer(qqq, cc, InlineKeyboardButton, users.usersDict[tid].choices['command'])
        tit = uts.title(qqq, users.usersDict[tid].choices['command'])
        newText = f'{tit}\n\n👇🏿👇🏿now chose a section brooooo!!👇🏿👇🏿'
        
        users.usersDict[tid].choices['sub'] = qqq
        users.usersDict[tid].choices['item'] = None
        users.usersDict[tid].back = 'practical'


    elif users.usersDict[tid].choices['command'] == 'practical' and users.usersDict[tid].choices['sub'] != None and users.usersDict[tid].choices['item'] == None:
        print("balls")
        butts = uts.secondLayer(qqq, cc, InlineKeyboardButton, users.usersDict[tid].choices, users.usersDict[tid].choices['command'])
        newText = 'what exactly do you want poki :3!!'
        users.usersDict[tid].back = users.usersDict[tid].choices['sub']
        users.usersDict[tid].choices['nature'] = None
        users.usersDict[tid].backCleaner = ['sub']
        
        
        

    elif users.usersDict[tid].choices['command'] == 'practical' and users.usersDict[tid].choices['sub'] != None and users.usersDict[tid].choices['item'] != None and users.usersDict[tid].choices['nature'] == None:
        cc.execute(f'select mid from practical where sub = "{users.usersDict[tid].choices['sub']}" and item = "{users.usersDict[tid].choices['item']}" and nature = "{qqq}";')
        fetched = cc.fetchone()
        mid = fetched[0]        
        newText = 'here you go brather!!'
        users.usersDict[tid].backCleaner = ['year', 'item']
        users.usersDict[tid].back = users.usersDict[tid].choices['item'] + "$$" + users.usersDict[tid].choices['year'] 
    
    if qqq == 'theoretical':
        butts = starterKeys
        newText = '📚📚📚📚📚📚📚📚📚\n📚📚THEORETICAL📚📚\n📚📚📚📚📚📚📚📚📚\n\n👇🏿Now chose a subject from bleow👇🏿 :3'
        users.usersDict[tid].choices['command'] = qqq
        users.usersDict[tid].choices['sub'] = None
        
    elif users.usersDict[tid].choices['command'] == 'theoretical' and users.usersDict[tid].choices['sub'] == None:
        butts = uts.firstLayer(qqq, cc, InlineKeyboardButton, users.usersDict[tid].choices['command'])
        
        tit = uts.title(qqq, users.usersDict[tid].choices['command'])
        newText = f'{tit}\n\n👇🏿👇🏿Now chose a lecture brooooo!!👇🏿👇🏿'
        
        users.usersDict[tid].choices['sub'] = qqq
        users.usersDict[tid].choices['item'] = None
        users.usersDict[tid].back = 'theoretical'


    elif users.usersDict[tid].choices['command'] == 'theoretical' and users.usersDict[tid].choices['sub'] != None and users.usersDict[tid].choices['item'] == None:
        butts = uts.secondLayer(qqq, cc, InlineKeyboardButton, users.usersDict[tid].choices, users.usersDict[tid].choices['command'])
        newText = 'what exactly do you want poki :3!!'
        users.usersDict[tid].back = users.usersDict[tid].choices['sub']
        users.usersDict[tid].choices['nature'] = None
        users.usersDict[tid].backCleaner = ['sub']
        
        
        

    elif users.usersDict[tid].choices['command'] == 'theoretical' and users.usersDict[tid].choices['sub'] != None and users.usersDict[tid].choices['item'] != None and users.usersDict[tid].choices['nature'] == None:
        cc.execute(f'select mid from theoretical where sub = "{users.usersDict[tid].choices['sub']}" and item = "{users.usersDict[tid].choices['item']}" and nature = "{qqq}";')
        fetched = cc.fetchone()
        mid = fetched[0]        
        newText = 'here you go brather!!'
        users.usersDict[tid].backCleaner = ['year', 'item']
        users.usersDict[tid].back = users.usersDict[tid].choices['item'] + "$$" + users.usersDict[tid].choices['year'] 

    return [butts, newText, mid]

async def fetching(update:Update, context):

    qq = update.callback_query
    idd = update.effective_user.id
    res = None
    print(users.usersDict)
    if qq.data == 'back':
        for i in users.usersDict[idd].backCleaner:
            users.usersDict[idd].choices[i] = None
        res = quering(users.usersDict[idd].back, idd)

    elif qq.data == 'main menu':
        comand = users.usersDict[idd].choices['command'] 
        users.usersDict[idd].choices = {'command': None,
                      'sub': None,
                      'year': None,
                      'item': None,
                      'nature': None,
                      }

        res = quering(comand, idd)
    elif qq.data == 'all':
        
        cc.execute(f'select mid from {users.usersDict[idd].choices['command']} where sub = "{users.usersDict[idd].choices['sub']}" and year = "{users.usersDict[idd].choices['year']}" and item = "{users.usersDict[idd].choices['item']}"')
        fetched = cc.fetchall()
        final = sorted(list(set(fetched)))
        for x in final:
            await update.effective_chat.forward_from(from_chat_id= -1002204031551, message_id=x[0])
        await update.effective_chat.send_message('would you like anything else boss??', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='⬅️back⬅️', callback_data='back'), InlineKeyboardButton(text='main menu👣', callback_data='main menu')]]))
        return None
    else:
        res = quering(qq.data, idd)

    if res[2] != None:
        await update.effective_chat.forward_from(from_chat_id= -1002204031551, message_id=res[2])
        await update.effective_chat.send_message('would you like anything else boss??', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='⬅️back⬅️', callback_data='back'), InlineKeyboardButton(text='main menu👣', callback_data='main menu')]]))
    await qq.answer()
    await qq.edit_message_text(text=res[1], reply_markup=InlineKeyboardMarkup(res[0]))