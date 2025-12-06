import pandas as pd
import os 

csv_path='sales.csv'
if not os.path.exists(csv_path) :
    data = [
        {'date':'2025-12-01','product':'camisa','price':50,'quantity':2},
           
           {'date':'2025-12-01','product':'moletom','price':40,'quantity':3},
           {'date':'2025-12-01','product':'vestido','price':400,'quantity':6},
           {'date':'2025-12-01','product':'salto','price':80,'quantity':3},
           {'date':'2025-12-01','product':'tenis','price':230,'quantity':4},
           {'date':'2025-12-01','product':'bone','price':90,'quantity':8},
           {'date':'2025-12-01','product':'pulseira','price':800,'quantity':4},
           {'date':'2025-12-01','product':'calça jeans','price':80,'quantity':13},
           {'date':'2025-12-01','product':'jaqueta','price':110,'quantity':15}, 
           {'date':'2025-12-01','product':'meias','price':20,'quantity':4}, 
           {'date':'2025-12-01','product':'anel','price':5,'quantity':7}       
]
    df_example =  pd.DataFrame(data)
    df_example.to_csv(csv_path, index= False)
    print('uhul criou', csv_path)


df=pd.read_csv(csv_path,parse_dates=['date'])

required={'date','product','price','quantity'}
if not required.issubset(set(df.columns)):
    print('as colunas estao erradas')
    
df['total']=df['price']*df['quantity']
df[['total']].to_csv('total.csv',index=False)
print('Boa, Arquivo criado')