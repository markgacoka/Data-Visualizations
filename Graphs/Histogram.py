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
