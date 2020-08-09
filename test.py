# with open("new.txt") as file_handler:
#     for i in file_handler:
#         print(i)

# from types import ClassMethodDescriptorType


# class Test:
#     def __init__(self,*colors):
#         self.colors=colors
#         # self.doors=doors

#     def brake(self):
#         return "Brake"

#     def stop(self):
#         return "Stop"


# if __name__ == "__main__":
#     car=Test("Red",4)
#     print(car.colors)
#     # print(car.doors)

#     b=car.brake()
#     print(b)

import csv
def read_csv(file_obj):
    read = csv.DictReader(file_obj)
    for i in read:
        print(i['first_name'])
        print(i["last_name"]) 

if __name__ == "__main__":
    with open("data.csv") as file:
        read_csv(file)
