import argparse
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('Path', type=str, help='csv file with patient data')
    args = parser.parse_args()
    input_path = args.Path
    
    brcaBucket = pd.read_csv(input_path)
    
    cols = list(brcaBucket.columns)
    cols.remove('is_tumorous')
    cols.remove('tumor_type')
    cols.remove('patient_ID')
    cols.remove('data_source')
    cols.remove('__no_feature')
    cols.remove('__ambiguous')
    cols.remove('__alignment_not_unique')

    X = brcaBucket[cols].astype('int32')
    Y = brcaBucket['is_tumorous']
    seed = 7
    test_size = 0.33
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
    model = XGBClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    predictions = [round(value) for value in y_pred]
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    
if __name__ == '__main__':
    main()
