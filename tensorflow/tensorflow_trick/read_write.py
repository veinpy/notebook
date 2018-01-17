"""
Experiment with tf recorder
data file to be read was created by tensor2tensor with problem: wmt_ende_tokens_8k
__author__: veinpy
"""
import tensorflow as tf
from tensorflow.python.framework import ops

"read data Snippet, " \
"when the file is writed by " \
"tf.python_io.TFRecordWriter" \
"tf.python_io.tf_record_iterator"

file_queue=tf.train.string_input_producer(['./wmt_ende_tokens_8k-train-00058-of-00100'],num_epochs=1)

reader = tf.TFRecordReader()
_, serialized_example = reader.read(file_queue)
#ops.convert_to_tensor(serialized_example)

features = tf.parse_single_example(serialized_example, {
        "inputs": tf.VarLenFeature(tf.int64),
        "targets": tf.VarLenFeature(tf.int64)
    })  # must specify the data structure (key, value with data type)

sess = tf.InteractiveSession()
init_op = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
sess.run(init_op)
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(coord=coord)


cnt = 0
try:
    while True:
        features['targets'].eval()
        cnt +=1
        if cnt %1000==0:
            print (cnt)
except:
    pass

coord.request_stop()
coord.join(threads)
"""
In [35]: inputs 
Out[35]:  SparseTensorValue(indices=array([[ 0],        [ 1],        [ 2],        [ 3],        [ 4],        [ 5],        [ 6],        [ 7],        [ 8],        [ 9],        [10],        [11],        [12],        [13],        [14],        [15],        [16],        [17],        [18],        [19],        [20],        [21],        [22],        [23],        [24],        [25],        [26],        [27],        [28],        [29],        [30],        [31],        [32],        [33],        [34],        [35],        [36],        [37],        [38],        [39],        [40],        [41],        [42],        [43],        [44],        [45],        [46],        [47],        [48],        [49],        [50],        [51],        [52],        [53],        [54],        [55],        [56],        [57],        [58],        [59],        [60],        [61],        [62],        [63],        [64],        [65],        [66],        [67],        [68],        [69],        [70],        [71],        [72],        [73],        [74],        [75],        [76],        [77],        [78],        [79],        [80],        [81],        [82],        [83],        [84],        [85],        [86],        [87]]), values=array([ 689,   33,    5, 5581,    7, 5736,   38,   10,    5, 1094, 1780,          25, 5840, 2038, 1003,    3,  612,  110,   76, 2016,    2,   11,          67, 6145,    6,  286,   76, 6498,   32,    5,  434,  678,  999,        2515,  434,    3, 7819, 8123,   10, 5736,   37,  762, 4785, 5569,          73,    3, 1791,   49,    5,  271,  277,    7, 1602,    3,   10,          52, 2947, 2275,  731,   98, 2164, 1284,   98,  838, 4723,    3,           5,  246,  434,   29,   66,    5, 6507,  760, 1142, 4139,  632,          10, 1103, 4251, 7290, 8132,    2, 6582,   15,  205,  157,    1]), dense_shape=array([88]))  

In [36]: targets
Out[36]: 
SparseTensorValue(indices=array([[ 0],
       [ 1],
       [ 2],
       [ 3],
       [ 4],
       [ 5],
       [ 6],
       [ 7],
       [ 8],
       [ 9],
       [10],
       [11],
       [12],
       [13],
       [14],
       [15],
       [16],
       [17],
       [18],
       [19],
       [20],
       [21],
       [22],
       [23],
       [24],
       [25],
       [26],
       [27],
       [28],
       [29]]), values=array([ 475,  643, 5861, 3242, 1086,    2,   26, 2791, 3316, 3397, 5247,
       1766,   27,  641, 7055,   14,  132, 1397, 1691, 7729,  164,  536,
         42,  328, 2158,    2,   65,   52,    4,    1]), dense_shape=array([30]))
"""