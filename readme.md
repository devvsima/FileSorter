# SimpleSorter 📁

**SimpleSorter** — это программа для автоматической сортировки файлов по категориям на основе расширений. Бот позволяет пользователю организовать файлы в папки и управлять их сортировкой в зависимости от типа. 📂

## Оглавление 📑

- [SimpleSorter 📁](#simplesorter-)
  - [Оглавление 📑](#оглавление-)
  - [Функционал 🛠️](#функционал-️)
  - [Установка 🚀](#установка-)
  - [Как это работает? 🤔](#как-это-работает-)
  - [Пример структуры конфигурации `config.json` 📝:](#пример-структуры-конфигурации-configjson-)
  - [Запуск программы ▶️](#запуск-программы-️)
    - [Запуск скрипта](#запуск-скрипта)
    - [Запуск .exe файла](#запуск-exe-файла)
  - [Как добавить новые категории? ➕](#как-добавить-новые-категории-)
  - [Обработка конфликтов имён 🔄](#обработка-конфликтов-имён-)
  - [Примечания ⚠️](#примечания-️)

---

## Функционал 🛠️

- **Сортировка файлов**: Программа сортирует файлы в зависимости от их расширения, перемещая их в соответствующие категории. 📑
- **Гибкие категории**: Категории файлов (например, изображения, документы, видео) определяются в конфигурационном файле, и можно легко добавлять новые категории. 📸📄🎬
- **Автоматическое создание папок**: При первом запуске создаются необходимые папки для каждой категории. 🗂️
- **Конфигурируемость**: Конфигурационные данные сохраняются в файле в `%APPDATA%`, что позволяет легко обновлять настройки. ⚙️
- **Иконки для категорий**: Программа поддерживает использование иконок для каждой категории. Иконки копируются в папку `%APPDATA%` при первом запуске. 🖼️

---

## Установка 🚀

1. Скачай или клонируй репозиторий. 🧑‍💻
2. Убедись, что у тебя установлен Python 3.x. ✅
3. Запусти программу через Python, используя команду:
    ```bash
    python sorter.py
    ```

---

## Как это работает? 🤔

1. **Первоначальная настройка**: При запуске программы она проверяет, есть ли уже папка с иконками в `%APPDATA%`. Если нет, иконки копируются в соответствующую директорию. 📂➡️🖼️
2. **Конфигурация**: Файл конфигурации `config.json` автоматически создается в папке `%APPDATA%`, если его нет. В нем указаны типы файлов и соответствующие категории. 🔧
3. **Сортировка**: Программа сканирует папки в текущем каталоге и перемещает файлы в соответствующие категории, в зависимости от расширения файла. 📂➡️📁

---

## Пример структуры конфигурации `config.json` 📝:

```json
{
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"]
}
```

---

## Запуск программы ▶️

### Запуск скрипта

Для того чтобы запустить программу как обычный Python-скрипт:

1. Убедись, что у тебя установлен Python 3.x.
2. Перейди в папку с файлом `sorter.py`.
3. Открой терминал или командную строку и выполни команду:
    ```bash
    python sorter.py
    ```
4. Программа начнёт сортировать файлы в текущем каталоге по категориям, определённым в конфигурации.

---

### Запуск .exe файла

Если ты собрал программу в `.exe` файл с помощью PyInstaller или другого инструмента:

1. Просто дважды кликни на файл `.exe`, чтобы запустить программу. 💻
2. Программа будет работать так же, как и при запуске скрипта, автоматически проверяя и сортируя файлы.

**Примечание**: Если ты переместишь `.exe` файл, иконки и другие данные будут искаться в папке `%APPDATA%`, что позволяет программе оставаться самодостаточной и не зависеть от текущего местоположения. 📂

---

## Как добавить новые категории? ➕

1. Открой файл `config.json`. 📑
2. Добавь новую категорию в соответствии с типами файлов, которые ты хочешь сортировать. 📂
3. После этого программа автоматически создаст соответствующие папки и начнёт сортировать файлы. 🗂️

---

## Обработка конфликтов имён 🔄

Если при сортировке программа находит файл с таким же именем в целевой папке, она создаст новый файл с добавлением индекса (например, `file (1).jpg`). Это предотвращает перезапись файлов и сохраняет их уникальными. 🔐

---

## Примечания ⚠️

- Программа автоматически создаёт папки для категорий при первом запуске. 🗂️
- Иконки для категорий должны быть размещены в папке `icons` рядом с `.exe` файлом перед компиляцией. 📂🖼️
- При перемещении `.exe` файла в другую папку, программа будет продолжать использовать иконки, хранящиеся в `%APPDATA%`. 📁🔄
