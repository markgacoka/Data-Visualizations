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
