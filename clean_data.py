import pandas as pd
import os


# 1️⃣ Charger le fichier CSV généré précédemment
df = pd.read_csv("all_data_raw.csv", encoding="utf-8-sig")

# 2️⃣ Nettoyage des dates
date_cols = [
    "تاريخ النشر",
    "آخر أجل لإيداع الترشيحات",
    "تاريخ الإمتحان"
]

for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce").dt.date

print("📅 Dates nettoyées (sans heure)")

# Test : affichage des 5 premières lignes des colonnes de dates
print("\n👀 Aperçu des dates nettoyées :")
print(df[date_cols].head())


# 2️⃣ Remplir les valeurs manquantes
df["Corps"] = df["Corps"].fillna("Non spécifié")
df["Grade"] = df["Grade"].fillna("Non spécifié")
df['Nom du poste'] = df['Nom du poste'].fillna('Non spécifié')
df['عدد المناصب'] = df['عدد المناصب'].fillna(0).astype(int)

print("🧩 Valeurs manquantes corrigées")

# 📝 Test : afficher les 5 premières lignes des colonnes corrigées
print("\n👀 Aperçu des valeurs après remplissage :")
print(df[["Corps", "Grade"]].head(10))


# 3️⃣ Conversion عدد المناصب إلى int
df["عدد المناصب"] = (
    pd.to_numeric(df["عدد المناصب"], errors="coerce")
    .fillna(0)
    .astype(int)
)

print("🔢 عدد المناصب حُوّل إلى أعداد صحيحة")


# 4️⃣ Nettoyage des colonnes texte
text_cols = [
    "Administration",
    "Nom du poste",
    "Corps",
    "Grade",
    "Type_Source"
]

for col in text_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

print("🧼 Texte nettoyé (espaces supprimés)")

# Test : affichage des 
print("\n👀 Aperçu du texte nettoyé :")
print(df[text_cols].head())

# 5  Extraire l'année à partir de تاريخ النشر
df['Année'] = pd.to_datetime(df['تاريخ النشر'], errors='coerce').dt.year

# 📝 Test : afficher les 5 premières lignes avec l'année
print("\n📆 Aperçu avec la colonne Année :")
print(df[['تاريخ النشر', 'Année']].head())

# Sauvegarde finale
df.to_csv("all_data_clean.csv", index=False, encoding="utf-8-sig")

print("✅ Nettoyage final terminé")
print("📊 Dimensions finales :", df.shape)
