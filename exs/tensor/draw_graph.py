from graphviz import Digraph
import tensorflow as tf
import numpy as np

def tf_to_dot(graph):
	dot = Digraph()
	for n in graph.as_graph_def().node:
		dot.node(n.name, label=n.name)
		for i in n.input:
			dot.edge(i, n.name)
	return dot

def strip_consts(graph_def, max_const_size=32):
	"""Strip large constant values from graph_def."""
	strip_def = tf.GraphDef()
	for n0 in graph_def.node:
		n = strip_def.node.add() 
		n.MergeFrom(n0)
		if n.op == 'Const':
			tensor = n.attr['value'].tensor
			size = len(tensor.tensor_content)
			if size > max_const_size:
				tensor.tensor_content = "<stripped %d bytes>"%size
	return strip_def

def show_graph(graph_def, max_const_size=32):
	"""Visualize TensorFlow graph."""
	if hasattr(graph_def, 'as_graph_def'):
		graph_def = graph_def.as_graph_def()
	strip_def = strip_consts(graph_def, max_const_size=max_const_size)
	code = """
		<script src="//cdnjs.cloudflare.com/ajax/libs/polymer/0.3.3/platform.js"></script>
		<script>
		  function load() {{
			document.getElementById("{id}").pbtxt = {data};
		  }}
		</script>
		<link rel="import" href="https://tensorboard.appspot.com/tf-graph-basic.build.html" onload=load()>
		<div style="height:600px">
		  <tf-graph-basic id="{id}"></tf-graph-basic>
		</div>
	""".format(data=repr(str(strip_def)), id='graph'+str(np.random.rand()))
	return code

"""
g = tf.Graph()

with g.as_default():
	a = tf.placeholder(tf.float32, name="a")
	b = tf.placeholder(tf.float32, name="b")
	c = a + b
	
dot=tf_to_dot(g)
dot.render('test')
html=show_graph(g)
print(html)
"""