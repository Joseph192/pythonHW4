import csv
import os
import shutil

class Students:
    number_of_students = 0
    students_list = []
    def __init__(self, first_name, last_name, class_id):
        self.first_name = first_name
        self.last_name = last_name
        self.class_id = class_id

    @classmethod
    def create_from_row(cls, row):
        csv_list = []
        directory = 'C:/Users/lalee/Downloads'
        os.chdir(directory)
        with open('hw-4.csv', 'r') as file:
            csv_file = csv.DictReader(file)
            for x in csv_file:
                csv_list.append(x)
        name = csv_list[row]['first_name']
        cls.students_list.append(name)
        cls.number_of_students = cls.number_of_students + 1

