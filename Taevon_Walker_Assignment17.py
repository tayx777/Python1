# Develop a function called find_common_elements that
# takes two lists as input and returns a new list containing elements that are common to both input lists.

#Create a function for the common elements

def fine_common_elements(list1, list2):
    common_elements = list(set(list1) & set(list2))
    return common_elements

#Create both lists
lista = [1, 2, 3, 4, 5]
listb = [4, 5, 6, 7, 8]

result = fine_common_elements(lista, listb)
print("Common Elements: ", result)