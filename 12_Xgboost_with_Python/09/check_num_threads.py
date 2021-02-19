# Otto multi-core test
from time import time

from pandas import read_csv
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier

# load data
data = read_csv('train.csv')
dataset = data.values
# split data into X and y
X = dataset[:, 0:94]
y = dataset[:, 94]
# encode string class values as integers
label_encoded_y = LabelEncoder().fit_transform(y)
# evaluate the effect of the number of threads
results = []
num_threads = [1, 16, 32]
for n in num_threads:
    start = time()
    model = XGBClassifier(nthread=n)
    model.fit(X, label_encoded_y)
    elapsed = time() - start
    print(n, elapsed)
    results.append(elapsed)
