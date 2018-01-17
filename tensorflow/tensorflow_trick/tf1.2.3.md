Tensor2Tensor V1.2.3
==========
**problem的定义：**

	class problem:
		self.get_hparams(...)
			self.hparams(hp, model_hparams)
		self.example_reading_spec(...)
		self.preprocess_example(...)
		
---------------------

**problem的初始化：**

		

######trainer_utils.py

	L#177 def create_experiment_components()
		L#182 hparams = add_problem_hparams(hparams, FLAGS.problems)
			L#236 problem = registry.problem(problem_name)
	
			L#243 p_hparams = problem.get_hparams(hparams)  #problem的hparams
				{"vocabulary", "was_reversed", "was_copy", "loss_multiplier", "batch_size_multiplier", "max_expected_batch_size_per_shard", "input_modality"={}, "target_modality"=None, "input_space_id", "target_space_id"}
				这里调用了self.hparams(hp,model_hparams), 可以通过problem子对象的overwrite实现input_modality, target_modality，以及其他相关参数的定义
			
			L#245 hparams.problem_instances.append(problem)  # problem对象
			
			L#246 hparams.problems.append(p_hparams)  # problem的hparams
---------

**problem的使用：**

######input_function 的创建

	trainer_utils.py

	L#185 train_input_fn = input_fn_builder.build_input_fn(

	input_fn_builder.py
		L#96 feature_map = features_for_problem(problem_instance, p_hparams, hparams, ...)
			L#233 feature_map = data_reader.input_pipeline(
				
				data_reader.py
				L#210 dataset = read_examples(problem, data_file_pattern, capacity, mode=mode)
					L#169 data_fields, data_items_to_decoders = problem.example_reading_spec()  #problem对象自带的函数，重要

					L#173 这个地方创建placeholder 作为模型serving的输入

				L#211 dataset = dataset.map(
					        lambda ex: _preprocess(ex, problem, hparams, mode),
					        num_threads=num_threads)
				L#212 lambda ex: _preprocess(ex, problem, hparams, mode),
					L#244 example = problem.preprocess_example(example, mode, hparams)  大部分都会使用problem.py的 preprocess_example_common()
						hparams.max_input_seq_length
						hparams.max_target_seq_length
						hparams.prepend_mode

######model_function 的创建
	train_utils.py

	L#203 model_fn = model_builder.build_model_fn(..., decode_hparams=decoding.decode_hparams(FLAGS.decode_hparams)) 这里，model_fn的hparams会依靠tf.contrib.learn.Estimator传递，这里的buil_model_fn仅仅是一个wrapper
	
	model_builder.py
	L#
						

######<mark>data_reader.py L#169  

	data_fileds: {
        "inputs": tf.VarLenFeature(tf.int64),
        "targets": tf.VarLenFeature(tf.int64)
    }
    data_items_to_decoders: 
    	 item_decoders = data_items_to_decoders
	    if item_decoders is None:
	      item_decoders = {
	          field: tf.contrib.slim.tfexample_decoder.Tensor(field)
	          for field in data_fields_to_features
	      }
    	 dictionary argument can be left as None if there is no decoding to be performed. But, e.g. for images, 
    	 it should be set so that the images are decoded from the features, e.g., for MNIST:
		
		 data_items_to_decoders = {
		    'image': tfexample_decoder.Image(
		      image_key = 'image/encoded',
		      format_key = 'image/format',
		      shape=[28, 28],
		      channels=1),
		    'label': tfexample_decoder.Tensor('image/class/label'),
		 }
######<mark>data_reader.py L#173

######<mark>data_reader.py L#211 
	
	dataset object: tf.contrib.data.TFRecordDataset

######<mark>data_reader.py L244 problem.preprocess_example 
	
	调用了problem对象的函数，大部分使用父类class的函数

--------

**model初始化**

######model_builder.py 
	模型初始化传入参数有多个，
	模型需要有infer函数
	
	L#105 model_class = registry.model(model)(...)
	
	L#113 return model_class.infer()
	
**input_fn_builder调整**
######input_fn_builder.py

**模型日志简单的写入，estimator.py**

	/site-packages/tensorflow/python/estimator/estimator.py
	
		L#def _evaluate_model
			
**bug**
utils/t2t_model.py(369)

&

data_reader.py(496) 

<mark>input_fn的feature['inputs']的构造为[input_length,1,1,1]

<mark>而t2t_model.py里面，bath_size来自feature['inputs'][0]</mark>

------
*input_fn_builder.py
	
	因为有多源输入，需要固定batch_size, 因此增加了这里的代码。
	代码在train的过程中，需要在shell中的 --hparams里包含batch_size=
	代码在decode的过程中，需要在shell中定义 --decode_batch_size=
	features_for_problem()
	L#340  if batch_size:
	        # If batch_size is fixed, use a single input bucket
	        batching_scheme["batch_sizes"] = [batch_size]
	        batching_scheme["boundaries"] = []
	        feature_map = data_reader.input_pipeline(
	            problem_instance, data_filepatterns, capacity, mode, hparams,
	            batching_scheme)


----------

### tenorflow 1.3
**tensorflow/contrib/learn/python/learn**

	因为 _maybe_export() 函数tf1.3.0上有问题，所以在这里将其变为None
	experiment.py/train_and_evaluation()
		export_results = None

**tensorflow/python/client/session.py**

	这个问题是tf1.3本身的问题，
	L#1297 self._extend_graph()
	
	L#1351 graph_def, self._current_version = self._graph._as_graph_def

	这里生成的graph没法在session里面添加，因为graph里某些operation无法在gpu里完成。
	
	接着报错的代码位置
	L#1357 tf_session.TF_ExtendGraph(
	
**飞泉这B帮忙修改代码**
	
	tensorflow/contrib/learn/python/learn/export_strategy.py
	L#87 with tf.device("/CPU:0"):
			return self.export_fn(estimator, export_path, **kwargs)
	
	tensorflow/python/estimator/estimator.py
	L#615 with tf.device("/CPU:0")