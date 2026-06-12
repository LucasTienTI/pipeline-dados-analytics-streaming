import pandas as pd
from sqlalchemy import create_engine

# 1. Configuração da conexão com o banco de dados (Sua senha configurada)
# Formato: postgresql://usuario:senha@localhost:porta/nome_do_banco
DATABASE_URL = "postgresql://postgres:tchuco09@localhost:5432/netflix_db"

print("Conectando ao banco de dados PostgreSQL...")
engine = create_engine(DATABASE_URL)

# 2. Lendo os arquivos CSV que geramos antes
print("Carregando arquivos CSV...")
users_df = pd.read_csv("users.csv")
content_df = pd.read_csv("content.csv")
watch_df = pd.read_csv("watch_history.csv")

# 3. Enviando os dados para as tabelas do PostgreSQL de forma automática
print("Injetando dados na tabela 'users'...")
users_df.to_sql("users", engine, if_exists="append", index=False)

print("Injetando dados na tabela 'content'...")
content_df.to_sql("content", engine, if_exists="append", index=False)

print("Injetando dados na tabela 'watch_history'...")
watch_df.to_sql("watch_history", engine, if_exists="append", index=False)

print("🚀 Sucesso! Todos os dados foram carregados no PostgreSQL!")