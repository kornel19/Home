"""
Write a program that reads from the user an integer and then displays a Christmas tree with that many levels with provided
number of levels.

For example, for 3 display:

```
    *
  * * *
* * * * *
```
"""

tree = int(input('Provide number of levels: '))

for i in range (0, tree):
    stars = i * 2 + 1
    spaces = (tree - i) * 2
    print (spaces * ' ' + '* ' * stars)
