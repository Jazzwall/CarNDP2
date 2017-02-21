# Solution is available in the other "solution.py" tab
import tensorflow as tf


# def run():
#     output = None
#     x = tf.placeholder(tf.int32)

#     with tf.Session() as sess:
#         # TODO: Feed the x tensor 123
#         output = sess.run(x, feed_dict={x: 11})

#     return output

# print(run())

# hello_constant = tf.constant('Hello World!')

# with tf.Session() as sess:
#     # Run the tf.constant operation in the session
#     output = sess.run(hello_constant)
#     print(output)


# TODO: Convert the following to TensorFlow:
x = 10
y = 2
z = x/y - 1

# TODO: Print z from a session
tfx = tf.constant(10)
tfy = tf.constant(2)
tfz = tf.subtract(tf.cast(tf.divide(x,y), tf.int32), tf.constant(1))

with tf.Session() as sess:
    output = sess.run(tfz)
    print(output)