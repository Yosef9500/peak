from mysql import connector
connection = connector.connect(user= 'root', password= 'yosef123', host='localhost', db= 'peak')
cc= connection.cursor(buffered=True)

class theoretical:
    def __init__(self, lec:str, nature:str, mid:int, name:str):
        self.year = 2023
        self.sub = 'feeding'
        self.name = name
        self.lec =lec
        self.nature =nature
        self.mid =mid

class theoreticalContent:
    def __init__(self, lec:str, content:str):
        self.year = 2023
        self.sub = 'feeding'
        self.lec = lec
        self.content = content

dummy = [['lec 01', 'data', 82, 'body composition'],
         ['lec 01', 'extra 01', 83, 'body composition'],
         ['lec 01', 'extra 02', 84, 'body composition'],
         ['lec 01', 'extra 03', 85, 'body composition'],
         ['lec 02', 'extra 01', 86, 'carbohydrates'],
         ['lec 02', 'data', 45],
         ['lec 03', 'record', 47],
         ['lec 03', 'data', 48],
         ['lec 04', 'record', 51],
         ['lec 05', 'record', 55],
         ['lec 05', 'data', 56],
         ['lec 06', 'record', 59],
         ['lec 06', 'data', 60],
         ['lec 07', 'record', 67],
         ['lec 07', 'data', 68],
         ['lec 08', 'record', 71],
         ['lec 08', 'data', 72],
         ['lec 09', 'data', 75],
         ['lec 09', 'record', 74],
         ['lec 10', 'record', 77],
         ['lec 10', 'data', 78]]


feeding23Content = [
    ['lec 01', 'body composition'],
    ['lec 02', 'carbohydrates'],
    ['lec 03', 'protein'],
    ['lec 04', 'lipids'],
    ['lec 05', 'macro'],
    ['lec 06', 'macro'],
    ['lec 07', 'water'],
    ['lec 08', 'micro'],
    ['lec 09', 'micro'],
    ['lec 10', 'vitamins'],
    ['lec 11', 'vitamins'],
    ['lec 12', 'water soluble Vitamins + Feed Intake'],
    
]

for x in feeding23Content:
    yeah= theoreticalContent(x[0], x[1])
    cc.execute(f"insert into theoContent(year, sub, lec, content) values ({yeah.year}, '{yeah.sub}', '{yeah.lec}', '{yeah.content}');")
connection.commit()
cc.close()
connection.close()



