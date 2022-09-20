
for short note,

<Bold><I> adding batch nomalization decreases the performance </I></Bold>

origin_url: https://stackoverflow.com/questions/57457817/adding-batch-normalization-decreases-the-performance


My interpretation of the phenomenon you are observing,, is that instead of reducing the covariance shift, which is what the Batch Normalization is meant for, you are increasing it. In other words, instead of decrease the distribution differences between train and test, you are increasing it and that's what it is causing you to have a bigger difference in the accuracies between train and test. Batch Normalization does not assure better performance always, but for some problems it doesn't work well. I have several ideas that could lead to an improvement:

+ Increase the batch size if it is small, what would help the mean and std calculated in the Batch Norm layers to be more robust estimates of the population parameters.
+ Decrease the bn_momentum parameter a bit, to see if that also stabilizes the Batch Norm parameters.
+ I am not sure you should set bn_momentum to zero when test, I think you should just call model.train() when you want to train and model.eval() when you want to use your trained model to perform inference.
+ You could alternatively try Layer Normalization instead of Batch Normalization, cause it does not require accumulating any statistic and usually works well

Try regularizing a bit your model using dropout
Make sure you shuffle your training set in every epoch. Not shuffling the data set may lead to correlated batches that make the statistics in batch normalization cycle. That may impact your generalization I hope any of these ideas work for you
