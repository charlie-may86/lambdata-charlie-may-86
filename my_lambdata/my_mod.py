# my_lambdata/my_mod.py
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from pdb import set_trace as breakpoint
import pandas as pd


def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100


def train_validation_test_split(X, y, train_size=0.7, val_size=0.1,
                                test_size=0.2, random_state=None,
                                shuffle=True):

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)

    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=val_size/(train_size+val_size),
        random_state=random_state, shuffle=shuffle)

    return X_train, X_val, X_test, y_train, y_val, y_test

if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    # print("HELLO")
    # y = int(input("Please choose a number"))
    # print(y, enlarge(y))

    raw_data = load_wine()
    df = pd.DataFrame(data=raw_data['data'], columns=raw_data['feature_names'])
    df['target'] = raw_data['target']
    print(df.shape)

    # breakpoint()