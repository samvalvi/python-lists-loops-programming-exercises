chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    new_list = []
    for one in list1:
        new_list.append(one)
    for two in list2:
        new_list.append(two)
    return new_list



print(merge_list(chunk_one, chunk_two))