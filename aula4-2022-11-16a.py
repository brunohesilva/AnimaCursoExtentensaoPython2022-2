import sqlite3

conexao = sqlite3.connect("dc_universe.db")

cursor = conexao.cursor()

sql = "SELECT pessoa_id, nome, nome_civil, tipo from pessoas"

cursor.execute(sql)

pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  printf(f"Nome: {pessoa[1]} ({pessoa[3]})")