import json
import os
from datetime import datetime

# Функция для создания новой заметки
def create_note():
    note_id = input("Введите идентификатор заметки: ")
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    
    save_note(note)
    print("Заметка успешно создана!")

# Функция для сохранения заметки в JSON-файл
def save_note(note):
    notes = load_notes()
    notes.append(note)
    
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

# Функция для загрузки заметок из JSON-файла
def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            return json.load(file)
    else:
        return []

# Функция для вывода списка всех заметок
def list_notes():
    notes = load_notes()
    for note in notes:
        print(f"Идентификатор: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Дата/время создания: {note['timestamp']}")
        print("------------------------")

# Функция для редактирования существующей заметки
def edit_note():
    note_id = input("Введите идентификатор заметки для редактирования: ")
    notes = load_notes()
    
    for note in notes:
        if note['id'] == note_id:
            print(f"Текущий заголовок: {note['title']}")
            new_title = input("Введите новый заголовок: ")
            print(f"Текст заметки:\n{note['body']}")
            new_body = input("Введите новый текст заметки: ")
            
            note['title'] = new_title
            note['body'] = new_body
            note['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            save_note(note)
            print("Заметка успешно отредактирована!")
            return
    
    print(f"Заметка с идентификатором {note_id} не найдена.")

# Функция для удаления существующей заметки
def delete_note():
    note_id = input("Введите идентификатор заметки для удаления: ")
    notes = load_notes()
    
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена!")
            return
    
    print(f"Заметка с идентификатором {note_id} не найдена.")

# Главная функция приложения
def main():
    while True:
        print("1. Создать новую заметку")
        print("2. Список всех заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")
        
        choice = input("Выберите действие (1/2/3/4/5): ")
        
        if choice == "1":
            create_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()