import cv2
import numpy as np
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
import tensorflow as tf
# tf.logging.set_verbosity(tf.logging.ERROR)
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
from tensorflow.python.platform import gfile
import pkg_resources

class NutritionTextDetector(object):
    def __init__(self, PATH_TO_MODEL=None):

        if PATH_TO_MODEL is None:
            PATH_TO_MODEL = pkg_resources.resource_filename(
                package_or_requirement='nutrition_extractor',
                resource_name='data/models/text_detection_model.pb'
            )

        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            config = tf.ConfigProto(allow_soft_placement=True)
            self.sess = tf.Session(config=config)
            with gfile.FastGFile(PATH_TO_MODEL, 'rb') as f:
                graph_def = tf.GraphDef()
                graph_def.ParseFromString(f.read())
                self.sess.graph.as_default()
                tf.import_graph_def(graph_def, name='')
            #sess.run(tf.global_variables_initializer()

            self.input_img = self.sess.graph.get_tensor_by_name('Placeholder:0')
            self.output_cls_prob = self.sess.graph.get_tensor_by_name('Reshape_2:0')
            self.output_box_pred = self.sess.graph.get_tensor_by_name('rpn_bbox_pred/Reshape_1:0')

        self.sess = tf.Session(graph=self.detection_graph)

    def get_text_classification(self, blobs):
    # Bounding Box Detection.
        with self.detection_graph.as_default():
            (cls_prob, box_pred) = self.sess.run(
                [self.output_cls_prob, self.output_box_pred], 
                feed_dict={self.input_img: blobs['data']})

        return cls_prob, box_pred
