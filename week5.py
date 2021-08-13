'''
5. Write a program to implement round robin
'''

def make_all_lists_same_length(lists):
    longest_len = max(list(map(len, lists)))
    for lst in lists:
        lst.extend([None] * (longest_len - len(lst)))

def round_robin(lists):
    make_all_lists_same_length(lists)
    return [char for tpl in zip(*lists) for char in tpl if char is not None]

num = int(input("Enter the number of lists : "))
lists = []
for count in range(num):
    new_list = input(f'Enter the space seperated list number {count + 1} : ').split()
    lists.append(new_list)

print(round_robin(lists))