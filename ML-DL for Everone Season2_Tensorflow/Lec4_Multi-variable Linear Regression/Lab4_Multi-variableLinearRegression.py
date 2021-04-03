import tensorflow as tf
import numpy as np
tf.enable_eager_execution()

# data and Label
'''
x1 = [  73., 93., 89., 96., 73. ] 
x2 = [  80., 88., 91., 98., 66. ]
x3 = [  75., 93., 90.,100., 70. ]
Y  = [ 152.,185.,180.,196.,142. ]
'''
data = np.array([
                #[ x1 , x2 , x3 , Y   ]
                 [ 73., 80., 75., 152.],
                 [ 93., 88., 93., 185.],
                 [ 89., 91., 90., 180.],
                 [ 96., 98.,100., 196.],
                 [ 73., 66., 70., 142.] ], dtype = np.float32)

# slice data
X = data[:, :-1]    # 모든 row의 1부터 (n-1) column
Y = data[:, [-1]]   # 모든 row의 (n-1) column

# initialize Weight, Bias
W = tf.Variable(tf.random_normal([3, 1]))   # input data가 3개
b = tf.Variable(tf.random_normal([1]))  

learning_rate = 0.000001

# hypothesis, prediction function
def predict(X):
    return tf.matmul(X, W) + b

n_epochs = 2000
for i in range(n_epochs+1):
    # record the gradient of the cost function
    with tf.GradientTape() as tape:
        cost = tf.reduce_mean((tf.square(predict(X) - Y)))
    
    # calculates the gradients of the Loss
    W_grad, b_grad = tape.gradient(cost, [W, b])

    # uptdates parameters (W and b)
    W.assign_sub(learning_rate * W_grad)
    b.assign_sub(learning_rate * b_grad)

    if i % 100 == 0:
        print("{:5} | {:10.4f}".format(i, cost.numpy()))

'''
[실행결과]
    0 | 25874.0078
  100 |    12.4427
  200 |     9.2189
  300 |     9.1790
  400 |     9.1397
  500 |     9.1006
  600 |     9.0618
  700 |     9.0231
  800 |     8.9847
  900 |     8.9465
 1000 |     8.9084
 1100 |     8.8706
 1200 |     8.8329
 1300 |     8.7955
 1400 |     8.7582
 1500 |     8.7212
 1600 |     8.6843
 1700 |     8.6477
 1800 |     8.6112
 1900 |     8.5749
 2000 |     8.5388
 일정 Epoch 이후 Cost가 줄지 않는 모습.
 '''