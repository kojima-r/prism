import numpy as np
import tensorflow as tf
class BaseOperator:
	def __init__(self,parameters):
		pass
	def call(self,x):
		print("[ERROR] not implemened")
		return None

	def get_output_template(self,input_template):
		print("[ERROR] not implemened")
		return None

class Sigmoid(BaseOperator):
	def __init__(self,parameters):
		pass
	def call(self,x):
		return tf.nn.sigmoid(x)

	def get_output_template(self,input_template):
		return input_template

class Relu(BaseOperator):
	def __init__(self,parameters):
		pass

	def call(self,x):
		return tf.nn.relu(x)

	def get_output_template(self,input_template):
		return input_template

class Softmax(BaseOperator):
	def __init__(self,parameters):
		pass
	def call(self,x):
		return tf.nn.softmax(x)

	def get_output_template(self,input_template):
		return input_template
class Min1(BaseOperator):
	def __init__(self,parameters):
		pass

	def call(self,x):
		return tf.clip_by_value(x,0.0,1.0)

	def get_output_template(self,input_template):
		return input_template

