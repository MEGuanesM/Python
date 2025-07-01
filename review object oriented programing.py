class Person:

    def __init__(self, last_name, first_name, age):
        self._last_name = last_name
        self._first_name = first_name
        self._age = age
    
    @property
    def last_name(self):
        return self._last_name
    @property
    def first_name(self):
        return self._first_name
    @property
    def age(self):
        return self._age
    
    def happy_birthday(self):
        self._age = self._age + 1
    
    def __str__(self):
        return"{} {}: {}".format(self.first_name, self.last_name, int(self.age))

from Person import Person

class Student(Person):
    def __init__(self,last_name, first_name, age, student_id, grade_level):
        super().__init__(last_name, first_name, age)
        self._student_id = student_id
        self._grade_level = grade_level

    @property
    def student_id(self):
        return self._student_id

    @property
    def grade_level(self):
        return self._grade_level

    def happy_birthday(self):
        super().happy_birthday()
        self._grade_level = self._grade_level + 1

    def __str__(self):
        return "{} ({} - {})".format(super().__str__(), self.student_id, self.grade_level)

from Person import Person


class Teacher(Person):
    def __init__(self, last_name, first_name, age, classroom, salary):
        super().__init__(last_name, first_name, age)
        self._classroom = classroom
        self._salary = salary

    @property
    def classroom(self):
        return self._classroom

    @property 
    def salary(self):
        return self._salary

    def happy_birthday(self):
        super().happy_birthday()
        self._salary = self._salary + 1000

    def __str__(self):
        return "{} ({} - ${})".format(super().__str__(), self.classroom, self.salary)

import sys


class View:
    def show_menu(self):
        print("Please enter one of the following options:\n add student\n add teacher\n list people\n exit")
        reader = sys.stdin.readline()
        return reader.strip()

    def add_student(self):
        print("Enter the following separated by one space")
        print("last_name first_name age student_id grade_level")
        reader = sys.stdin.readline()
        return reader.strip()

    def add_teacher(self):
        print("Enter the following separated by one space")
        print("last_name first_name age classroom salary")
        reader = sys.stdin.readline()
        return reader.strip()

    def list_people(self, persons):
        i = 0
        for j in persons:
            print("{}) {}".format(i, j))
            i = i + 1

    def show_error(self, error):
        print("Error: {}".format(error))

#why???
    def __init__(self):
        pass

from Person import Person
from Student import Student
from Teacher import Teacher
from View import View
import sys


class Controller:
    def main(args):
        Controller().run()

    def __init__(self):
        self._persons = []
        self._view = View()

    @property
    def persons(self):
        return self._persons

    @persons.setter
    def persons(self, person):
        self._persons = person

    def run(self):
        while True:
            reader = self._view.show_menu()
            if reader == "add student":
                self.add_student(self._view.add_student())
            elif reader == "add teacher":
                self.add_teacher(self._view.add_teacher)
            elif reader == "exit":
                break
            else:
                self._view.show_error("Invalid Input")
                

    def add_student(self, reader):
        try:
            arr = reader.split(" ")
            student = Student(arr[0], arr[1], arr[2], arr[3], int(arr[4]))
            self._persons.append(student)
        except Exception as e:
            self._view.show_error(e)

    def add_teacher(self, reader):
        try:
            arr = reader.split(" ")
            teacher = Teacher(arr[0], arr[1], arr[2], arr[3], arr[4])
            self._persons.append(teacher)
        except Exception as e:
            self._view.show_error(e)


if __name__ == "__main__":
    Controller.main(sys.argv)