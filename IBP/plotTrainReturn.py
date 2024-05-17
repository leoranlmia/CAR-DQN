# # import libraries
# import numpy as np
# import scipy.stats
# import matplotlib.pyplot as plt
#
# # create data sets with 45 values each
# seed1 = np.random.normal(1.5, 0.2, 45)
# seed2 = np.random.normal(2.0, 0.3, 45)
# seed3 = np.random.normal(2.5, 0.4, 45)
# seed4 = np.random.normal(3.0, 0.5, 45)
# seed5 = np.random.normal(3.5, 0.6, 45)
#
# # stack data sets into a 2D array
# data = np.stack([seed1, seed2, seed3, seed4, seed5])
#
# # calculate mean and SEM along the columns
# mean = np.mean(data, axis=0)
# sem = scipy.stats.sem(data, axis=0)
#
# # create figure and axis
# fig, ax = plt.subplots()
#
# # plot mean and SEM
# ax.plot(mean, label='mean')
# ax.fill_between(np.arange(len(mean)), mean-sem, mean+sem, alpha=0.5, label='SEM')
#
# # add labels, legends, titles, etc.
# ax.set_xlabel('Value')
# ax.set_ylabel('Value')
# ax.set_xticks(np.linspace(1, 4, 9))
# ax.legend()
# ax.set_title('Mean and SEM of five seeds with 45 data points each')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

seed1 = np.random.normal(1.5, 0.2, 45)
seed2 = np.random.normal(2.0, 0.3, 45)
seed3 = np.random.normal(2.5, 0.4, 45)
seed4 = np.random.normal(3.0, 0.5, 45)
seed5 = np.random.normal(3.5, 0.6, 45)

data = np.concatenate((seed1, seed2, seed3, seed4, seed5))
episode = np.concatenate((np.arange(45), np.arange(45), np.arange(45), np.arange(45), np.arange(45)))
sns.lineplot(x=episode, y=data)
plt.xlabel('Episode')
plt.ylabel('Return')
plt.show()
