# list example
courses_list = ["History", "Math", "Physics", "CompSci"]
courses_list2 = ["Nature", "Education"]
nums_list = [1, 5, 2, 4, 3]

# adding element(s).
courses_list.append("Music")  # add an item in the end of the list.
courses_list.insert(0, "Art")  # add an item at the specified index number place.
# courses_list.insert(0, courses_list2)    # insert another list at the specified index number place as ONE item.
courses_list.extend(courses_list2)  # add items in different list separately.

print(courses_list)  # show the elements
print(len(courses_list))  # number of elements
print(
    courses_list[-1]
)  # pick one element by index. -1 is always the last element in the list.
print(
    courses_list[0:2]
)  # slicing. it chooses from index 0 to (2-1)=1, so 2 elements in total.

# removing element(s).
courses_list.remove("Math")  # remove a specified item by its value.
popped = courses_list.pop()  # remove the last element.

print(popped)
print(courses_list)


# reverse the order of elements in a list
courses_list.reverse()
print(courses_list)

# sort the elements in a list
courses_list.sort()  # in alphabetical order
nums_list.sort()  # in ascending order
print(courses_list)
print(nums_list)

courses_list.sort(reverse=True)
nums_list.sort(reverse=True)
print(courses_list)
print(nums_list)

sorted_courses = sorted(courses_list)
print(sorted_courses)
print(courses_list)

# some other operations
print(min(nums_list))
print(max(nums_list))
print(sum(nums_list))

print(courses_list.index('CompSci'))
print('Education' in courses_list)

# get an item per line
for item in enumerate(courses_list, start=1):
    print(item)

# make items into joint-string.
course_str = ', '.join(courses_list)    # , or - can be used to join items.
print(course_str)

# make joined string into separate items.
new_list = course_str.split(', ')
print(new_list)



# test the difference between list and tuple.
list_1 = ["History", "Math", "Physics", "CompSci"]
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

tuple_1 = ("History", "Math", "Physics", "CompSci")
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#tuple_1[0] = 'Art'

#print(tuple_1)
#print(tuple_2)


# sets

cs_courses = {"History", "Math", "Physics", "CompSci"}
art_courses = {"History", "Math", "Art", "Design"}
print(cs_courses)
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# empty lists
empty_list = []
empty_list = list()

# empty tuples
empty_tuple = ()
empty_tuple = tuple()

# OBS! different for empty sets!!!
# empty_set = {} # this is wrong. It's a dict.
empty_set = set()

