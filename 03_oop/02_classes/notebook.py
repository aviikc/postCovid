# !/usr/bin/env python3

from datetime import datetime


class Note:
    def __init__(self, memo="", title="", tags=[]):
        self.memo = memo
        self.title = title
        self.tags = tags
        self.time_now = datetime.now()

    def match(self, filter):
        return filter in self.title or filter in self.tags

    def __del__(self):
        return f'Note titled {self.title} created on {self.time_now} deleted!'

    def __repr__(self):
        return f'{self.title} created at {self.time_now}'


class Notebook:
    def __init__(self):
        self.my_notes = []

    def addNote(self, memo_body, title_body, tags):
        my_note = Note(memo=memo_body, title=title_body, tags=tags)
        self.my_notes.append(my_note)

    def searchNote(self, filter):
        for note in self.my_notes:
            if note.match(filter):
                return note


class NotebookInterface:
    def __init__(self):
        self.my_notebook = Notebook()
        self.menu()

    def menu(self):
        print('''
        1. Add Note
        2. Search Note
        3. List all notes
        4. Quit Program
        ''')
        self.run()
        
    def run(self):
        while True:
            choice = input("Enter Choice: ")
            if choice == "1":
                memo = input("Enter the content: ")
                title = input("Enter a Title: ")
                tags = input("Enter tags seperated by commas: ").strip().split(",")
                self.my_notebook.addNote(memo, title, tags)
                continue
            elif choice == "2":
                current_filter = input("Enter an indentifiable tag or title: ")
                self.my_notebook.searchNote(current_filter)
                continue
            elif choice == "3":
                for note in self.my_notebook.my_notes:
                    print(f'{note.title} created on {note.time_now}')
                continue
            elif choice == "4":
                break
            else:
                print("Enter a valid choice.")
                continue

 mynote = Note("dcgvbihlbyttv tdxcty tgiuib", "jibrish", ["nothing", "everything"])
 print(mynote)
 my_notebook = Notebook()
 my_notebook.addNote("time to get grocery", "grocery", ["shopping", "grocery"])
 my_notebook.addNote("python class examples for sem4", "programming", ["python", "sem4"])
 my_notebook.addNote("learn shading in blender", "Shading in blender", ["blender", "shading"])
 print(my_notebook.searchNote("blender"))
myApp = NotebookInterface()

