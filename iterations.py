

#%%

my_list = [4, 7, 0, 3]


# get an iterator using iter()
my_iter = iter(my_list)

my_iter

## iterate through it using next() 

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

#prints 0
print(my_iter.__next__())

#prints 3
print(my_iter.__next__())

print('for loop:')
for element in my_list:
    print(element)

#Self define iterator
class PowTwo:      #   """Class to implement an iterator  of powers of two"""
    def __init__(self, max = 0):
        self.max = max

    def __iter__(self): #Iteration method
        self.n = 0
        return self

    def __next__(self): #next method
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

#Using the iterator
a = PowTwo(4)
print('a: ', a)
i = iter(a)
print('i: ', next(i))
print('i: ', next(i))


for j in PowTwo(5):
    print('j: ', j)


l = range(1,10)
iter(l)
print(next(l))

## numpy array iteration
import numpy as np 
array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
for i in array:
    for j in i:
        print(j)


#dataframe iteration with pandas
import pandas as pd 
data = {'A':[1,2], 'B':[3,4], 'C':[5,6]}
df = pd.DataFrame(data=array, columns = ['A','B','C','D'])  
for i in df:
    #print(i)
    print(df[i])

#Generating random classes and populating array of labels
n = 10
s = 20
x = np.random.randint(0,n, size=s)
label = np.zeros((s,n))
label[list(range(0,s)), [x]] = 1
x, label