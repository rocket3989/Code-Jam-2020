# 2020 Google Code Jam Qualification
Code Jam 2020 has begun! Congratulations to everyone who qualified- I will see you in round 1A

Here are my solutions to the qualification round
## Vesitigium
This problem is all about understanding how to input and analyse a matrix from stdin

For my implementation, I created a 2d list (equivalent to a vector in c++) within which I stored the matrix as it was input

```python
matrix = []
for i in range(N):
    matrix.append([int(x) for x in input().split()])
```
Now that the given array in in memory, the problem asks for 3 numbers relating to the matrix: the trace of the matrix, the number of invalid rows, and the number of invalid columns
#### Trace
The trace is the simplest to calculate: walk along the diagonal, adding each element to a running sum

```python
trace = 0
for i in range(N):
    trace += matrix[i][i]
```
Complexity O(n)
#### Rows
In order for a row to be valid, it must have N unique elements in it. In order to verify this, for each row, I added all elements in the row to a set- then compared the size of the set to N

I use a set, as a set only keeps one copy of each unique element- so if the size of the set is smaller than the size of the row, some number of the elements were non-unique
```python
rowCount = 0
for r in range(N):
    curr = set()
    for c in range(N):
        curr.add(matrix[r][c])
    if len(curr) != N:
        rowCount += 1
```
Complexity O(n ^ 2)

Python note- instead of iterating over every element in the matrix, instead iterate over each row, and pass the whole row into the set function
```python
for row in matrix:
    if len(set(row)) != N:
        rowCount += 1
```
For this question, I knew I had to deal with rows and columns, so I used the iteration method that works for both
#### Columns
Same logic as rows, with the iteration order flipped
```python
colCount
for c in range(N):
    curr = set()
    for r in range(N):
        curr.add(mat[r][c])
    if len(curr) != N:
        colCount += 1
```
Complexity O(n ^ 2)
#### Output
Print out the three numbers calculated
```python
print("Case #{}: {} {} {}".format(tc + 1, trace, rowCount, colCount))
```
I sure wish google used a more modern python than 3.5... and got rid of the "Case" thing

[Source](./vestigum.py)
## Nesting Depth
At first glance, this problem looks quite intimidating 

But if the given string is evaluated from left to right, it can be repaired as we go- if there is a closed brace with no matching open brace- simply add it and continue

The goal of my code is to track the 'parentheses depth' as it iterates through the input, and add the correct characters to the output as it goes

Note here on strings- 
Strings are immutable, or unchangeable. That means, operations like `+=` actually create a whole new string, copy the old data, and add the new data. This can make an O(n) solution become O(n ^ 2) if one isn't careful. For this reason, I add each answer element to a list, and convert it to a string at the end

To fix the input string, I go char by char, with some casework to decide which operation is correct
#### Case 1
```python 
depth = 0
output = []
for char in s:
    if char == '(':
        depth += 1
        output.append('(')
```
The first case is the char is an open parentheses. This char is always valid, so simply add it to the output and increase the depth

#### Case 2
```python
elif char == ')':
    if depth == 0:
        depth += 1
        output.append('(')
    
    depth -= 1
    output.append(')')
```
The second case is a closed parentheses. This char is only valid if `depth > 0`. If it is not valid, then add an open parentheses, then in either case, add a closed parentheses and decrease the depth
#### Case 3
```python
else:
    d = int(char)
    while depth > d:
        output.append(')')
        depth -= 1
    while depth < d:
        output.append('(')
        depth += 1
    output.append(char)
```
The final case is a number. For this case, first cast the char to an int. Then, while the depth is too high, add close parentheses and decrease depth. While the depth is too small, do the opposite. Finally, add the char itself

#### Output
```python
while count:
    output.append(')')
    count -= 1
```
Before outputting, make sure all parentheses are closed

```python
print("Case #{}: {}".format(tc + 1, ''.join(output)))
```
output in given format, joining the generated list with an empty char

Complexity O(n)

[Source](./nesting.py)
## Parenting
For this problem, all of the events must be assigned to either parent- but it does not matter which parent gets the task. An important idea for this question is sorting the schedule by time- so the events are evaluated in order


With this in mind, a greedy approach can be used. For each event, grab one of the free parents (a parent is free if their previous task ends before or when the new task begins) and assign them the new task, marking when they are free again.

I got briefly hung up on this question, when I output my answer in order that the tasks occurred in time- but instead, they must be output in the order that they are given by the problem

```python
events = []
for i in range(N):
    l, r = [int(x) for x in input().split()]
    events.append((l, r, i))
```
First, put all of the tasks in an array, marking when they start, end, and what position they were in
```python
Jfree = -1
Cfree = -1
output = [''] * N
```
setup output array, and variables to track when the parents are free
```python
for event in sorted(events):
    if Jfree <= event[0]:
        Jfree = event[1]
        output[event[2]] = "J"
```
go through the events in sorted order. First check if J is free, and if they are, assign them the task. Mark when J is free again, and add this task to the output
```python
elif Cfree <= event[0]:
    Cfree = event[1]
    output[event[2]] = "C
```
J was not free, so try to assign the task to C. Assign the same set of variables as the last check
```python
else:
    output = ["IMPOSSIBLE"]
    break
```
No one was free! The tasks cannot be assigned, so break out after marking the output as impossible
```python
print("Case #{}: {}".format(tc + 1, ''.join(output)))
```
output the built list

Complexity O(nlogn)

[Source](./parenting.py)

## ESAb ATAd (database)
This question asks for data to be gathered through queries. For any question of this form, the goal should always be to gleam as much information as possible through each query. 

This question has the hidden array change itself secretly every 10 queries, so the question is how quickly can the new state of the array after the shuffle be determined?

The two operations on the array are flip, and invert. Which of the operations (or both, or neither) occurred can be discovered using only two queries- leaving the other 8 queries free to discover the states of new bits

more explanation to come
[Source](./database.py)

## Indicium 
I first built up a possible diagonal of the final latin square (which has a matching trace) then filled in the rest of the elements with a sudoku solver
[Source](./latin.py)