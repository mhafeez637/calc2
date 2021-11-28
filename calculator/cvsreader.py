import csv
from calculator.absolutepath import abspath


def Classfactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []
        try:
            with open(abs_path(filepath)) as text_data:
                csv_data = csv.DictReader(text_data, delimiter=',')
                for row in csv_data:
                    self.data.append(row)
        except OSError:
            print('cannot open', filepath)

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(Classfactory(class_name, row))
        return objects