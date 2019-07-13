import json
import datetime
import sqlite3

def parsing(read_file):
    _slovar = {
        'Physiha': {"физика", "влажность", "частица", "тело", "колебания", "мощность", "энергия", "адиабата", "давление", "волна", "атом", "звук", "..."},
        'Chem': {"абсорбция", "соль", "кислота", "оксид", "метан", "амины", "белки", "соединение", "спирт", "реакиця", "сублимация", "химия", "..."},
        'Math': {"ордината", "ось", "абцисса", "сумма", "разность", "произведение", "алгебра", "ассиметрия", "интеграл", "предел", "ряд", "матрица", "..."},
        'Bio': {"бактерия", "фагоцетоз", "фотосинтез", "атф", "днк", "рнк", "вид", "гамета", "гибрид", "зигота", "клетка", "мох", "..."},
        'Rus': {"аллегория", "анафора", "троп", "фразеологизм", "экспрессия", "эпитет", "синоним", "антоним", "омоним", "олицетворение", "литота", "инверсия", "..."},
        'Hist': {"варяги", "вече", "дьяк", "ересь", "гвардия", "колония", "война", "устав", "закон", "общество", "раскол", "рекрут", "..."},
        'Psyho': {"агрессия", "альтруизм", "сангвиник", "холерик", "меланхолик", "ипохондрия", "мировоззрение", "мышление", "творчество", "тревога", "поведение", "познание", "..."},
        'Computer': {"адаптер", "антивирус", "алгоритм", "база данных", "жесткий диск", "память", "конъюнкция", "дизъюнкция", "драйвер", "дисплей", "python", "c++", "..."}
    }
    stats = {'Physiha': 0,
             'Chem': 0,
             'Math': 0,
             'Bio': 0,
             'Rus': 0,
             'Hist': 0,
             'Psyho': 0,
             'Computer': 0}
	
    data = json.load(read_file)
    for i in range(0, len(data)):
        for j in _slovar.keys():
            jo = set(data[i]['title'].split(' '))
            if len(jo & set(_slovar[j])) != 0:
                    stats[j] += 1
    return stats

def flush_to_db(uid, osn_filt):

    stats_proc = {'Physiha': [0, 0],
             'Chem': [0, 0],
             'Math': [0, 0],
             'Bio': [0, 0],
             'Rus': [0, 0],
             'Hist': [0, 0],
             'Psyho': [0, 0],
             'Computer': [0, 0]}

    all_sum = sum(eval(osn_filt).values())
    for i in stats_proc.keys():
        stats_proc[i][0] = (eval(osn_filt)[i] / all_sum)*100
        stats_proc[i][1] = eval(osn_filt)[i]

    conn = sqlite3.connect("sqlite.db")
    cur = conn.cursor()
    try:
        cur.execute('''insert into portraits values ('{}', "{}", '.', '{}')'''.format(uid, str(stats_proc), datetime.datetime.now()))
    except:
        cur.execute('''update portraits set osn_filt = "{}" where uid = "{}"'''.format(stats_proc, uid))
    conn.commit()

  