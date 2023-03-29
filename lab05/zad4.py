import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier


df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=278820)

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

# 5NN

knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn.fit(train_inputs, train_classes)

predictions = knn.predict(test_inputs)

conf_matrix = confusion_matrix(test_classes, predictions)

print("k = 5:")
print(knn.score(test_inputs, test_classes))
print(conf_matrix)

# 3NN

knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
knn.fit(train_inputs, train_classes)

predictions = knn.predict(test_inputs)

conf_matrix = confusion_matrix(test_classes, predictions)

print("k = 3:")
print(knn.score(test_inputs, test_classes))
print(conf_matrix)

# 11NN

knn = KNeighborsClassifier(n_neighbors=11, metric='euclidean')
knn.fit(train_inputs, train_classes)

predictions = knn.predict(test_inputs)

conf_matrix = confusion_matrix(test_classes, predictions)

print("k = 11:")
print(knn.score(test_inputs, test_classes))
print(conf_matrix)

# DD - mniej dokladne - zamiast 97% jest 93%

dt = DecisionTreeClassifier(random_state=42)
dt.fit(train_inputs, train_classes)

predictions = dt.predict(test_inputs)

conf_matrix = confusion_matrix(test_classes, predictions)

print("Decision Tree:")
print(dt.score(test_inputs, test_classes))
print(conf_matrix)

# NB - tez mniej dokladne - 93%

nb = GaussianNB()
nb.fit(train_inputs, train_classes)

predictions = nb.predict(test_inputs)

conf_matrix = confusion_matrix(test_classes, predictions)

print("Naive Bayes:")
print(nb.score(test_inputs, test_classes))
print(conf_matrix)

# Podsumowując najdokładniejsze są klasyfikatory k-NN