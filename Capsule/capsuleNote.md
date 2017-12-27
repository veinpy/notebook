# Capsule
```
Author: Hinton
Abstract:
		Compared with CNN, which aims to improve classification accuracy, Capsule wants to represent knowledges (features) in different way which could contain more infomation about knowledges.
		In comapred with CNN or other structure, who represent features' existence by a seperate logistic unit (outputing probability), Capsules use the overall length of vector of instantiation parameters to represent the existence of the entity and to force the orientation of the vector to represent the properties of the entity(knowledge)
```
#### Characters:

`separating and identifying overlapping handwritten digits with accuracy far beyond existing neural netowrks.	`
	
details about CNN's shortage:
	![What is wrong with convolutional neural nets ?](https://www.youtube.com/watch?v=rTawFwUvnLE)

origin paper:
	![Dynamic Routing Between Capsules]([nips2017]1710.09829v1_Dynamic Routing between Capsules.pdf)

good illustration:
	![Understanding Hinton’s Capsule Networks(I)](Understanding Hinton’s Capsule Networks(I).pdf)
	![Understanding Hinton’s Capsule Networks(II)](Understanding Hinton’s Capsule Networks(II).pdf)
```
Algorithm Details:

***
	
```

Advance Thought
	![Hinton++ – Towards Data Science](Hinton++ – Towards Data Science.pdf)

```
Capsules are an attempt to overcoome geometric changes.
But it cannot solve such phenomenon:
	"It's a face, but the eyes are sideways, and the mouth is upside-down." because the eyes or the mouth are not lighting up, so the agreement cannot be realized. It does not have inference ("it should be, something, and which part is not as what I thought")
	Out brains seem to project the 'face expectation' back down to the lower layers, asking, 'if this were a normal face, what would the normal poses be for the moth, nose, and eyes?'
	The face's compression generates an expectation of pose for its parts!
```