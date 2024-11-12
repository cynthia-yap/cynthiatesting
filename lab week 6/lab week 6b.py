table = [
['Australia', 'Funny that you have asked; MCD4710 will never gonna give you up never gonna let you down :).'],
['Australia', 'I have thought the unit was so fun that they might rename the unit as fun 4710!'],
['Malaysia', 'Aside from Python, I have also learned about developing logic in this units.'],
['Australia', 'Do you think Robbie can pass the test or become a Python programmar?'],
['Malaysia', 'The quality of examples were great!'],
['Australia', 'Solving the quadratic equation was challenging but rewarding!'],
['Malaysia', 'I say random things sometimes and type random characters like #&#$***!'],
['Malaysia', 'The unit was not challenging at first but then became harder.'],
['Australia', 'The student challenges are no challenge for me!']
]
from copy import deepcopy
#task 1

def create_new_copy(table):
    new_copy = deepcopy(table)
    return new_copy
    pass
def add_row(row,table):
    nic= table.append(row)
    pass
def delete_row(index,table):
    del table[index]
    pass
def insert_row(index,row,table):
    table.insert(row,index)
    pass
def edit_row(index,row,table):
    table[index]=row
    pass
def add_coulomn(column,table):
    if len(table) == len(column):
        for i in range(len(table)):
            table[i].append (column[i])
    else:
        print("error")

# #task 2
def create_new_copy(table):
    new = []
    for i in table:
        new.append([])

    for i in range(len(table)):
        for j in range(len(table[i])):
            new[i].append(table[i][j])

    return new
deepy = create_new_copy(table)
print(deepy)

#task 3

#1 unwanted word
unwanted = "!@#$%^&*()_-+=[]{};,<>./?"
string = "I am nicholas..././asa"
eStr = ""
for c in string:
    if c in unwanted:
        c = ""
    eStr+=c
print(eStr)

#2 replace the  long space
a= "I    am    you"
x = str(a).replace("    ", " ")
print(x)

#3 removing the space
b= "Python  is easy and fun to other people"
y = str(b).replace(" ", "")
print(y)


#4 convert lower
lst=[" I AM  YOU", "YOU ARE ME"]
newList = []
for i in lst:
    newList.append(str(i).lower())
print(newList)