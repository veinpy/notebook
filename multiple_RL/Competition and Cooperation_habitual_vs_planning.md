competition and cooperation
habitual and goal-directed(planning)

没看完，有点长。。。

<mark>cost-benefit tradeoff</mark>

habitual <=> model-free 
goal-directed <=> model-based

```
model-free strategy is a form of Thorndike's Law of Effect, which states that actions that led to a reward become more likely to be repeated.
but its inflexibility: when environment changed.
So it's habitual
```

```
model-based strategy, represents its knowledge in the form of an internal model that can be modified locally when changes occur.
it, unlike the model-free strategy, need not cache values.
it inevitably more time and resource intensive than querying a look-up table of cached values or function approximator
```

1. Shenhav,
Botvinick, and Cohen (2013) have proposed that the brain computes an ‘expected value of
control’ for each action—the expected rewarded discounted by the cost of associated
control demands—and then chooses the action with highest value

2. metacontrol between different systems is determined by the ‘value of computation’, the
expected reward for a given action subtracted by the costs of computation and time