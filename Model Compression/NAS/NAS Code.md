# NAS Code

## Search Space

**Micro Structure**
micro_space主要指cell里的operation:   
```python

MICRO_OP_SPACE: ['none', 'skip_connect', 'nor_conv_k*k', 'avg_pool_k*k', 'max_pool_k*k', 'dua_spec_k*k', 'dil_spec_k*k']

# reference: AutoDL-Project/xautodl/models/cell_operations.py
```

**Macro Structure**  

hand-crafted structure,

Input_Data -> **stem** -> [cells] -> **lastact**

```python
## [cells]
## reduction时，使用 ResNetBasicblock()
## 其他情况时，  使用 SearchCell()
layer_channels = [C] * N + [C * 2] + [C * 2] * N + [C * 4] + [C * 4] * N
layer_reductions = [False] * N + [True] + [False] * N + [True] + [False] * N

stem = nn.Sequential(
            nn.Conv2d(3, C, kernel_size=3, padding=1, bias=False), nn.BatchNorm2d(C)
        )

lastact = nn.Sequential(
    nn.BatchNorm2d(
        C_prev, affine=affine, track_running_stats=track_running_stats
    ),
    nn.ReLU(inplace=True),
)
        
```

## Optimization

**Weight Optimization**
```
optimizer:  SGD | RMSprop

scheduler:  CosineAnnealingLR | MultiStepLR | ExponentialLR | LinearLR

criterion:  CrossEntropyLoss  | CrossEntropyLabelSmooth 
```

**Alpha(Cell_Structure) Optimization**
```
Adam(alpha_parameters,
        lr=xargs.arch_learning_rate,
        betas=(0.5, 0.999),
        weight_decay=xargs.arch_weight_decay,)
```


## Benchmark Monitor

```
reference: AutoDL-Project/xautodl/utils/flop_benchmark.py
```

## Training Protocal
```
for epoch in range(start_epoch, total_epoch):
    w_scheduler.update(epoch, 0.0)
    
backward_step_unrolled
```
