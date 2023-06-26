import pandas


class File:

    def __init__(self, path, file_type):
        self.path = path
        self.file_type = file_type.lower()
        self.sheet = ''
        self.book = ''
        return

    def open(self):
        if self.file_type == 'excel':
            self.book = pandas.ExcelFile(self.path)
            self.sheet = pandas.read_excel(self.book, usecols='c,h', header=4, names=['ID', 'Text'], index_col=0)
        elif self.file_type == 'csv':
            self.book = pandas.read_csv(self.path, header=0)
            self.sheet = pandas.DataFrame.read_csv(self.path, header=0)
        return

    def getRow(self, id):
        return
