import os

APP_NAME = "SimSorter"

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


def get_appdata_icon_path(icon_name):
    """Возвращает путь к иконке в %APPDATA%"""
    appdata_dir = os.getenv("APPDATA")  # Папка AppData\Roaming
    icons_dir = os.path.join(appdata_dir, "SimpleSorter", "icons")
    os.makedirs(icons_dir, exist_ok=True)  # Создаём папку, если её нет
    return os.path.join(icons_dir, icon_name)


ICON_PATHS = {
    "Images": get_appdata_icon_path("images.ico"),
    "Documents": get_appdata_icon_path("documents.ico"),
    "Videos": get_appdata_icon_path("videos.ico"),
}


def load_config():
    """Загружает конфигурацию или создаёт её, если файла нет"""
    config_path = get_config_path()
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(FILE_TYPES, f, ensure_ascii=False, indent=4)
        return FILE_TYPES
