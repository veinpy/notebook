# Coarse-to-Fine Question Answering for Long Documents


For a document, the answer selection contains (from coarse to fine):

+ skim the document, identify relevant parts
+ carefully read these parts to produce an answer


### method
**selection sentence as a variable latent variable trained jointly from the answer only using reinforcement learning.**

hierarchical approach where 

+ a fast model to select a few sentences from the document that are relevant for answering the question
+ a slow RNN is employed to produce the final answer from the selected sentences.

slow rnn runs over a fixed number of tokens regarless of teh length of the document.