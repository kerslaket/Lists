names = ['Jim', 'Bob', 'Alison', 'Jo', 'James']

element_sought = input('Enter the name you are searching for : ')
this_element = 0
found = False
while not found:
       if names[this_element] == element_sought:
          found = True
       else:
          this_element = this_element + 1
          if this_element == 5:
              break

if found:
   print('{0} was in element {1} in the list'.format(element_sought, this_element))
else:
   print('Not found')
