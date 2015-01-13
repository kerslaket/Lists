#List Syntax Revision

##Task 1 - Creating a list
Complete the following table with the appropriate syntax.

|Description|Syntax|
|-----------|------|
|Create a blank list|animals = [] |
|Create a list with existing items|animals = ["Dog","Cat","Albatross"] |

##Task 2 - List operations
Complete the following table with the appropriate syntax. Assume that you are using the list you defined with existing items in Task 1.

|Description|Syntax|
|-----------|------|
|add an item to the end of a list|animals.append("Banana") |
|delete an item from the end of a list|animals.pop() |
|insert an item into the middle of a list|animals.insert(1,"Monkey") |
|change the value stored at a particular index in the list|animals[0] = "Ben"|

##Task 3 - List slices
Complete the following table with the appropriate syntax. The list you should use for this task should be called `pets` and have the following items: `"dog", "cat", "goldfish", "hamster", "rabbit", "gerbil"`

|Description|Syntax|
|-----------|------|
|A slice with the third and fourth items in the list|pets[2:4] |
|A slice containing the first two items in the list|pets[:2] |
|A slice containing the last three items in the list|pets[:3] |
|A slice with every second item in the list|pets[::2] |

##Task 4 - Lists and loops
Assuming that you have the `pets` list from Task 3 give the correct code for each of the following operations:

1. printing each item in the list

    ```python
    for item in pets:
	    print(item)
    ```

2. printing each item in the list with a number before it e.g. `1. Dog`


    ```python
    for item in pets:
	    print("{0}.{1}".format((pets.index(item) + 1), item))
	for index,item in enumerate(pets):
		print("{0}.{1}".format(index+1,pets)
    ```






> Written with [StackEdit](https://stackedit.io/).