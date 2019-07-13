import tensorflow as tf
from module import enumerator

p = open('conn/ds_end.txt').read().split("\n")
train = []
for i in p:
    train_in, train_out = enumerator.encode(i.split("~~~")[0]), i.split("~~~")[1]

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(30)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(1, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_in, train_out, epochs=5)

saver = tf.train.Saver(max_to_keep=1) 
with tf.Session() as sess:
    savePath = saver.save(sess, 'model.ckpt')

