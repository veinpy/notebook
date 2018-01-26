#### Spatial Transformer Networks
Spatial Transformer Network（STN）是 DeepMind 提出的一个全新的网络模块，能够显示地学习到网路对输入的旋转、平移、缩放等等变换的不变性（invariance）
STN 模块本身可微，可以无缝嵌入现有网络架构，且无需额外的监督信息帮助训练。STN 网络可以视为一种崭新的 Attention 机制，对于 OCR、Weakly-supervised Learning、Co-Localization 等领域和任务均有巨大的应用价值。
[paper](./5854-spatial-transformer-networks.pdf)

[github_simple](https://github.com/zsdonghao/Spatial-Transformer-Nets)

[github_complex](https://github.com/kevinzakka/spatial-transformer-network)


#### 应用

###### Recurrent Spatial Transformer Networks
在 RNN 中结合 Spatial Transformer Networks（STN）进行 OCR 整行文本识别，是一种更加先进的 Attention 机制。

###### A DNN Framework For Text Image Rectification From Planar Transformations
矫正文档图像的透视变换和旋转变换，利用 Spatial Transformer Networks（STN）使得不同矫正阶段能够 end-to-end 地串联起来。

###### STN-OCR: A single Neural Network for Text Detection and Text Recognition
借助 Spatial Transformer Networks，用一个网络，end-to-end 同时实现文本检测和文本识别。

###### Robust Scene Text Recognition with Automatic Rectification
使用 STN 在 OCR 中对扭曲文本进行校正，提高了 OCR 识别的效果。
