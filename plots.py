import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

# Single series: 1000 N(0,1) numbers (with an index of days)
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
# ts.plot()
# plt.show()

# 4 series
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
# plt.figure();  # This creates a new figure
# df.plot()  # plot to the figure
# plt.show()  # show the figure

# Plot one series against another
df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
df3['A'] = pd.Series(list(range(len(df))))
# df3.plot(x='A', y='B')
# plt.show()

# Other plot types
df.ix[5].plot(kind='bar')  # get 5th row as a Series, and plot it as a bar chart
plt.axhline(0, color='k')  # block colour for the x=0 line
plt.show()
