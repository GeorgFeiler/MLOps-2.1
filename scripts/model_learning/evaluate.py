import os
import sys
import pickle
import json
import pandas as pd
from sklearn.metrics import accuracy_score

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython evaluate.py data-file model\n")
    sys.exit(1)

df = pd.read_csv(sys.argv[1])
X = df.iloc[:, 1:]  # Используем все колонки, кроме первой, как признаки
y = df.iloc[:, 0]   # Используем первую колонку как метки

with open(sys.argv[2], "rb") as fd:
    clf = pickle.load(fd)

# Предсказание и оценка
y_pred = clf.predict(X)
score = accuracy_score(y, y_pred)

prc_file = os.path.join("evaluate", "evaluate.json")
os.makedirs(os.path.join("evaluate"), exist_ok=True)

with open(prc_file, "w") as fd:
    json.dump({"score": score}, fd)
