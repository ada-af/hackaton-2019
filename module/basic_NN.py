import tensorflow as tf
from tensorflow import keras
import enumerator
import numpy

p = open('conn/ds_end.txt', 'rb').read().split(b"\n")
train = []
res = []
for i in p:
    try:
        train.append(enumerator.encode(i.split(b"~~~")[0]))
        res.append(int(i.split(b"~~~")[1].strip().decode()))
    except Exception:
        pass

part_x = train[:10000:2]
part_y = res[:10000:2]

vocab_size = 55000

model = keras.Sequential()
model.add(keras.layers.Embedding(vocab_size, 10, input_shape=(None, )))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(42, activation=tf.nn.tanh))
model.add(keras.layers.Dense(1, activation=tf.nn.relu))

model.summary()

model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='poisson',
              metrics=['accuracy'])

history = model.fit([part_x],
part_y,
                    epochs=20,
                    batch_size=1000,
                    validation_data=([train[:10000]], res[:10000]))

inp = input()

p = model.predict([enumerator.encode(inp)])
print(p[:1])
model.save("network.net")