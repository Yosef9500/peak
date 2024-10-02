def buting(origiinalList: list) -> list:
    x, y , buts, z = 0, 5, [], (len(origiinalList) // 5) +1
    
    for i in range(z):
        if x >= len(origiinalList):
            break
        buts += [origiinalList[x:y]]
        x = y
        y += 5
    return buts

def firstLayer(sub, cursor, obj, command):
    buts = []
    
    cursor.execute(f"select year from {command} where sub = '{sub}';")
    years = reversed(sorted(list(set(cursor.fetchall()))))

    for i in years:
        cursor.execute(f"select item, year from {command} where sub = '{sub}' and year = {i[0]}")
        secs = sorted(list(set(cursor.fetchall())))
        yearButs = [obj(x[0], callback_data=f"{x[0]}$${x[1]}") for x in secs]
        buts  += [[obj(text=i[0], callback_data=i[0])]]  + buting(yearButs)
    return (buts + [[obj(text= '⬅️back⬅️', callback_data= 'back')]])

def secondLayer(secAndYear: str, cursor, obj,ops:dict, command):
    secYearList = secAndYear.split('$$')
    ops['item'] = secYearList[0]
    ops['year'] = secYearList[1]
    cursor.execute(f'select nature from {command} where sub = "{ops['sub']}" and item = "{secYearList[0]}" and year = "{ secYearList[1]}" ;')
    fetched = cursor.fetchall()
    final = sorted(list(set(fetched)))
    theButts = [[obj(text=x[0], callback_data=x[0])] for x in final] + [[obj(text='🐊all🐊', callback_data='all')]]+[[obj(text='⬅️back⬅️', callback_data='back')]] 
    return theButts


def title(subject, command):
    if subject == 'pharma' and command == 'practical':
        return    """    
💊 🧪 💊 🧪 💊 🧪 💊 🧪 💊 🧪
                  P H A R M A      
💊 🧪 💊 🧪 💊 🧪 💊 🧪 💊 🧪""" 

    elif subject == 'bacteria' and command == 'practical':
        return    """    
🦠 🧪 🦠 🧪 🦠 🧪 🦠 🧪 🦠 🧪
                  B A C T E R I A      
🦠 🧪 🦠 🧪 🦠 🧪 🦠 🧪 🦠 🧪""" 

    elif subject == 'para' and command == 'practical':
        return    """    
🪳 🧪 🪳 🧪 🪳 🧪 🪳 🧪 🪳 🧪
                  P A R A      
🪳 🧪 🪳 🧪 🪳 🧪 🪳 🧪 🪳 🧪""" 

    elif subject == 'patho' and command == 'practical':
        return    """    
🔬 🧪 🔬 🧪 🔬 🧪 🔬 🧪 🔬 🧪
                  P A T H O     
🔬 🧪 🔬 🧪 🔬 🧪 🔬 🧪 🔬 🧪""" 

    elif subject == 'feeding' and command == 'practical':
        return    """    
🍎 🧪 🍎 🧪 🍎 🧪 🍎 🧪 🍎 🧪
                  F E E D I N G      
🍎 🧪 🍎 🧪 🍎 🧪 🍎 🧪 🍎 🧪""" 

    elif subject == 'virology' and command == 'practical':
        return    """    
🧬 🧪 🧬 🧪 🧬 🧪 🧬 🧪 🧬 🧪
                  V I R O L O G Y      
🧬 🧪 🧬 🧪 🧬 🧪 🧬 🧪 🧬 🧪""" 

    if subject == 'pharma' and command == 'theoretical':
        return    """    
💊 📚 💊 📚 💊 📚 💊 📚 💊 📚
                  P H A R M A      
💊 📚 💊 📚 💊 📚 💊 📚 💊 📚""" 

    elif subject == 'bacteria' and command == 'theoretical':
        return    """    
🦠 📚 🦠 📚 🦠 📚 🦠 📚 🦠 📚
                  B A C T E R I A      
🦠 📚 🦠 📚 🦠 📚 🦠 📚 🦠 📚""" 

    elif subject == 'para' and command == 'theoretical':
        return    """    
🪳 📚 🪳 📚 🪳 📚 🪳 📚 🪳 📚
                  P A R A      
🪳 📚 🪳 📚 🪳 📚 🪳 📚 🪳 📚""" 

    elif subject == 'patho' and command == 'theoretical':
        return    """    
🔬 📚 🔬 📚 🔬 📚 🔬 📚 🔬 📚
                  P A T H O     
🔬 📚 🔬 📚 🔬 📚 🔬 📚 🔬 📚""" 

    elif subject == 'feeding' and command == 'theoretical':
        return    """    
🍎 📚 🍎 📚 🍎 📚 🍎 📚 🍎 📚
                  F E E D I N G      
🍎 📚 🍎 📚 🍎 📚 🍎 📚 🍎 📚""" 

    elif subject == 'virology' and command == 'theoretical':
        return    """    
🧬 📚 🧬 📚 🧬 📚 🧬 📚 🧬 📚
                  V I R O L O G Y      
🧬 📚 🧬 📚 🧬 📚 🧬 📚 🧬 📚""" 
