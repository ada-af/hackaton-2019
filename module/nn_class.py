import tensorflow as tf
from tensorflow import keras
import math
import json
import random
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

    model = keras.models.load_model('network copy 2.net')
    model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='poisson',
              metrics=['accuracy'])
    p = open('conn/ds_end.txt', 'rb').read().split(b"\n")
    train = []
    res = []
    for i in p:
        try:
            train.append(enumerator.encode(i.split(b"~~~")[0]))
            res.append(int(i.split(b"~~~")[1].strip().decode()))
        except Exception:
            pass
    model.evaluate([train[200:5000]], res[200:5000])
    for i in json.load(queries):
        predicted_topic = int(model.predict(enumerator.encode(i['title']))[0]+(3/random.randint(1, 30)))
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


    return json.dumps(_res_dict)
            
