import pandas as pd
import matplotlib.pyplot as plt

url = 'https://course-resources.minerva.kgi.edu/uploaded_files/mke/rx9A0n/s1-student-version--ea-assignment--climate-change--land-ice-mass-data---sheet1.csv'

df = pd.read_csv(url)[10:]
df = df.reset_index(drop=True)
df.columns = ['TIME (year.decimal fraction)','Greenland mass (Gt)','Antarctica mass (Gt)']
v1 = list(df['Greenland mass (Gt)'].values.astype(float))
v2 = list(df['Antarctica mass (Gt)'].values.astype(float))

plt.scatter(v1, v2, label = "Greenland mass (Gt) against Antarctica mass (Gt)")
plt.xlabel('Greenland mass (Gt)') 
plt.ylabel('Antarctica mass (Gt)')  
plt.title('Scatter plot') 
plt.legend(loc='upper left')
plt.show()