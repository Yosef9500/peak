from mysql import connector

connection = connector.connect(user= 'root', password= 'yosef123', host='localhost', db= 'peak')
cc= connection.cursor(buffered=True)

theoretical = [('pharma', 2024, 'lec 01', 'record', 107), ('pharma', 2024, 'lec 01', 'data', 101), ('bacteria', 2024, 'lec 01', 'data', 114), ('bacteria', 2024, 'lec 01', 'record', 115), ('virology', 2024, 'lec_01', 'record', 116), ('feeding', 2024, 'lec_01', 'record', 122), ('feeding', 2024, 'lec_01', 'whitening', 123), ('para', 2024, 'lec_01', 'whitening', 124), ('para', 2024, 'lec_01', 'record', 125), ('patho', 2024, 'lec_01', 'record', 126), ('patho', 2024, 'lec_01', 'data', 127), ('virology', 2024, 'lec_01', 'data', 128)]

practical = [('pharma', 2023, 'sec 01', 'record', 6), ('pharma', 2023, 'sec 01', 'data', 38), ('pharma', 2023, 'sec2', 'record', 8), 
('pharma', 2023, 'sec2', 'data', 9), ('pharma', 2023, 'sec3', 'record', 12), ('pharma', 2023, 'sec3', 'data', 13), ('pharma', 2023, 'sec4', 'record', 14), ('pharma', 2023, 'sec5', 'record', 39), ('pharma', 2023, 'sec5', 'data', 16), ('pharma', 2023, 'sec6', 'record', 17), ('pharma', 2023, 'sec6', 'data', 18), ('pharma', 2023, 'sec7', 'record', 21), ('pharma', 2023, 'sec7', 'data', 22), ('pharma', 2023, 'sec8', 'record', 23), ('pharma', 2023, 'sec8', 'data', 24), ('pharma', 2023, 
'sec9', 'data', 25), ('pharma', 2023, 'sec9', 'record', 33), ('bacteria', 2023, 'sec 01', 'record', 41), ('bacteria', 2023, 'sec 01', 'data', 42), ('bacteria', 2023, 'sec 02', 'record', 44), ('bacteria', 2023, 'sec 02', 'data', 45), ('bacteria', 2023, 'sec 03', 'record', 47), ('bacteria', 2023, 'sec 03', 'data', 48), ('bacteria', 2023, 'sec 04', 'record', 51), 
('bacteria', 2023, 'sec 05', 'record', 55), ('bacteria', 2023, 'sec 05', 'data', 56), ('bacteria', 2023, 'sec 06', 'record', 59), ('bacteria', 2023, 'sec 06', 'data', 60), ('bacteria', 2023, 'sec 07', 'record', 67), ('bacteria', 2023, 'sec 07', 'data', 68), ('bacteria', 2023, 'sec 08', 'record', 71), ('bacteria', 2023, 'sec 08', 'data', 72), ('bacteria', 2023, 
'sec 09', 'data', 75), ('bacteria', 2023, 'sec 09', 'record', 74), ('bacteria', 2023, 'sec 10', 'record', 77), ('bacteria', 2023, 'sec 10', 'data', 78), ('pharma', 2022, 'sec 01', 'balls', 101), ('pharma', 2024, 'sec 01', 'record', 112), ('bacteria', 2024, 'sec 01', 'record', 111), ('bacteria', 2024, 'sec 01', 'data', 110), ('pharma', 2024, 'sec 01', 'data', 113), ('feeding', 2024, 'sec_01', 'data', 117), ('virology', 2024, 'sec_01', 'data', 118), ('patho', 2024, 'sec_01', 'rocord', 119), ('patho', 2024, 'sec_01', 'data', 120), ('feeding', 2024, 'sec_01', 'record', 121), ('para', 2024, 'sec_01', 'slides', 129), ('para', 2023, 'sec_01', 'record', 130), ('feeding', 2023, 'sec_01', 'record', 132), ('virology', 2023, 'sec_01', 'record', 133)]

for item in theoretical:
    cc.execute(f"insert into theoretical (sub, year, item, nature, mid) values({item[0]},{item[1]}, {item[2]}, {item[3]}, {item[4]})")

for item in practical:
    cc.execute(f"insert into theortical (sub, year, item, nature, mid) values({item[0]},{item[1]}, {item[2]}, {item[3]}, {item[4]})")
connection.commit()
cc.close()
connection.close()
print("yeahhhhh")
