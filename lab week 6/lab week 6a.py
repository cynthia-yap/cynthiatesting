#task 1 a
x= 10
y = x
y += 5
print(x, y)
#b
list_a = [1, 2, 3]
list_b = list_a
list_b.append(4)
print(list_a, list_b)
# c
def modify_list(some_list):
    some_list.append(4)
    return some_list
original_list = [1, 2, 3]
result = modify_list(original_list)
print(original_list, result)
# d
from copy import copy
x = ['Fellowship', 'Towers', 'King']
lst = copy(x)
lst.append('Hobbit')
# e
from copy import copy
x = [['Menace', 'Clones', 'Sith'], ['Hope', 'Empire', 'Return']]
lst = copy(x)
lst[-1][-1] = 'Jedi'
#task 2
from copy import copy
def deepcopy_exactly_2(lst):
    new = []
    for lists in lst:
        new.append([])

    for i in range(len(lst)):
        for element in range(len(lst[i])):
            new[i].append(copy(lst[i][element]))
    return new

original_list = [['a','b','c'],['d'],['e','f']]
deepcopy_exactly_list = deepcopy_exactly_2(original_list)
print("deep: ", deepcopy_exactly_list)


#task 3
def download_progress_bar(file_size_mb):
    download_speed = 0.007
    total_sec = file_size_mb / download_speed
    progress_bar_length = 60

    progress = 0
    print(f"Download started: [{' ' * progress_bar_length}]")

    half_time_seconds = total_sec / 2
    progress = int(half_time_seconds * progress_bar_length / total_sec)
    print(f"Halfway through:  [{'*' * progress + ' ' * (progress_bar_length - progress)}]")

    progress = progress_bar_length
    print(f"Download complete: [{'*' * progress}]")
file_size_mb = float(input("Enter the file size in MB to simulate download progress: "))
download_progress_bar(file_size_mb)