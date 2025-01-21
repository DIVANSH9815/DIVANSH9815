# Python List Functions and Methods with Examples

### **List-Specific Methods (11)**

# 1. **append()**: Adds an element to the end of the list.
#    ```python
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  # Output: ['apple', 'banana', 'cherry']
#    ```

# # 2. **extend()**: Adds elements from another iterable to the list.
#    ```python
numbers = [1, 2]
numbers.extend([3, 4])
print(numbers)  # Output: [1, 2, 3, 4]
#    ```

# 3. **insert()**: Inserts an element at a specified index.
#    ```python
colors = ['red', 'blue']
colors.insert(1, 'green')
print(colors)  # Output: ['red', 'green', 'blue']
#    ```

# 4. **remove()**: Removes the first occurrence of a value.
#    ```python
animals = ['cat', 'dog', 'cat']
animals.remove('cat')
print(animals)  # Output: ['dog', 'cat']
#    ```

# 5. **pop()**: Removes and returns an element at a given index (default is the last element).
#    ```python
items = [10, 20, 30]
removed_item = items.pop(1)
print(removed_item)  # Output: 20
print(items)  # Output: [10, 30]
#    ```

# 6. **clear()**: Removes all elements from the list.
#    ```python
numbers = [1, 2, 3]
numbers.clear()
print(numbers)  # Output: []
#    ```

# 7. **index()**: Returns the index of the first occurrence of a value.
#    ```python
fruits = ['apple', 'banana', 'cherry']
print(fruits.index('banana'))  # Output: 1
#    ```

# 8. **count()**: Counts the occurrences of a value.
#    ```python
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))  # Output: 3
#    ```

# 9. **sort()**: Sorts the list in ascending or descending order.
#    ```python
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]
#    ```

# 10. **reverse()**: Reverses the order of elements in the list.
    # ```python
numbers = [1, 2, 3]
numbers.reverse()
print(numbers)  # Output: [3, 2, 1]
    # ```

# 11. **copy()**: Creates a shallow copy of the list.
    # ```python
original = [1, 2, 3]
duplicate = original.copy()
print(duplicate)  # Output: [1, 2, 3]
    # ```

# ---

## **General Built-In Functions Applicable to Lists**

# 1. **len()**: Returns the number of elements in the list.
#    ```python
numbers = [1, 2, 3]
print(len(numbers))  # Output: 3
#    ```

# 2. **max()**: Returns the largest element in the list.
#    ```python
numbers = [10, 20, 5]
print(max(numbers))  # Output: 20
#    ```

# 3. **min()**: Returns the smallest element in the list.
#    ```python
numbers = [10, 20, 5]
print(min(numbers))  # Output: 5
#    ```

# 4. **sum()**: Returns the sum of all elements in the list.
#    ```python
numbers = [1, 2, 3, 4]
print(sum(numbers))  # Output: 10
#    ```

# 5. **sorted()**: Returns a new sorted list without modifying the original.
#    ```python
numbers = [3, 1, 4, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 4]
#    ```

# 6. **enumerate()**: Returns an enumerate object with index-value pairs.
#    ```python
fruits = ['apple', 'banana', 'cherry']
for index, value in enumerate(fruits):
    print(index, value)
   # Output:
   # 0 apple
   # 1 banana
   # 2 cherry
#    ```

# 7. **all()**: Returns `True` if all elements in the list are truthy.
#    ```python
numbers = [1, 2, 3]
print(all(numbers))  # Output: True
#    ```

# 8. **any()**: Returns `True` if any element in the list is truthy.
#    ```python
numbers = [0, 0, 1]
print(any(numbers))  # Output: True
#    ```

# 9. **zip()**: Combines elements from two lists into pairs.
#    ```python
names = ['Alice', 'Bob']
ages = [25, 30]
combined = list(zip(names, ages))
print(combined)  # Output: [('Alice', 25), ('Bob', 30)]
#    ```

# 10. **filter()**: Filters elements based on a condition.
    # ```python
number =[1,2,3,4,5,6,7,8]
even_number =list(filter(lambda x : x % 2 == 0,number))
print(even_number)

    # ```

# 11. **map()**: Applies a function to each element of the list.
    # ```python
numbers = [1, 2, 3]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9]
    # ```

# 12. **reversed()**: Returns an iterator for reversing the list.
    # ```python
numbers = [1, 2, 3]
print(list(reversed(numbers)))  # Output: [3, 2, 1]
    # ```

# ---

### **Advanced Functions for Lists**

# 1. **reduce()** (from `functools`): Applies a rolling computation to elements in the list.
#    ```python
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24
#    ```

# 2. **itertools.chain()**: Chains multiple lists together.
#    ```python
from itertools import chain
list1 = [1, 2]
list2 = [3, 4]
combined = list(chain(list1, list2))
print(combined)  # Output: [1, 2, 3, 4]
#    ```

