import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv('kidney_disease.csv')

df['classification'] = df['classification'].str.strip()

features = ['age', 'bp', 'sg', 'al', 'bgr', 'sc', 'hemo']

df_clean = df.dropna(subset=features + ['classification'])

X = df_clean[features]
y = df_clean['classification'].map({'ckd': 1, 'notckd': 0})

print(f"X rows: {len(X)}, y rows: {len(y)}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

with open('ckd_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Project brain (ckd_model.pkl) successfully saved!")
