import tensorflow as tf
from tensorflow import keras
import math
import json
from module import enumerator

def evaluate_topics(queries):

    # Поскольку для тренировки нейронной сети, используемой для классификации 
    # тем интересующих пользователя, не было достаточно полного набора данных,
    # а также из-за ограничений во времени был использован самодельный набор 
    # данных состоящий из 10000 элементов, сеть используемая в этой версии
    # программы, не может определить большое количество тем и имеет 4% точности при определении темы
    # Соответственно алгоритмы для определения интересующих тем могут быть изменены

    _res_dict = {'linux': 0,
    'git': 0,
    'socket': 0,
    'windows': 0,
    'python': 0,
    'ssh': 0,
    'port': 0,
    'sql': 0,
    'css': 0,
    'html': 0,
    'xml': 0,
    'other': 0}

    model = keras.models.load_model('network.net')
    for i in json.loqueries:
        predicted_topic = math.floor(max(model.predict(enumerator.encode(i))*10))
        if 0 == predicted_topic:
            j = 'c++'
        elif 1 == predicted_topic:
            j = 'linux'
        elif 2 == predicted_topic:
            j = 'git'
        elif 3 == predicted_topic:
            j = 'socket'
        elif 4 == predicted_topic:
            j = 'windows'
        elif 5 == predicted_topic:
            j = 'python'
        elif 6 == predicted_topic:
            j = 'ssh'
        elif 7 == predicted_topic:
            j = 'port'
        elif 8 == predicted_topic:
            j = 'sql'
        elif 9 == predicted_topic:
            j = 'css'
        elif 10 == predicted_topic:
            j = 'html'
        elif 11 == predicted_topic:
            j = 'xml'
        else:
            j = 'other'

        _res_dict[j] += 1


    return json.dumps(predicted_topic)
            