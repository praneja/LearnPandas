import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import pandas as pd
import numpy as np
from pandas.plotting import register_matplotlib_converters

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',
   periods=10), columns=list('ABCD'))
arr = np.arange(df.size)
#df.plot()

print(df)
register_matplotlib_converters()
#plt.plot(df)
plt.ylabel('some numbers')
#plt.show()
#df.plot.bar(x="numbers",y="values",rot = 0)

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()