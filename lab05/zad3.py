import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=278820)

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

dtc = DecisionTreeClassifier()
dtc.fit(train_inputs, train_classes)
print(dtc.score(test_inputs, test_classes))

predictions = dtc.predict(test_inputs)
conf_matrix = confusion_matrix(test_classes, predictions)

print(conf_matrix)

# tak to drzewko jest lepsze niz zrobione ręcznie - dokładność wzrosła z 91% do 93%