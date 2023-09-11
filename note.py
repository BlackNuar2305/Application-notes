from datetime import datetime
import datetime as DT

class Service:
    def add(notes = {}):
        heading = input("Введите заголовок заметки: ")
        note_body = input("Введите тело заметки: ")
        time = datetime.now().strftime('%d/%m/%Y')
        notes[heading] = [note_body, time]
    def delete(notes = {}):
        heading = input("Введите заголовок заметки: ")
        del notes[heading]
    def save(notes = {}):
        with open('notes.json', 'a', encoding='utf-8') as f:
            for key, value in notes.items():
                f.write(key + "; " + value[1] + "; " + value[0] + ";\n")
    def load(notes = {}):
        with open('notes.json', 'r', encoding='utf-8') as f:
            list = f.read().split('\n')
            matrix = []
            for i in list:
                if len(i) != 0:
                    matrix.append(i.split(';'))
            for i in range(0, len(matrix)):
                notes[matrix[i][0]] = [matrix[i][2], matrix[i][1]]
    def listEntries(notes = {}):
        for i in notes.keys():
            Service.printNote(i, notes)
    def output(notes = {}):
        heading = input("Введите заголовок заметки: ")
        if heading in notes.keys():
            Service.printNote(heading, notes)
        else:
            print("Такой заметки не найдено!")
    def select(notes = {}):
        start_time_str = input("Введите дату начала (dd/mm/yyyy) ")
        end_time_str = input("Введите дату конца (dd/mm/yyyy) ")
        start_time = DT.datetime.strptime(start_time_str, '%d/%m/%Y').date()
        end_time = DT.datetime.strptime(end_time_str, '%d/%m/%Y').date()
        for k, v in notes.items():
            if (DT.datetime.strptime(v[1], '%d/%m/%Y').date() > start_time and DT.datetime.strptime(v[1], '%d/%m/%Y').date() < end_time):
                print("Заголовок: " + k)
                print("Дата записи: " + v[1])
                print("Тело записи: " + v[0])
    def edit(notes = {}):
        heading = input("Введите заголовок заметки: ")
        if heading in notes.keys():
            note_body = input("Введите новое тело заметки: ")
            time = datetime.now().strftime('%d/%m/%Y')
            notes[heading] = [note_body, time]
        else:
            print("Такой заметки не найдено!")
    def printNote(key = '', notes = {}):
        print("Заголовок: " + key)
        print("Дата записи: " + notes[key][1])
        print("Тело записи: " + notes[key][0])

notes = {}
choice = True

while choice:
    command = input("Введите команду: ")
    if command == "add":
        Service.add(notes)
    elif command == "delete":
        Service.delete(notes)
    elif command == "save":
        Service.save(notes)
    elif command == "load":
        Service.load(notes)
    elif command == "list":
        Service.listEntries(notes)
    elif command == "output":
        Service.output(notes)
    elif command == "select":
        Service.select(notes)
    elif command == "edit":
        Service.edit(notes)
    elif command == "exit":
        choice = False
    else:
        print("Вы ввели неправильную команду!")
