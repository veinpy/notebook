# Neural Word Segmentation Learning for Chinese

[paper](https://arxiv.org/pdf/1606.04300v2.pdf)

---

## word score

![word emb](./word emb.png)

```
包含reset gate 和 update gate

reset gate: 候选词中每个字符相互相关，依据相关系数矩阵，产出attention，后续作用于字符本身，计算出w_hat

update gate: w_hat与候选词中每个字符，via系数矩阵，产出attention(sum=1)

```
+ **r** reset gate,  *dep:* **R × c**
+ **z** upate gate,  *dep:* **U × [w,c]**

<img src="./w.png" width="400"/>
--
<img src="./w_hat.png" width="400"/>
--
<img src="./r.png" width="400"/>

--
<img src="./z.png" width="400"/>

<img src="./z_norm.png" width="250"/>

## link score

## sentence score

## loss function
