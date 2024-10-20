def main():
    documents = [
        {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
        {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
        {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
    ]
    
    directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
    }
    
    while True:
        command = input("Введите команду (p для поиска владельца, s для поиска полки, q для выхода): ").strip().lower()
        
        if command == 'q':
            print("Завершение программы.")
            break
        else:
            process_command(command, documents, directories)
            
def find_owner(document_number, documents):
    for document in documents:
        if document['number'] == document_number:
            return f"Владелец документа: {document['name']}"
    return "Владелец документа: владелец не найден"

def find_shelf(document_number, directories):
    for shelf, docs in directories.items():
        if document_number in docs:
            return f"Документ хранится на полке: {shelf}"
    return "Документ не найден"

def process_command(command, documents, directories):
    if command == 'p':
        document_number = input("Введите номер документа: ").strip()
        result = find_owner(document_number, documents)
        print(result)
    elif command == 's':
        document_number = input("Введите номер документа: ").strip()
        result = find_shelf(document_number, directories)
        print(result)
    else:
        print("Неизвестная команда, попробуйте снова.")



# Запуск основной функции
main()