# encoding=utf-8

"""
swiss roll data with noise
    mainly used for manifold learning problem

basic manifold learning tutorial:
    https://github.com/jeenalee/swissroll_manifold_learning/blob/master/swissroll_manifold_learning.ipynb
"""

from sklearn import manifold, datasets, decomposition, ensemble, discriminant_analysis, random_projection
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n_points = 1000
noise = 0.5
X, color = datasets.samples_generator.make_swiss_roll(n_points, noise)

"""
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(251, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color)
plt.title("Original Swiss Roll")
plt.show()
"""
