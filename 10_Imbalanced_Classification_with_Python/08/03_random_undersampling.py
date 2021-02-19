# example of random undersampling to balance the class distribution
from collections import Counter

from imblearn.under_sampling import RandomUnderSampler
from sklearn.datasets import make_classification

# define dataset
X, y = make_classification(n_samples=10000, weights=[0.99], flip_y=0)
# summarize class distribution
print(Counter(y))
# define undersample strategy
undersample = RandomUnderSampler(sampling_strategy='majority')
# fit and apply the transform
X_over, y_over = undersample.fit_resample(X, y)
# summarize class distribution
print(Counter(y_over))
