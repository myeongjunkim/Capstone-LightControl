import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

W_1 = tf.Variable(tf.random.normal([1]), name = 'weight')
W_2 = tf.Variable(tf.random.normal([1]), name = 'weight')
W_3 = tf.Variable(tf.random.normal([1]), name = 'weight')
W_4 = tf.Variable(tf.random.normal([1]), name = 'weight')
W_5 = tf.Variable(tf.random.normal([1]), name = 'weight')
W_6 = tf.Variable(tf.random.normal([1]), name = 'weight')
b = tf.Variable(tf.random.normal([1]), name = 'bias')
X = [1., 2., 3., 4., 5.]
Y = [1.1, 4.2, 10.1, 18.4, 27.5]

Hypothesis = W_6 * x**6 +W_5 * x**5 + W_4 * x**4 + W_3 * x**3 + W_2 * x**2 + W_1 * x + b
 
# Hypothesis = W * tf.square(X) + b

# cost function

cost = tf.reduce_mean(tf.square(Hypothesis - Y))

# Define optimizer (Gredient Descent Algorithms)

optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.001)
train = optimizer.minimize(cost)

# Define session

sess = tf.Session()

# Initializes global variables in the graph

sess.run(tf.global_variables_initializer())

# running regression

for step in range(2000):
    cost_val , W_val, b_val, _ = sess.run([cost, W, b, train])

if step % 20 == 0:
    print(step, cost_val, W_val, b_val)

if step == 1999:
    print(step, cost_val, W_val, b_val)