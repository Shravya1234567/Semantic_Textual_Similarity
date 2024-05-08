import torch
import numpy as np
import pandas as pd
from cnn_utils import preprocess, load_data
import sys

def main(data):

    _,_,_,_,_,_,X1_test, X2_test, y_test = load_data(data)

    if data == 'sts':
        test_data = pd.read_csv('../../data/sts/test.csv')
        senteces_A = test_data['sentence1'].values
        sentences_B = test_data['sentence2'].values
        labels = test_data['similarity'].values
    elif data == 'sick':
        test_data = pd.read_csv('../../data/sick/test.csv')
        senteces_A = test_data['sentence_A'].values
        sentences_B = test_data['sentence_B'].values
        labels = test_data['normalised_score'].values

    model = torch.load(f'models/model_{data}.pt')

    model.eval()

    with torch.no_grad():
        y_pred = model(X1_test, X2_test)
        y_pred = y_pred.numpy()
        y_pred = np.squeeze(y_pred)
        y_pred = np.clip(y_pred, 0, 5)
        results = pd.DataFrame({'sentence1': senteces_A, 'sentence2': sentences_B, 'similarity': labels, 'predicted_similarity': y_pred})
        results.to_csv(f'results/results_cnn_{data}.csv', index=False)
        print(f'Predictions saved in results_cnn_{data}.csv')

    correlation = pd.Series(labels).corr(pd.Series(y_pred))
    print('Correlation between expected and predicted similarity scores:', correlation)


if __name__ == '__main__':
    data = sys.argv[1]
    main(data)