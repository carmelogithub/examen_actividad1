import pandas as pd
import matplotlib.pyplot as plt
import pymongo

print('hola mundo')
conexion=pymongo.MongoClient("mongodb+srv://colaborador:colaboradorpassword@cluster0.lxijdu9.mongodb.net/")
print(conexion)
db = conexion['ejemplo']
col=db['productos']
data=list(col.find({"unidades":{"$gt":5}})) #select * from productos where unidades >5
print(data)
df=pd.DataFrame(data)
print(df)
plt.bar(df['nombre'],df['unidades'])
plt.title('Ventas de productos')
plt.xlabel('productos')
plt.ylabel('unidades')
plt.show()