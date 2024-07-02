import os
import kaggle

def download_kaggle_dataset():
    # Устанавливаем рабочую директорию для скачивания
    download_dir = 'datasets/raw'
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Указываем идентификатор датасета
    dataset = 'alexandrududa/cars-moldova'

    # Скачиваем файл cars.csv
    kaggle.api.dataset_download_file(dataset, 'cars.csv', path=download_dir)

    # Разархивируем скачанные файлы
    os.system(f'unzip -o {download_dir}/cars.csv.zip -d {download_dir}')

    # Удалим zip-файлы после разархивирования
    os.remove(f'{download_dir}/cars.csv.zip')

if __name__ == '__main__':
    download_kaggle_dataset()