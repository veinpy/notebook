### meta
1. no longer tied to MF model.
2. take advantage of dnn
3. transfer learning across users (by means of shared parameters), enabling us to cope with limited amount of data per user.

linear weight adaptation.
non-llinear bias adaptation.


### key idea
item representation (via DNN), each one can be represented by a vector.
limited time's user-item history : (tm, emj), where emj is whether item(tm) be engaged , emj = {0,1}, tm is the item for user.

R0: aggregate the history which match emj=0, calculate the aggregated vector of list of items' vector. (calculate mean is only the basic method)
R1: aggregate the history which match emj=1, calculate the aggregated vector of list of items' vector. (calculate mean is only the basic method)

the item needs to be predicted: ti, also be represented by a vector.


##### Linear Classifier
w0*R0 + w1*R1 : represent the user.
ti's vector represent item.

w0 and w1 are adapted per user., b came across all users

sigmoid(item * user + bias) => the probolity of the ti will be engaged.


##### Non-linear:
	
output=>	bias: v0*R0 + v1*R1, v0 and v1 (vector) are adapted per user.
output=>	w: weights of output, parameter(vector) came across all user
hidden=>	bias: V0*R0 + V1*R1 , parameter(matrix) came across all user
hidden=>	W: weight, parameter(matrix) came across all user