import pandas
import numpy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Loading input data
file = pandas.read_json('/Users/jingjing/Documents/Python_file/projects/knn/rew_data.json')
all_data = pandas.DataFrame(file).to_numpy().T

# Extract and clean dependent variables
org_y = all_data[0]
y = []
for i in range(0, len(org_y)):
    for j in range(0, len(org_y[0])):
        each = org_y[i][j]
        each = int(each.replace(',', '').replace('$', '').replace('\n', ''))
        y = numpy.append(y, each)
y = y.reshape(-1, 1)

# Extract and clean independent variables
org_x = all_data[1]
x = []
for i in range(0, len(org_x)):
    for j in range(0, len(org_x[0])):
        each = org_x[i][j]
        if 'x' in each:
            each = each.replace('ft', '')
            each = each.split('x')
            each = int(each[0]) * int(each[1])
        elif '-' in each:
            each = each.replace('sf', '')
            each = each.split('-')
            each = (int(each[0]) + int(each[1]))/2
        elif '<' in each:
            each = int(each.replace('<', '').replace('sf', ''))
        x = numpy.append(x, each)
x = x.reshape(-1, 1)

# Splitting the dataset into the Training and Test set
x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Feature Scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

# Loading KNN model
classifier = KNeighborsClassifier(n_neighbors=10, p=2, metric='euclidean')

# Fitting model
classifier.fit(x_train, y_train.ravel())

# Predicting the test set
y_pred = classifier.predict(x_test)

# Evaluating model
conf_matrix = confusion_matrix(y_test, y_pred)
#print(conf_matrix)

# Getting accuracy score
print(accuracy_score(y_test, y_pred))