# 3. **itertools.combinations()**: Generates all combinations of a given length.
#    ```python
from itertools import combinations
numbers = [1, 2, 3]
comb = list(combinations(numbers, 2))
print(comb)  # Output: [(1, 2), (1, 3), (2, 3)]
#    ```
# 
# 4. **collections.Counter()**: Counts the frequency of elements in a list.
#    ```python
from collections import Counter
numbers = [1, 2, 2, 3, 3, 3]
freq = Counter(numbers)
print(freq)  # Output: Counter({3: 3, 2: 2, 1: 1})
#    ```

# 5. **pickle.dump() and pickle.load()**: Serializes and deserializes a list.
#    ```python
import pickle
numbers = [1, 2, 3]

   # Save the list to a file
with open('numbers.pkl', 'wb') as file:
    pickle.dump(numbers, file)

   # Load the list from the file
with open('numbers.pkl', 'rb') as file:
    loaded_numbers = pickle.load(file)
print(loaded_numbers)  # Output: [1, 2, 3]
#    ```

# 6. **eval()**: Evaluates a string as Python code.
    # ```python
code = "[1, 2, 3, 4]"
result = eval(code)
print(result)  # Output: [1, 2, 3, 4]
    # ```

# 7. **slice()**: Creates a slice object to extract elements from the list.
    # ```python
numbers = [10, 20, 30, 40, 50]
sliced = numbers[slice(1, 4)]  # Equivalent to numbers[1:4]
print(sliced)  # Output: [20, 30, 40]
    # ```


# Python Set Functions and Methods with Examples

### **Set-Specific Methods (14)**

# 1. **add()**: Adds a single element to the set.
#    ```python
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # Output: {1, 2, 3, 4}
#    ```

# # 2. **remove()**: Removes a specific element from the set (raises an error if not found).
#    ```python
numbers = {1, 2, 3}
numbers.remove(2)
print(numbers)  # Output: {1, 3}
#    ```

# 3. **discard()**: Removes a specific element without raising an error if it’s not found.
#    ```python
numbers = {1, 2, 3}
numbers.discard(4)  # Does nothing as 4 is not in the set
print(numbers)  # Output: {1, 2, 3}
#    ```

# 4. **pop()**: Removes and returns an arbitrary element from the set.
#    ```python
numbers = {1, 2, 3}
element = numbers.pop()
print(element)  # Output: An arbitrary element (e.g., 1)
print(numbers)  # Remaining elements in the set
#    ```

# 5. **clear()**: Removes all elements from the set.
#    ```python
numbers = {1, 2, 3}
numbers.clear()
print(numbers)  # Output: set()
#    ```

# 6. **union()**: Returns a new set with elements from both sets.
#    ```python
set1 = {1, 2}
set2 = {3, 4}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4}
#    ```

# 7. **update()**: Updates the set with elements from another set or iterable.
#    ```python
set1 = {1, 2}
set1.update([3, 4])
print(set1)  # Output: {1, 2, 3, 4}
#    ```

# 8. **intersection()**: Returns a new set with common elements of two sets.
#    ```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2)
print(result)  # Output: {2, 3}
#    ```

# 9. **intersection_update()**: Updates the set with the intersection of itself and another.
#    ```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print(set1)  # Output: {2, 3}
#    ```

# 10. **difference()**: Returns a new set with elements in the first set but not the second.
    # ```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.difference(set2)
print(result)  # Output: {1}
    # ```

# 11. **difference_update()**: Removes elements found in another set from the original set.
    # ```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print(set1)  # Output: {1}
    # ```

# 12. **symmetric_difference()**: Returns a new set with elements in either set but not both.
    # ```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 4}
    # ```

# 13. **symmetric_difference_update()**: Updates the set with elements in either set but not both.
    # ```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 4}
    # ```

# 14. **isdisjoint()**: Checks if two sets have no common elements.
    # ```python
set1 = {1, 2}
set2 = {3, 4}
print(set1.isdisjoint(set2))  # Output: True
    # ```

# 15. **issubset()**: Checks if the set is a subset of another.
    # ```python
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # Output: True
    # ```

# 16. **issuperset()**: Checks if the set is a superset of another.
    # ```python
set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # Output: True
    # ```

# ---

### **General Built-In Functions Applicable to Sets**

# 1. **len()**: Returns the number of elements in the set.
#    ```python
numbers = {1, 2, 3}
print(len(numbers))  # Output: 3
#    ```

# 2. **max()**: Retu2rns the largest element in the set.
#    ```python
numbers = {10, 20, 5}
print(max(numbers))  # Output: 20
#    ```

# 3. **min()**: Returns the smallest element in the set.
#    ```python
numbers = {10, 20, 5}
print(min(numbers))  # Output: 5
#    ```

# 4. **sum()**: Returns the sum of all elements in the set.
#    ```python
numbers = {1, 2, 3}
print(sum(numbers))  # Output: 6
#    ```

# 5. **sorte/d()**: Returns a new sorted list of the set elements.
#    ```python
numbers = {3, 1, 2}
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 3]
#    ```

# 6. **all()**: Returns `True` if all elements in the set are truthy.
#    ```python
numbers = {1, 2, 3}
print(all(numbers))  # Output: True
#    ```

# 7. **any()**: Returns `True` if any element in the set is truthy.
#    ```python
numbers = {0, 0, 1}
print(any(numbers))  # Output: True
#    ```

