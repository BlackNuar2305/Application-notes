class Service:
    def add(notes = {}):
        heading = input("Введите заголовок заметки: ")
        note_body = input("Введите тело заметки: ")
        notes[heading] = note_body
    def delete(notes = {}):
        heading = input("Введите заголовок заметки: ")
        del notes[heading]
    def save(notes = {}):
        with open('notes.json', 'a', encoding='utf-8') as f:
            f.write("Hello world!")
    def load(notes = {}):
        with open('notes.json', 'r', encoding='utf-8') as f:
            print(f.read())
    def listEntries(notes = {}):
        for i in notes.keys():
            print(i)
    def output(notes = {}):
        heading = input("Введите заголовок заметки: ")
        if heading in notes.keys():
            print(notes[heading])
        else:
            print("Такой заметки не найдено!")
    def sort():
        pass
    def edit(notes = {}):
        heading = input("Введите заголовок заметки: ")
        if heading in notes.keys():
            notes[heading] = input("Введите новое тело заметки: ")
        else:
            print("Такой заметки не найдено!")


