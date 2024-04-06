import pandas as pd
import matplotlib.pyplot as plt

def get_correlation(file):
    data = pd.read_csv(file)
    expected_scores = data['expected_score'].values
    predicted_scores = data['predicted_score'].values
    correlation = pd.Series(expected_scores).corr(pd.Series(predicted_scores))
    return correlation
 
correlation_values = []
for n in range(1,6):
    correlation = get_correlation('results/sick/results_{}.csv'.format(n))
    correlation_values.append(correlation)
    print('Correlation for n = {}: {}'.format(n, correlation))

plt.plot(range(1,6), correlation_values, marker='o')
plt.xlabel('n')
plt.ylabel('Correlation')
plt.title('Correlation vs n')
plt.show()