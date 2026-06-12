import pandas as pd
import random
from datetime import datetime, timedelta

# -----------------------
# CONFIGURAÇÃO
# -----------------------
NUM_USERS = 100
NUM_VIEWS = 500

genres = ["Sci-fi", "Comédia", "Documentário", "Terror"]

content_titles = {
    "Sci-fi": ["Nebula Wars", "Future Code", "AI Awakening", "Galaxy Drift"],
    "Comédia": ["Rindo Alto", "Vida Engraçada", "Amigos Caóticos", "Noite de Risadas"],
    "Documentário": ["Planeta Vivo", "Segredos do Oceano", "Mentes Geniais", "História do Mundo"],
    "Terror": ["Casa Sombria", "O Chamado", "Noite Sem Fim", "Sombras"]
}

# -----------------------
# USERS
# -----------------------
users = []
for i in range(1, NUM_USERS + 1):
    users.append({
        "user_id": i,
        "name": f"User_{i}",
        "age": random.randint(16, 60),
        "country": "Brazil"
    })

users_df = pd.DataFrame(users)

# -----------------------
# CONTENT
# -----------------------
content = []
content_id = 1

for genre in genres:
    for title in content_titles[genre]:
        content.append({
            "content_id": content_id,
            "title": title,
            "genre": genre
        })
        content_id += 1

content_df = pd.DataFrame(content)

# -----------------------
# WATCH HISTORY (EVENTOS)
# -----------------------
watch_history = []

start_date = datetime(2025, 1, 1)

for _ in range(NUM_VIEWS):
    user = random.randint(1, NUM_USERS)
    content_item = random.choice(content)

    watch_history.append({
        "user_id": user,
        "content_id": content_item["content_id"],
        "watch_time_minutes": random.randint(5, 120),
        "watched_at": (start_date + timedelta(days=random.randint(0, 180))).strftime("%Y-%m-%d")
    })

watch_df = pd.DataFrame(watch_history)

# -----------------------
# EXPORTAR CSVs
# -----------------------
users_df.to_csv("users.csv", index=False)
content_df.to_csv("content.csv", index=False)
watch_df.to_csv("watch_history.csv", index=False)

print("Dataset gerado com sucesso!")