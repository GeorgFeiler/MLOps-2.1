# MLOps-2 - Практическое задание №1

## Постановка задачи
* Создать собственный репозиторий проекта машинного обучения в git и инфраструктуру для хранения артефактов в dvc, повторив шаги, описанные в модуле.
* Установить и настроить необходимое программное обеспечение для работы (virtualbox, putty, VSCode, ssh сервер, системные linux утилиты и библиотеки python).
* Установку необходимых библиотек python важно осуществлять в виртуальное окружение venv, сохранить версии библиотек в requirements.txt, который потом опубликовать в git.
* Построить модель, определить метрику, задать гиперпараметры, провести эксперимент, сохранить эксперимент.
* Произвести изменения в конвейере, сравнить результаты метрик.

## Решение задачи
Для выполнения данной задачи был взят датасет ["Cars for sale in Moldova"](https://www.kaggle.com/datasets/alexandrududa/cars-moldova?select=cars.csv). Загружен датасет был путём применения [скрипта](https://github.com/GeorgFeiler/MLOps-2.1/blob/main/scripts/.ipynb_checkpoints/get_data-checkpoint.py). Путём [преобразований](https://github.com/GeorgFeiler/MLOps-2.1/blob/main/scripts/data_processing/get_features.py) в созданном конвейере набор данных был урезан с 9 до 6 столбцов, все значения признаков были [приведены к числовому формату](https://github.com/GeorgFeiler/MLOps-2.1/blob/main/scripts/data_processing/change_text_to_numeric.py) и результат разделён на [тренировочную и тестовую выборки](https://github.com/GeorgFeiler/MLOps-2.1/blob/main/scripts/data_processing/train_test_split.py). На тренировочном наборе была [обучена модель](https://github.com/GeorgFeiler/MLOps-2.1/blob/main/scripts/model_learning/dt.py) и [проверена](https://github.com/GeorgFeiler/MLOps-2.1/blob/main/scripts/model_learning/evaluate.py) на тестовой выборке. Изменение параметров производилось в файле [params.yaml](https://github.com/GeorgFeiler/MLOps-2.1/blob/main/params.yaml). С полным конвейеером можно ознакомиться в файле [dvc.yaml](https://github.com/GeorgFeiler/MLOps-2.1/blob/main/dvc.yaml). Оценка сохраняемой предсказательной точности сохранялась в файле [evaluate.json](https://github.com/GeorgFeiler/MLOps-2.1/blob/main/evaluate/evaluate.json). Последний оптимистичный результат составляет 0.8985365853658537.

## Технологии

* Oracle VirtualBox 7.0.18
* Ubuntu 24.04 LTS
* Python 3.9.19
* DVC 3.51.2
* Git 2.43.0
* Visual Studio Code 1.90.2

## Библиотеки

  [requirements.txt](https://github.com/GeorgFeiler/MLOps-2.1/blob/main/requirements.txt)
* aiohttp==3.9.5
* aiohttp-retry==2.8.3
* aiosignal==1.3.1
* attrs==23.2.0
* diskcache==5.6.3
* distro==1.9.0
* dulwich==0.22.1
* dvc==3.51.2
* dvc-data==3.15.1
* dvc-http==2.32.0
* dvc-objects==5.1.0
* dvc-render==1.0.2
* dvc-studio-client==0.21.0
* dvc-task==0.4.0
* fsspec==2024.6.1
* funcy==2.0
* gitdb==4.0.11
* GitPython==3.1.43
* joblib==1.4.2
* numpy==1.21.6
* pandas==1.5.0
* pathspec==0.12.1
* pygit2==1.15.0
* python-dateutil==2.9.0.post0
* pytz==2024.1
* PyYAML==6.0
* requests==2.32.3
* scikit-learn==1.1.3
* scipy==1.9.3
* tqdm==4.66.4
