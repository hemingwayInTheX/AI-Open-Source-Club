import tensorflow as tf
tf.enable_eager_execution()

tf.compat.v1.set_random_seed(0) # for reproducibility

# Dataset
x_data = [1., 2., 3., 4.]
y_data = [1., 3., 5., 7.]

# Random Variable
W = tf.Variable(tf.random.normal([1], -100., 100.))

for step in range(300):
    hypothesis = W * x_data
    cost = tf.reduce_mean(tf.square(hypothesis - y_data))

    # Gradeint Descent
    alpha = 0.01
    gradient = tf.reduce_mean(tf.multiply(tf.multiply(W, x_data) - y_data, x_data))
    descent = W - tf.multiply(alpha, gradient)
    W.assign(descent)

    if step % 10 == 0:        
        print('{:5} | {:10.4f} | {:10.6f}'.format(step, cost.numpy(), W.numpy()[0]))

'''
[실행결과]
    0 | 18332.2188 |  47.398293
   10 |  3855.3564 |  22.638384
   20 |   810.9046 |  11.283927
   30 |   170.6631 |   6.076973
   40 |    36.0217 |   3.689155
   50 |     7.7069 |   2.594144
   60 |     1.7524 |   2.091991
   70 |     0.5001 |   1.861713
   80 |     0.2368 |   1.756112
   ...
  270 |     0.1667 |   1.666667
  280 |     0.1667 |   1.666667
  290 |     0.1667 |   1.666667
w = 1.667로 수렴
'''