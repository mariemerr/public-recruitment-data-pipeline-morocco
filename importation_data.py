import pandas as pd
import os
# 1️⃣ Chemin du dossier contenant les fichiers Excel
BASE_DIR = r"C:\Users\meriem\Desktop\data"

# 2️⃣ Noms des fichiers Excel (sans espaces dans les noms)
files = {
    'etat': os.path.join(BASE_DIR, 'concours_service_etat.xlsx'),
    'collectivites': os.path.join(BASE_DIR, 'concours_collectivites.xlsx'),
    'etablissements': os.path.join(BASE_DIR, 'concours_etablissements.xlsx'),
    'experts': os.path.join(BASE_DIR, 'experts.xlsx')
}

# 3️⃣ Lecture des fichiers Excel
dataframes = {}

for key, file_path in files.items():
    try:
        df = pd.read_excel(file_path, engine="openpyxl")
        dataframes[key] = df
        print(f"✅ Fichier '{key}' chargé avec succès")
        print(f"📌 Colonnes : {df.columns.tolist()}")
        print(f"📊 Taille : {df.shape}\n")
    except Exception as e:
        print(f"❌ Erreur sur '{key}' : {e}\n")

# 4️⃣ Création des DataFrames finaux (uniquement si le chargement a réussi)
if 'etat' in dataframes:
    df_etat = dataframes['etat']

if 'collectivites' in dataframes:
    df_coll = dataframes['collectivites']

if 'etablissements' in dataframes:
    df_etab = dataframes['etablissements']

if 'experts' in dataframes:
    df_exp = dataframes['experts']

print("🎯 Importation terminée avec succès.")


#....................................................#
# 1️⃣ إضافة عمود المصدر (باش نحافظو على الهوية ديال كل سطر)
df_etat['Type_Source'] = 'Ministère'
df_coll['Type_Source'] = 'Collectivité'
df_etab['Type_Source'] = 'Établissement'
df_exp['Type_Source']  = 'Expert'

# 2️⃣ تحديد قائمة الأعمدة الكاملة اللي بغيتي
# ملاحظة: استعملت السميات كيفما طالعين عندك في الـ Terminal
full_cols = [
    'Type_Source', 
    'Administration', 
    'عدد المناصب', 
    'Corps',            # الهيئة
    'Grade',            # الدرجة
    'Nom du poste',     # اسم المنصب
    'تاريخ النشر', 
    'آخر أجل لإيداع الترشيحات', 
    'تاريخ الإمتحان'
]


# غادي نجمعو غير الجداول اللي فيهم هاد الأعمدة، والخبراء غانزيدوه واخا ناقصينو شي أعمدة
# بايثون غايفهم راسو وغايحط NaN فين ماكايناش الداتا
df_all = pd.concat([df_etat, df_coll, df_etab, df_exp], ignore_index=True)

# 4️⃣ نختارو غير الأعمدة اللي حددنا باش الجدول يكون منظم
# كانديرو هاد الخطوة باش نحيدو الأعمدة اللي معاودة بالعربية (حيت ديجا عندنا بالفرنسية)
df_all = df_all[full_cols]

print("✅ تم الجمع بنجاح مع الحفاظ على كل التفاصيل!")
print(f"📏 حجم الجدول الموحد: {df_all.shape}") # غايعطيك عدد السطور وعدد الأعمدة (9)
print("\n👀 نظرة على الأعمدة المختار :")
print(df_all.iloc[0:5, :]) # عرض أول 5 سطور مع كاع الأعمدة

df_all.to_csv('all_data_raw.csv', index=False, encoding='utf-8-sig')