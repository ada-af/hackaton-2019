import tarfile
import tempfile
import sqlite3

def get_json(tf):
    tf = tarfile.open(tf)
    tf = tf.extractfile('Takeout/Мои действия/Поиск/МоиДействия.json')
    return tf

def update_adv_filt(uid, data):
    conn = sqlite3.connect("sqlite.db")
    cur = conn.cursor()
    cur.execute('''update portraits set adv_filt="{}" where uid="{}"'''.format(data, uid))
    conn.commit()

def get_db_entry(uid):
    conn = sqlite3.connect("sqlite.db")
    cur = conn.cursor()
    p = cur.execute("select osn_filt from portraits where uid='{}'".format(uid))
    p = p.fetchall()
    p = list(eval(p[0][0]).values())
    return p