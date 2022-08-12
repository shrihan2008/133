import plotly.express as px
import plotly.express as px
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
rows = []
name=[]
import csv
f=pd.read_csv('total_stars.csv')
star_data=name[1:]
star_data_rows = rows[1:]
gravity=[]
mass=f['Mass'].to_list()
radius =f['Radius'].to_list()
star_name=[]
for i in star_data:
  mass.append(star_data[3])
  radius.append(star_data[4])
  name.append(star_data[1])

star_gravity=[]
low_gravity_stars=[]

for index,gravity in enumerate(star_gravity):
  if gravity<100:
    low_gravity_stars.append(star_data_rows[index])

print(len(low_gravity_stars))

star_type_values=[]
for i in star_data_rows:
  star_type_values.append(i[6])

print(list(set(star_type_values)))


star_mass=[]
star_radius=[]

for i in low_gravity_stars:
  star_mass.append(i[3])
  star_radius.append(i[7])

fig=px.scatter(x=star_radius,y=star_mass)
fig.show()


X=[]

for index,star_m in enumerate(star_mass):
  templist=[
      star_radius[index],
      star_mass[index]
  ]
  X.append(templist)

wcss=[]

for i in range(1,11):
  kmeans=KMeans(n_clusters=i,init='k-means++',random_state=48)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(range(1,11),wcss,marker='o',color="#583")
plt.title('ELBOW METHOD')

plt.xlabel('No.of clusters')
plt.ylabel('Wcss value')

plt.show()

