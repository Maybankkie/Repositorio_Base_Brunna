# importar a sqlite
# não precisa instalar

import sqlite3

# Passo 2
#         - Criar conexão com o banco de dados
#         - Na primeira execução sera criado o banco
conexao = sqlite3.connect('agencia2.db', timeout=20)

# Passo 3 
#        - Criar um cursor 
#        - Serve para executar scrips SQL dentro do banco
cursor = conexao.cursor()

print('conexão criada com sucesso')

cursor.execute('''
               
   CREATE TABLE IF NOT EXISTS motos (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        cc INTEGER NOT NULL,
        ano INTEGER NOT NULL,
        valor DECIMAL NOT NULL
    )            
                  

                ''')


#cursor.execute("INSERT INTO motos('marca','modelo','cc','ano','valor') VALUES (?,?,?,?,?)",('Honda','shadow',650,2004,13500))
#cursor.execute("INSERT INTO motos('marca','modelo','cc','ano','valor') VALUES (?,?,?,?,?)",('Royal Enfield','Hunter',350,2025,19900))
#cursor.execute("INSERT INTO motos('marca','modelo','cc','ano','valor') VALUES (?,?,?,?,?)",('Royal Enfield','Shotgun',650,2025,31500))
#cursor.execute("INSERT INTO motos('marca','modelo','cc','ano','valor') VALUES (?,?,?,?,?)",('BMW','GS 800F',800,2015,39500))
#cursor.execute("INSERT INTO motos('marca','modelo','cc','ano','valor') VALUES (?,?,?,?,?)",('Harley Davidson','Heritage',1600,2016,77000))
#cursor.execute("INSERT INTO motos('marca','modelo','cc','ano','valor') VALUES (?,?,?,?,?)",('Harley Davidson','Fat Boy',1600,2014,67500))
#conexao.commit()




consulta = cursor.execute("SELECT * FROM motos")

for lista in consulta.fetchall():
    print(f'Marca: {lista[1]} - modelo: {lista[2]} - Cilindrada: {lista[3]} - Ano: {lista[4]} - Valor: {lista[5]}')

print('n_____________________________________________________________')



consulta2 = cursor.execute("SELECT marca, cc FROM motos")
print('Marcas e cilindradas:\n')
for lista3 in consulta2.fetchall():
    print(f'          {lista3[0]} - {lista3[1]}')


# U - UPDATE

cursor.execute("UPDATE motos SET cc = ? WHERE id = ?", (1300,5))
conexao.commit()



# D - DELETE

