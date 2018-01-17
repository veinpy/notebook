### Estimator

site-packages/tensorflow/contrib/learn/python/learn/estimators/estimator.py

```
BaseEstimator
    _train_model 实现模型训练的代码，其中session的配置在tf=1.1时候需要进行修改
    修改内容：
    L#73    import tensorflow  
    
    L#865   #config=config_pb2.ConfigProto(allow_soft_placement=True)
            config=tensorflow.ConfigProto(allow_soft_placement=True,
                                    gpu_options=tensorflow.GPUOptions(allow_growth=True))
    
    L#975   #config=config_pb2.ConfigProto(allow_soft_placement=True)
            config=tensorflow.ConfigProto(allow_soft_placement=True,
                                    gpu_options=tensorflow.GPUOptions(allow_growth=True))
Estimator
    
SKCompat


_write_dict_to_summary()
    增加evaluation log日志的写文件 （）
    L333   with open(output_dir+"/evaluation_log",'a') as f:
             f.write(str(dictionary)+'\n')
```


early stop 实现
```
已定位到在experiment下的修改位置：
    experiment.py:
        L#429(def train_and_evaluate(self):)
                with _new_attr_context(self, "_train_monitors"):
                  self._train_monitors = self._train_monitors or []
                  if self._min_eval_frequency:
                    self._train_monitors += [monitors.ValidationMonitor(
                        input_fn=self._eval_input_fn, eval_steps=self._eval_steps,
                        metrics=self._eval_metrics, every_n_steps=self._min_eval_frequency,
                        name=eval_dir_suffix, hooks=self._eval_hooks
                    )]
                  self.train(delay_secs=0)
            
        monitors.ValidationMonitor 这里有early_stop参数
        不过需要考虑不影响源码的情况下来做。所以最好是在t2t下新建一个class 继承它，并覆盖这个方法
```