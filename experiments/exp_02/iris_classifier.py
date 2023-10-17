# Import ML Libs
from micromlgen import port
from sklearn import metrics        
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# Main program
if __name__ == '__main__':

    # Load iris dataset:
    X, y = load_iris(return_X_y=True)
    print("\nShape of X:", X.shape, "\tSize of y:", len(y))
    print("\nX:", X)
    print("\ny:", y)
    
    # Splitting into train and test
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25)
    
    # Train a Random Forest Model
    model = RandomForestClassifier(n_estimators=10)
    model.fit(X_train, y_train)

    # --- Performance in Training ---
    training_prediction = model.predict(X_train)
    print(training_prediction)

    print("\nPrecision, Recall, Confusion matrix, in training\n")
    # Precision Recall scores
    print(metrics.classification_report(y_train, training_prediction, digits=3))
    # Confusion matrix
    print(metrics.confusion_matrix(y_train, training_prediction))
    # ------------------------------------

    # --- Performance in Test ---
    test_prediction = model.predict(X_test)
    print(test_prediction)

    print("\nPrecision, Recall, Confusion matrix, in testing\n")
    # Precision Recall scores
    print(metrics.classification_report(y_test, test_prediction, digits=3))
    # Confusion matrix
    print(metrics.confusion_matrix(y_test, test_prediction))
    # ------------------------------------


    # --- Test classification in randomic samples ---
    # Sample of a Setosa
    print('\nThe accuracy of model is:', model.predict([[5.1, 3.5, 1.4, 0.2]]))

    # Sample of a Versicolor
    print('The accuracy of model is:', model.predict([[6.2, 2.2, 4.5,1.5]]))

    # Sample of a Virginica
    print('The accuracy of model is', model.predict([[6.1, 3.0, 4.9,1.8]]))


    # --- Performance in Training ---
    c_code = port(model)
    with open('iris_classifier.h', 'w') as file:
        file.write(c_code)
    