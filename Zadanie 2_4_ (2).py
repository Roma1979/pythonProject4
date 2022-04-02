spisok ="инженер-конструктор Игорь", "главный бухгалтер МАРИНА", "токарь высшего разряда нИКОЛАй", "директор аэлита"
name = "Марина"
name_1 = "Николай"
name_2 = "Аэлита"
hello_str = "инженер-конструктор Игорь"
print (hello_str)                                        
hello_str = "Главный бухгалттер {}". format(name)
print (hello_str)
hello_str = "Токарь высшего разряда {}". format(name_1)
print (hello_str)
hello_str = "Директор {}". format(name_2)
print (hello_str)


""" 2 ой вариант решения"""

my_list = ["инженер-конструктор Игорь", "главный бухгалтер МАРИНА", "токарь высшего разряда нИКОЛАй", "директор аэлита"]
my_list.insert(1, "главный бухгалтер Марина")
my_list. pop (2)
my_list.insert(2, "токарь высшего разряда Николай")
my_list. pop (3)
my_list.insert(3, "директор Аэлита")
my_list. pop (4)
print(my_list)