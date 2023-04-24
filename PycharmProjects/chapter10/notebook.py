class Note(object):
    def __init__(self, contents=None):
        self.contents = contents

    # def write_contants(self, contents):
    #     self.contents = contents

    def remove(self):
        self.contents = "No Content"

    def __str__(self):
        return print(self.contents)

class NoteBook (object):
    def __init__(self,title):
        self.title = title
        self.notes = {}

    def add_note(self, new_note, page=1):
        if len(self.notes.keys()) < 300:
            if page in self.notes:
                page = 1
                while page in self.notes:
                    page += 1

                self.notes[page] = new_note

            else:
                self.notes[page] = new_note

        else:
            print('page가 모두 채워졌습니다.')
            print("title: {}\npages_number: {}\npage: {}".\
                  format(self.title, len(self.notes), tuple(self.notes.keys())))

    def __str__(self):
        return "title: {}\npages_number: {}\npage: {}".\
            format(self.title, len(self.notes), tuple(self.notes.keys()))