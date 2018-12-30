# Learning to Compose Neural Networks for Question Answering

## Data 
(world, question, answer)

## Structure
```trained jointly```

1. a collection of neural "modules" that can be freely composed 
2. a network layout predictor that assembles modules into complete deep networks 

## Neural Modules
basic network module that execute some calculations to perform function, including: 
1. Lookup
2. Find
3. Relate
4. And
5. Describe
6. Exists

<mark> 该paper的module是人工定义的，是否能够做到拓展性？

### Mapping query into neural compositions 
(parse the query into parse-tree)

1. Represent the input sentence as a dependency tree.
2. Collect all nouns, verbs and prepositional phrases and associate each of these with a layout fragment: Ordinary nouns and verbs are mapped to a single **find** module. `Proper nouns` to a single **lookup** module. 
3. `Prepositional phrases` are mapped to a depth-2 fragment, with a relate module for the preposition above a find module for the enclosed head noun. 
4. Form subsets of this set of layout fragments. For each subset, construct a layout candidate by joining all fragments with an **and** module, and inserting either a **measure** or **describe** module at the top (each subset thus results in two parse candidates.)

## Training