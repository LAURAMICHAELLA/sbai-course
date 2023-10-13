from micromlgen import port
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris


if __name__ == '__main__':
    X, y = load_iris(return_X_y=True)
    clf = RandomForestClassifier(n_estimators=10).fit(X, y)
    c_code = port(clf)

    with open('classifier.h', 'w') as file:
        file.write(c_code)