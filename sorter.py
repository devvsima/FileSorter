import json
import os
import shutil
import sys

APP_NAME = "SimSorter"

# Категории файлов (по умолчанию)
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".heic"],
    "Word": [".pdf", ".doc", ".docx"],
    "Documents": [".txt", ".ppt", ".pptx", ".ppsx", ".xls", ".xlsx"],
    "Excel": [".xls", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", "webm", ".3gp"],
    "Programs": [".msi", ".exe"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Torrents": [".torrent"],
    "Fonts": [".ttf", ".otf"],
    "Programing/Json": [".json"],
    "Programing/Xml": [".xml"],
    "Programing/Java": [".jar"],
    "Programing/Csv": [".csv"],
    "Programing/Databases": [".db", ".sqlite", ".sqlite3", ".sql"],
    "Programing/Python": [".py"],
}


def get_script_directory():
    """Определяем директорию, где лежит исполняемый файл"""
    if getattr(sys, "frozen", False):  # Проверяем, запущено ли как .exe
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def get_config_path():
    """Путь к конфигу (APPDATA)"""
    appdata_path = os.getenv("APPDATA")
    config_dir = os.path.join(appdata_path, APP_NAME)
    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, "config.json")


def load_config():
    """Загружает конфигурацию или создаёт её, если файла нет"""
    config_path = get_config_path()

    # Проверяем, существует ли файл
    if os.path.exists(config_path):
        # Проверяем, не пустой ли он
        if os.path.getsize(config_path) > 0:
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            print("⚠️ Файл конфигурации пуст. Пересоздаём...")

    # Если файл пуст или отсутствует — создаём его заново
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(FILE_TYPES, f, ensure_ascii=False, indent=4)

    return FILE_TYPES


FILE_TYPES = load_config()


def create_directories(base_path):
    """Создаёт папки для сортировки"""
    for category in FILE_TYPES.keys():
        dir_path = os.path.join(base_path, category)
        os.makedirs(dir_path, exist_ok=True)


def move_file(file_path, base_path):
    """Перемещает файл в нужную категорию"""
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
    """Если файл уже существует, создаёт новый с (1), (2) и т.д."""
    base, ext = os.path.splitext(path)
    counter = 1
    new_path = f"{base} ({counter}){ext}"
    while os.path.exists(new_path):
        counter += 1
        new_path = f"{base} ({counter}){ext}"
    return new_path


def sort_files(base_path):
    """Основная функция сортировки"""
    create_directories(base_path)
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isfile(item_path):
            move_file(item_path, base_path)


if __name__ == "__main__":
    base_path = get_script_directory()
    sort_files(base_path)
    print(f"Сортировка завершена в папке: {base_path}")
