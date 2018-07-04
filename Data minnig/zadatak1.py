import pandas as pd

narudzbine = pd.read_csv("C:\\Users\\Priboj\\Desktop\\pajton\\petnica 2018\\instacart_2017_05_01\\orders.csv")
proizvodi = pd.read_csv("C:\\Users\\Priboj\\Desktop\\pajton\\petnica 2018\\instacart_2017_05_01\\products.csv")

print("Narudzbina ima: ",narudzbine.count()['order_id'])
print("Proizvoda ima: ",proizvodi.count()['product_id'])
print("Korisnika ima: ",narudzbine['user_id'].drop_duplicates().count())
