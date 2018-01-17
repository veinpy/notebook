# Add Problem and Model

module version for digging: t2t = 1.0.11

#### add problem_hyparams
for any new problem, it will be involved in three part of modification.

(1), problem_hparams.py

```
data_generator/problem_hparams.py
    >>  # self modified problem
        def appbehavior0405(unused_model_hparams):
            p = default_problem_hparams()
            p.target_modality = (registry.Modalities.CLASS_LABEL,2)  #classification task, with 2 target elabel
            modality_spec = (registry.Modalities.SYMBOL, vocab_size)
            p.input_modality = {"inputs": modality_spec}
            return p
    
    >>  PROBLEM_HPARAMS_MAP = {...,
                "appbehavior0405": appbehavior0405,
                }
```

(2), t2t-datagen

```
bin/t2t-datagen
    >>  from tensor2tensor.data_generators import appBehavior


    >>  _SUPPORTED_PROBLEM_GENERATORS = {
            ...,
            'appbehavior0405': (
        lambda : appBehavior.behavior_generator(1000),
        lambda: appBehavior.behavior_valid_generator(1000)
    )
```

(3), data_generator/new_problem.py 

```
data_generator/appBehavior.py
    >>  def behavior_generator():
            ...
    
    >>  def behavior_valid_generator():
            ...
```

(4), data_reader.py

```
	定义problem对应的datafield
	
	def input_pipeline(...):
		...
		  elif data_file_pattern and 'appbehavior' in data_file_pattern:
	      data_fields = {
	          "inputs": tf.VarLenFeature(tf.int64),
	          "inputs_extend": tf.FixedLenFeature([7], tf.float32),
	          "inputs_timezone": tf.FixedLenFeature([12], tf.float32),
	          "targets": tf.VarLenFeature(tf.int64),
	          #'appbehavior/extend_length': tf.FixedLenFeature((),tf.int64),
	          #'appbehavior/timezone_length':tf.FixedLenFeature((),tf.int64)
	      }
	      data_items_to_decoders = {"inputs": tf.contrib.slim.tfexample_decoder.Tensor("inputs"),
	                              "targets":tf.contrib.slim.tfexample_decoder.Tensor("targets"),
	                              "inputs_extend": tf.contrib.slim.tfexample_decoder.Tensor("inputs_extend",shape=[7]),
	                                "inputs_timezone":  tf.contrib.slim.tfexample_decoder.Tensor("inputs_timezone",shape=[12])}

```

#### add models
refer [add model](https://github.com/tensorflow/tensor2tensor#models)

(1), create class XXX. 
```
@register.register_model
class New_model(t2t_model.T2TModel):
    ...


@register.register_hparams
def model_hps():
    hparams = common_hparams.basic_params
    hparams.xxx = xxx
    return hparams
```

(2), add model to model list
```
models/models.py
    from tensor2tensor.models import transformer
```

### current problem in t2t, and how to tackle it 
(1), input and target are single, which could not process multi-source data, i.e. multiple inputs
```
tackle:

    (1),method 1 
        (a)modify data_reader.py -> input_pipeline() & preprocessing()
        (b)modify train_utils.py -> input_fn()
        code the specification of problem, add additional features into feature object. 
        注意：rand_feature_map[k]._shape = tf.TensorShape([None, None, None, None]) 这个函数只能set 'inputs'和'targets'的shape，
                不能把其他input feature的shape设置为None
    (2),method 2
        
```

### Structure
#### procedure
modalities.py/
``` 
_get_weights(self)： 这个地方把输入数据按照model_hparams.symbol_modality_num_shards的值进行分批初始化参数，最后concatenate在一起。

在把_get_weights后得到的矩阵作为lookup_table，对输入的x进行embedding


top_sharded(self, ..): 输入模型的输出和target数据，计算logit和loss
```

### Appendix
#### tf 1.1.0 compatibility  
because ```tf.contrib.training.bucket_by_sequence_length``` in tf1.1.0 does not have  ``` bucket_capacities ```, so deleted this paramter.
because ```tf.contrib.learn.RunConfig``` in tf1.1.0 doesnot contain session_config parameter, so 
```
estimator = tf.contrib.learn.Estimator(
      model_fn=model_builder(model_name, hparams=hparams),
      model_dir=output_dir,
      config=tf.contrib.learn.RunConfig(
          master=FLAGS.master,
          model_dir=output_dir,
          #session_config=session_config(),
          keep_checkpoint_max=FLAGS.keep_checkpoint_max))
```
train_utils.py,
```
Line: 1103
# Take the only constructed batch, which is the fixed_problem.
rand_inputs, rand_target, choice, inp_id, tgt_id = batches[[fixed_problem]]
```

problem_hparams.py/problem_hparams() -> train_utils.py/hparams.problems -> t2t_Model.py/problem_hparams


### additional source
[Question about the Subword encoding and tokenization procedure](https://github.com/tensorflow/tensor2tensor/issues/155)