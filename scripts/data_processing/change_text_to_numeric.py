import sys
import os
import pandas as pd

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 change_text_to_numeric.py input-file output-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = sys.argv[2]
os.makedirs(os.path.dirname(f_output), exist_ok=True)

def process_data(input_path, output_path):
    # Чтение данных
    cars = pd.read_csv(input_path)
    
    # Заполнение пропущенных значений для всех интересующих столбцов
    cars[['Make', 'Model', 'Fuel_type']] = cars[['Make', 'Model', 'Fuel_type']].fillna('Unknown')
    
    # Замена значений в столбцах 'Make', 'Model' и 'Fuel_type' на индексы
    cars['Make'], make_index = pd.factorize(cars['Make'])
    cars['Model'], model_index = pd.factorize(cars['Model'])
    cars['Fuel_type'], fuel_type_index = pd.factorize(cars['Fuel_type'])
    
    # Сохранение преобразованных данных в новый файл
    cars.to_csv(output_path, index=False)
    

# Выполнение обработки данных
process_data(f_input, f_output)
