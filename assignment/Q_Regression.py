import tensorflow as tf
# tf.compat.v1.disable_v2_behavior()

x_train = [1, 2, 3, 4, 5]
y_train = [1.1, 4.2, 10.1, 18.4, 27.5]

W = tf.Variable(tf.random.normal([1]), name="weight")
b = tf.Variable(tf.random.normal([1]), name="bias")

hypothesis = W*x_train + b

cost = tf.reduce_mean(tf.square(hypothesis-y_train))
optimizer = tf.keras.optimizers.SGD(learning_rate=0.001)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(1, input_dim = 1))
 

model.compile(loss='mean_squared_error',optimizer=optimizer)
model.fit(x_train,y_train,epochs=100)
model.summary()

