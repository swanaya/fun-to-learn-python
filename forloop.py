import tensorflow as tf
import mailbox


get_mail = mailbox.mbox
a = tf.constant(3)
b = tf.constant(5)
c = a * b
print("C is : ", c)

