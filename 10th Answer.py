import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
x = np.array([[1, 0], [2, 0], [3, 0], [6, 0], [6, 0], [7, 0], [10,0], [11, 0]])
y = np.array([0, 0, 1, 1, 1, 0, 0, 0])
x_train, x_test, y_train, y_test, = train_test_split(x, y, test_size=0.5, random_state=0, shuffle=False )
print(x_train)
print(y_train)
neighbor = KNeighborsClassifier(n_neighbors=3)
neighbor.fit(x_train, y_train)
y_pred = neighbor.pedict(x_test)
y_pred

