# relational inductive biases within deep learning architectures

blending powerful deep learning approaches with structured representations

graph networks support relational reasoning and combinatorial generalization

representing structure and reasoning about relations.

---
**relational.inductive biasq**

+ **entity**
+ element with attributes 
+ **relation**
+ property between entities
+ **rule** 
+ funtion that maps entities and relations to other entities and relations (*unary and binary -> uniary*)
+ rule(arg1) -> result1, rule(arg1, arg2) -> result1

all of the building blocks in deep learning can be *regarded as a particular type of relational inductive bias* -- in whcih computations are performed in stages, typically resulting increasingly longrange interactions among information in the input signal

--
show **Table 1**

---

**this paper's proposition**

present a general framework (**graph networks**) for entity- and relation-based reasoning -- which we term *graph networks* -- for unifying and extending existing methods which operate on graphs, and describe key design principles for building powerful architectures using **graph networks as building blocks.**

---

**permutation inveriance** 
输入的ordering不影响结果 
而MLP需要固定的input order.

**pairwise interactions**

**Graphs** are a representation which supports arbitrary (pairwise) relational structure, and computations over graphs afford a strong relational inductive bias beyond that which cnn and rnn can provide.

---

### Graph Networks

the **GN framework's block organization** emphasizes customizability and synthesizing new architectures which express desired relational inductive biases.

+ main unit: GN block
+ graph-to-graph module, input graph, output graph.

#### key principles:
+ Flexible representations
+ Configurable within-block structure
+ Composable multi-block architectures

### Graph definition

3-tuple G = (**u**, V, E)
+ u: global attributes
+ V: vertics (nodes)
+ E: edges
+ E = {(e\_k, r\_k, s\_k)} , e\_k is edge attributes, r\_k is receiver\_index, s\_k is sender\_index

### Architecture

+ Composition of GN blocks (linear)
+ encode-process-decode
+ recurrent GN-based architectures

**covariant compositional networks**

### Limitations
+ cannot be guaranteed to solve some classes of problems 
+ like: discriminating between certain non-isomorphic graphs
+ cannot be straight forward to represent notions like: recursion, control flow, conditional iteration

### Need improvement

+ modify graphs: add/remove edges
+ structure extraction
+