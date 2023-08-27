# imports and definitions
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from abstract_model import AbstractModel
import sys

#text = sys.argv[2]
class Model(AbstractModel):
    def __init__(self):
        self.model = self.model_definition()

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        #return self.model.predict(X_test)
        return self.model.predict(X_test)

    def predict_proba(self, X_test):
        #return self.model.predict(X_test)
        return self.model.predict_proba(X_test)

    def get_params(self):
        return self.model.get_params()


    def model_definition(self):
        mlp = MLPClassifier(hidden_layer_sizes=(8, 8, 8), activation='relu', solver='adam', max_iter=500)

        return mlp


if __name__ == "__main__":
    seed_number = 123

    # load the dataset to pandas
    filename = "cleaned_data.csv"
    df = pd.read_csv(filename, header=0)
    # get train/test splits
    features = df.iloc[:, 1:5]
    targets = df['species'].to_numpy()
    test_proportion = 0.3
    X_train, X_test, y_train, y_test = train_test_split(
        features,
        targets,
        test_size=test_proportion,
        stratify=targets,
        random_state=seed_number,
    )
    X_train_df = pd.DataFrame(X_train)
    X_test_df = pd.DataFrame(X_test)
    y_train_df = pd.DataFrame(y_train)
    y_test_df = pd.DataFrame(y_test)

    # Save each dataset to its respective CSV file
    X_train_df.to_csv('X_train.csv', index=False)
    X_test_df.to_csv('X_test.csv', index=False)
    y_train_df.to_csv('y_train.csv', index=False)
    y_test_df.to_csv('y_test.csv', index=False)
    # define the neural network
    from sklearn.neural_network import MLPClassifier

    mlp = MLPClassifier(hidden_layer_sizes=(8, 8, 8), activation='relu', solver='adam', max_iter=500)
    mlp.fit(X_train, y_train)

    predict_train = mlp.predict(X_train)
    predict_test = mlp.predict(X_test)

    from sklearn.metrics import classification_report, confusion_matrix

    with open("output2.txt", "a") as f:
        f.write('Result from neural network\n\nClassification Report\n\n{}\n\n'.format(
            classification_report(y_train, predict_train)))