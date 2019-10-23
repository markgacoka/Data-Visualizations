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
