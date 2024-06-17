import os
import shutil
from datetime import datetime
import json

# Категории файлов
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.heic'],
    'Word': ['.pdf', '.doc', '.docx'],
    'Documents': ['.txt', '.ppt', '.pptx', '.ppsx', '.xls', '.xlsx'],
    'Excel': ['.xls', '.xlsx'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', 'webm', '.3gp'],
    'Programs': ['.msi', '.exe'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Torrents': ['.torrent'],
    'Fonts': ['.ttf', '.otf'],
    'Programing/Json': ['.json'],
    'Programing/Xml': ['.xml'],
    'Programing/Java': ['.jar'],
    'Programing/Csv': ['.csv'],
    'Programing/Databases': ['.db', '.sqlite', '.sqlite3', 'sql'],
    'Programing/Python': ['.py'],
}

def get_config_path():
    appdata_path = os.getenv('APPDATA')
    config_path = os.path.join(appdata_path, 'SimpleSorter', 'config.json')
    return config_path
    

    
def load_config():
    config_path = get_config_path()
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # Если конфигурационный файл не существует, создаем его с значениями по умолчанию
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, 'w', encoding='utf-8') as json_file:
            json.dump(FILE_TYPES, json_file, ensure_ascii=False, indent=4)
        return FILE_TYPES

FILE_TYPES = (load_config())

    
def create_directories(base_path):
    for category in FILE_TYPES.keys():
        dir_path = os.path.join(base_path, category)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

def move_file(file_path, base_path):
    file_ext = os.path.splitext(file_path)[1].lower()
    file_name = os.path.basename(file_path)
    for category, extensions in FILE_TYPES.items():
        if file_ext in extensions:
            dest_dir = os.path.join(base_path, category)
            dest_path = os.path.join(dest_dir, file_name)
            if os.path.exists(dest_path):
                dest_path = resolve_name_conflict(dest_path)
            shutil.move(file_path, dest_path)
            break

def resolve_name_conflict(path):
    base, ext = os.path.splitext(path)
    counter = 1
    new_path = f"{base} ({counter}){ext}"
    while os.path.exists(new_path):
        counter += 1
        new_path = f"{base} ({counter}){ext}"
    return new_path

def sort_files(base_path):
    create_directories(base_path)
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isfile(item_path):
            move_file(item_path, base_path)

def get_script_directory():
    script_path = os.path.abspath(__file__)
    return os.path.dirname(script_path)

if __name__ == "__main__":
    base_path = get_script_directory()
    sort_files(base_path)
    print("Done")