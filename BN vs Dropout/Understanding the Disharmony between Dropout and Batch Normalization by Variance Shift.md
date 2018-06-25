# Understanding the Disharmony between Dropout and Batch Normalization by Variance Shift

### Dropout

will shift the variance of a specific neural unit


### BN
maintain its statistical varaince, which is accumulated from the entir learning procedure


### Dropout before BN
the inconsistency of variance causes the unstable numerical behavior in inference that leads to more erroneous predictions.


### Suggested Methods

**Apply Dropout after all BN layers**


**Change Dropout into a more variance-stable form.**