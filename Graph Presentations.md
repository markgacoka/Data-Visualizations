

```python
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://course-resources.minerva.kgi.edu/uploaded_files/mke/rx9A0n/s1-student-version--ea-assignment--climate-change--land-ice-mass-data---sheet1.csv'

df = pd.read_csv(url)[10:]
df = df.reset_index(drop=True)
df.columns = ['TIME (year.decimal fraction)','Greenland mass (Gt)','Antarctica mass (Gt)']
v1 = list(df['TIME (year.decimal fraction)'].values.astype(float))
v2 = list(df['Greenland mass (Gt)'].values.astype(float))
v3 = list(df['Antarctica mass (Gt)'].values.astype(float))

plt.plot(v1, v2, label = "Greenland mass over time")
plt.plot(v1, v3, label = "Antarctica mass over time")
plt.xlabel('Time in years') 
plt.ylabel('Mass in (Gt)')
plt.grid(True)
plt.figtext(.1, -.3, "Figure 1: Annual land ice mass anomalies from the time series mean for Greenland and Antarctic Ice Sheets.\n\
The lines indicate annual Greenland mass(Gt) anomalies and Antarctica mass(Gt) anomalies respectively over\na period of 12 years for\
the time series mean. The graph shows a gradually decreasing positive anomaly in a \ncyclic pattern for both areas over time. The\
two anomalies intersect around ~0 where Greenland has a faster\ndecrease towards a more negative anomaly. This indicates that there\
is a gradual decrease in mass(Gt) having\ndecreased by an anomaly of ~3500Gt from the average in the course of 12 years presented for\
both Greenland\nand Antarctica.")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()
#plt.savefig('line_graph.png')
```


![png](output_0_0.png)



```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'https://course-resources.minerva.kgi.edu/uploaded_files/mke/rx9A0n/s1-student-version--ea-assignment--climate-change--land-ice-mass-data---sheet1.csv'

df = pd.read_csv(url)[10:]
df = df.reset_index(drop=True)
df.columns = ['TIME (year.decimal fraction)','Greenland mass (Gt)','Antarctica mass (Gt)']
v1 = list(df['TIME (year.decimal fraction)'].values.astype(float))
v2 = list(df['Greenland mass (Gt)'].values.astype(float))
v3 = list(df['Antarctica mass (Gt)'].values.astype(float))

plt.scatter(v1, v2, label = "Greenland mass (Gt) against Time in years", color='red')
plt.plot(np.unique(v1), np.poly1d(np.polyfit(v1, v2, 1))(np.unique(v1)), label="Best fit line")

plt.xlabel('Time in years') 
plt.ylabel('Greenland mass (Gt)')  
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.figtext(.1, -.3, "Figure 2: Annual land ice mass anomalies from the time series mean for Greenland.\n\
The scatter plot shows the relationship between the Greenland mass(Gt) anomalies\nfrom the mean against the \
time series in years. The best fit line suggests that there\nhas been a positive anomaly from the time series \
mean until 2008 where a negative\nanomaly occured until 2014. This implies that there has been a gradual decrease \n\
in Greenland mass with increase in mass.")
plt.show()
#plt.savefig('scatter_plot.png')
```


![png](output_1_0.png)



```python
import pandas as pd
import numpy
import matplotlib.pyplot as plt

url = 'https://course-resources.minerva.kgi.edu/uploaded_files/mke/rx9A0n/s1-student-version--ea-assignment--climate-change--land-ice-mass-data---sheet1.csv'

df = pd.read_csv(url)[10:]
df = df.reset_index(drop=True)
df.columns = ['TIME (year.decimal fraction)','Greenland mass (Gt)','Antarctica mass (Gt)']
v1 = list(df['Greenland mass (Gt)'].values.astype(float))

range = (-2200, 2000) 
bins = 15

plt.hist(v1, bins, range, color = 'green', histtype = 'bar', rwidth = 0.8)
plt.xlabel('Greenland mass (Gt)') 
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.30)
plt.axvline(numpy.mean(v1), color="blue", linewidth=1.5,label='Mean: {:f}'.format(numpy.mean(v1)))
plt.legend(loc=0)
plt.figtext(.1, -.2, "Figure 3: Frequency of annual land ice mass anomalies from the time series mean for Greenland from 2002 to 2014.\n\
The distribution is more left skewed having a greater distribution towards the ~1000Gt mark. This implies that the\ndispersion in data\
was more towards the positive anomaly for the time period until it reached the ~0 mark where it took\na shorter time for the anomaly to\
decrease towards a negative anomaly. This indicates a rapid decrease in Greenland mass(Gt)\nespecially after transitioning to the negative\
anomaly in 2009")
plt.show()
#plt.savefig('histogram.png')
```


![png](output_2_0.png)

