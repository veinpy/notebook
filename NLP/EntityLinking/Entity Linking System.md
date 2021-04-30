# Entity Linking System

### Task One
+ 1. Mention Detection (MD)
+ 2. Named Entity Recognition (NER)

### Task Two
+ 1. Entity Disambiguation (ED)
	+ ```linke these spans to corresponding entities in a KB```


----
<>  
First generates all possible spans (mentions) that have at least one possible entity candidates.   
Then, each mention - candidate pair receives a context-aware compatibility score based on word and entity embedding coupled with a neural attention an a global voting mechanisms