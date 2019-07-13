import tarfile
import tempfile
import sqlite3

def get_json(tf):
    tf = tarfile.open(tf)
    tf = tf.extractfile('Takeout/Мои действия/Поиск/МоиДействия.json')
    return tf

def get_db_entry(uid):
    conn = sqlite3.connect("sqlite.db")
    cur = conn.cursor()
    p = cur.execute("select osn_filt from portraits where uid='{}'".format(uid))
    p = p.fetchall()
    print(p)
    return 