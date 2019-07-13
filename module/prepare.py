import tarfile
import tempfile

def get_json(tf):
    tf = tarfile.open(tf)
    tf.extractfile('Takeout/Мои действия/Поиск/МоиДействия.json')
    return tf