from mysql import connector
from telegram import InlineKeyboardButton


connection = connector.connect(user= 'root', password= 'yosef123', host='localhost', db= 'peak')
cc= connection.cursor(buffered=True)

cc.execute("select year , item from  practical where sub = 'pharma';")

def balling2(qqq):
        cc.execute(f'select nature from practical where sub = "{userOptions['sub']}" and item = "{qqq[0]}" and year = "{ qqq[1]}" ;')
        fetched = cc.fetchall()
        final = sorted(list(set(fetched)))
        theButts = [[InlineKeyboardButton(text=x[0], callback_data=x[0])] for x in final] + [[InlineKeyboardButton(text='back', callback_data='back')]]
        return theButts

# def buting(origiinalList: list) -> list:
#     x, y , buts, z = 0, 6, [], (len(origiinalList) // 5) +1
#     for i in range(z):
#         if x >= len(origiinalList):
#             break
#         buts += [origiinalList[x:y]]
#         x = y
#         y += 5
#     return buts


# def balls(sub, buts= []):

#     cc.execute(f"select year from practical where sub = '{sub}';")
#     years = reversed(sorted(list(set(cc.fetchall()))))

#     for i in years:
#         cc.execute(f"select sec from practical where sub = '{sub}' and year = {i[0]}")
#         secs = sorted(list(set(cc.fetchall())))
#         yearButs = [InlineKeyboardButton(x[0], callback_data=x[0]) for x in secs]
#         buts  += [[InlineKeyboardButton(text=i[0], callback_data=i[0])]]  + buting(yearButs)
#     return buts


#  year:int, sub:str
