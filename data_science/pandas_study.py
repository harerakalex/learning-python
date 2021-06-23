import pandas as pd
import numpy as np

numbers = pd.Series(np.random.randint(0, 1000, 10000))
# This way is not effective enough so this can be removed
for label, value in numbers.iteritems():
    numbers.loc[label] = value+2

# Alternative and simple way to do the above we should use

numbers+=2
print(numbers.head())