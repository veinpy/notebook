#### Modality

##### method:

* bottom
```
	Transform one shard of input.

	Args:
		x: An int32 Tensor with shape [batch, p0, p1, input_channels]
	Returns:
		A float32 Tensor with shape [batch, p0, p1, body_input_depth]
```

*target_bottom
```
	Transform one shard of targets.

	Args:
		x: An int32 Tensor with shape [batch, p0, p1, target_channels]
	Returns:
		A float32 Tensor with shape [batch, p0, p1, body_input_depth]
```

*top
```
	Generate predictions/logits for one shard of output.

	Most classes will override this function.

	Args:
		body_output: A Tensor with shape [batch, p0, p1, body_output_depth]
		targets: A Tensor with shape [batch, p0, p1, targets_channels,
        top_dimensionality]
	Returns:
		A Tensor of class logits.
```

*loss
```
	Compute loss numerator and denominator for one shard of output
```