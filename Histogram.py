import pandas as pd
import matplotlib.pyplot as plt

url = 'https://course-resources.minerva.kgi.edu/uploaded_files/mke/rx9A0n/s1-student-version--ea-assignment--climate-change--land-ice-mass-data---sheet1.csv'

df = pd.read_csv(url)[10:]
df = df.reset_index(drop=True)
df.columns = ['TIME (year.decimal fraction)','Greenland mass (Gt)','Antarctica mass (Gt)']
v1 = list(df['Greenland mass (Gt)'].values.astype(float))

range = (-3000, 3000) 
bins = 10

plt.hist(v1, bins, range, color = 'green', histtype = 'bar', rwidth = 0.8)
plt.xlabel('Greenland mass (Gt)') 
plt.ylabel('Frequency')  
plt.title('LAND ICE MASS DATA detailing the anomalies relative to timeseries mean') 
plt.show()