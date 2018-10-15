# Convolution Types

---
### Vanilla Convolution

--
### Dilated Convolution

--
### Separable Convolution

--
### Deformable Convolution

--
### Deconvolution

--
### Design Criteria  
+ **extract saturate features**: they are generally stacked with an increasing number of filters in each layer(number of kernels). <u>*Each successive layer can have two to four times the number of filters in the previous layer*</u>. This helps the network learn hierarchical features.
+ **save computation cost**: decrease the size of the filters and increase the strides (like 1x1 convolutional filter)

### 1x1 Convolutional Filter

--
### Reference
[卷积方式大汇总](../../optimizer/CNN/CNN 中千奇百怪的卷积方式大汇总.md)