# 8. **enumerate()**: Returns an enumerate object (useful for iterating with index).
#    ```python
numbers = {10, 20, 30}
for index, value in enumerate(numbers):
    print(index, value)
   # Output:
   # 0 10
   # 1 20
   # 2 30
#    ```

# ---

# Would you like more details or additional examples for any of these methods? 😊


# Python Tuple Functions and Methods with Examples

### **Tuple-Specific Methods (2)**

# 1. **count()**: Returns the number of times a value appears in the tuple.
#    ```python
numbers = (1, 2, 2, 3, 4, 2)
print(numbers.count(2))  # Output: 3
#    ```

# 2. **index()**: Returns the index of the first occurrence of a value in the tuple.
#    ```python
fruits = ('apple', 'banana', 'cherry', 'banana')
print(fruits.index('banana'))  # Output: 1
#    ```

# ---

### **General Built-In Functions Applicable to Tuples**

# 1. **len()**: Returns the number of elements in the tuple.
#    ```python
numbers = (1, 2, 3)
print(len(numbers))  # Output: 3
#    ```

# 2. **max()**: Returns the largest element in the tuple.
#    ```python
numbers = (10, 20, 5)
print(max(numbers))  # Output: 20
#    ```

# 3. **min()**: Returns the smallest element in the tuple.
#    ```python
numbers = (10, 20, 5)
print(min(numbers))  # Output: 5
#    ```

# 4. **sum()**: Returns the sum of all elements in the tuple.
#    ```python
numbers = (1, 2, 3, 4)
print(sum(numbers))  # Output: 10
#    ```

# 5. **sorted()**: Returns a new sorted list of elements from the tuple without modifying the tuple.
#    ```python
numbers = (3, 1, 4, 2)
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 4]
#    ```

# 6. **all()**: Returns `True` if all elements in the tuple are truthy.
#    ```python
numbers = (1, 2, 3)
print(all(numbers))  # Output: True
#    ```

# 7. **any()**: Returns `True` if any element in the tuple is truthy.
#    ```python
numbers = (0, 0, 1)
print(any(numbers))  # Output: True
#    ```

# 8. **enumerate()**: Returns an enumerate object with index-value pairs for the tuple.
#    ```python
fruits = ('apple', 'banana', 'cherry')
for index, value in enumerate(fruits):
    print(index, value)
   # Output:
   # 0 apple
   # 1 banana
   # 2 cherry
#    ```

# 9. **zip()**: Combines elements from two tuples into pairs.
#    ```python
names = ('Alice', 'Bob')
ages = (25, 30)
combined = list(zip(names, ages))
print(combined)  # Output: [('Alice', 25), ('Bob', 30)]
#    ```

# 10. **reversed()**: Returns an iterator that yields elements in reverse order.
    # ```python
numbers = (1, 2, 3)
print(tuple(reversed(numbers)))  # Output: (3, 2, 1)
    # ```

# ---

### **Advanced Functions for Tuples**

# 1. **itertools.chain()**: Chains multiple tuples together.
#    ```python
from itertools import chain
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple(chain(tuple1, tuple2))
print(combined)  # Output: (1, 2, 3, 4)
#    ```

# 2. **itertools.combinations()**: Generates all combinations of a given length.
#    ```python
from itertools import combinations
items = (1, 2, 3)
comb = list(combinations(items, 2))
print(comb)  # Output: [(1, 2), (1, 3), (2, 3)]
#    ```

# 3. **collections.Counter()**: Counts the frequency of elements in a tuple.
#    ```python
from collections import Counter
items = (1, 2, 2, 3, 3, 3)
freq = Counter(items)
print(freq)  # Output: Counter({3: 3, 2: 2, 1: 1})
#    ```

# 4. **pickle.dump() and pickle.load()**: Serializes and deserializes a tuple.
#    ```python
import pickle
data = (1, 2, 3)

   # Save the tuple to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

   # Load the tuple from the file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
print(loaded_data)  # Output: (1, 2, 3)
#    ```

# 5. **eval()**: Evaluates a string as Python code and returns the result.
#    ```python
code = "(1, 2, 3)"
result = eval(code)
print(result)  # Output: (1, 2, 3)
#    ```

# 6. **id()**: Returns the memory address of the tuple.
#    ```python
items = (1, 2, 3)
print(id(items))  # Output: (Some memory address, e.g., 1403123456)
#    ```

# 7. **type()**: Returns the type of the object.
#    ```python
items = (1, 2, 3)
print(type(items))  # Output: <class 'tuple'>
#    ```

# 8. **dir()**: Lists all the attributes and methods available for a tuple object.
#    ```python
items = (1, 2, 3)
print(dir(items))  # Output: ['count', 'index', ...]
#    ```

# ---

### **Tuple Characteristics**
# - Tuples are immutable (cannot be changed after creation).
# - They are ordered collections of elements.
# - Tuples allow duplicate values.
# - Tuples can contain elements of mixed data types (e.g., integers, strings, other tuples).

# Would you like more examples or a deeper explanation of any specific method?

