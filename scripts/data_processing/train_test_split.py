import yaml
import sys
import os

import pandas as pd
from sklearn.model_selection import train_test_split

params = yaml.safe_load(open("params.yaml"))["split"]

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 train_test_split.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output_train = os.path.join("datasets", "train_test_split", "cars_train.csv")
os.makedirs(os.path.join("datasets", "train_test_split"), exist_ok=True)
f_output_test = os.path.join("datasets", "train_test_split", "cars_test.csv")
os.makedirs(os.path.join("datasets", "train_test_split"), exist_ok=True)

p_split_ratio = params["split_ratio"]

df = pd.read_csv(f_input)

# Разделение данных на признаки и метки
X = df.iloc[:, 1:]
y = df.iloc[:, 0]

# Проверка распределения классов
class_counts = y.value_counts()
classes_to_remove = class_counts[class_counts < 2].index

# Удаление классов с менее чем двумя элементами
for cls in classes_to_remove:
    mask = y != cls
    X = X[mask]
    y = y[mask]

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=p_split_ratio, stratify=y)

# Объединение меток и признаков в один DataFrame для train и test наборов
train_data = pd.concat([y_train, X_train], axis=1)
test_data = pd.concat([y_test, X_test], axis=1)

# Сохранение данных с заголовками
train_data.to_csv(f_output_train, header=True, index=False)
test_data.to_csv(f_output_test, header=True, index=False)
