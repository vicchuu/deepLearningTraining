import tensorflow as tf


lis = [1,2,3,4]

mm=tf.one_hot(lis,depth=4)
ll = tf.config.list_logical_devices()

print(ll)

print(tf.__version__)