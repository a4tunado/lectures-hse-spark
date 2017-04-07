import numpy as np
from sklearn.datasets import make_classification


X, _ = make_classification(n_features=2, n_classes=3, 
                           n_redundant=0, n_informative=2,
                           random_state=1, n_clusters_per_class=1)

rng = np.random.RandomState(2)
X += 2 * rng.uniform(size=X.shape)

for v in X:
    print ','.join(map(str, list(v)))

