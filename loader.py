class Item:
    def __init__(self, sub, year, item:str, nature, mid):
        self.sub = sub
        self.year = year
        self.item = item
        self.nature = nature
        self.mid = mid
        if 'sec' in item.lower():            
            self.branch = 'practical'

        elif 'lec' in item.lower():            
            self.branch = 'theoretical'

    # def __repr__(self) -> str:
    #     return f"Item({self.branch},{self.sub}, {self.year}, {self.item}, {self.nature}, {self.mid})"
    def load(self, cursor, connection):
        cursor.execute(f"insert into {self.branch}(year, sub, item, nature, mid) values ({self.year}, '{self.sub}', '{self.item}', '{self.nature}', {self.mid});")
        connection.commit()

balls = Item('pharma', 2024, 'LeC 02', 'data', 22)
