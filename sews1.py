
# coding: utf-8

# In[1]:


#fibonaci using yield
def simple(n):
    prev1, prev2=0,1
    for i in range(n):
        yield prev2
        prev2, prev1 = prev1, prev2 + prev1
        

for i in simple(6):
    print(i)


# In[7]:


def updown(n):
    yield from range(n)
    yield from range(n,-1,-1)
    

print(updown(3))


# In[ ]:


if __name__ == '__main__':
    N = int(input())
    result = []
    for n in range(N):
        x = input().split(" ")
        command = x[0]
        if command == 'append':
            result.append(int(x[1]))
        if command == 'print':
            print(result)
        if command == 'insert':
            result.insert(int(x[1]), int(x[2]))
        if command == 'reverse':
            result == result[::-1]
        if command == 'pop':
            result.pop()
        if command == 'sort':
            result == sorted(result)
        if command == 'remove':
            result.remove(int(x[1]))
        print(result)


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split())) #to covert a list of no to integers
    print(hash(integer_list))


# In[3]:


def swap_case(s):
    return(s.swapcase())


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



s1 = 'abc'
s2 = '123'

""" Each character of s2 is concatenated to the front of s1""" 
print('s1.join(s2):', s1.join(s2))


# In[ ]:


def split_and_join(line):
    return("-".join(line.split()))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    


# In[ ]:


def print_full_name(a, b):
    print(f"Hello {a} {b}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# In[ ]:


def mutate_string(s, i, c):
    return(print(s[:int(i)] + c + s[int(i)+1:]))

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# In[ ]:


def count_substring(string, sub_string):
   
    return sum(1 for i in range(len(string)) if sub_string in string[i:i+len(sub_string)])
    #GENERATE 1 if match found....sum of all these one is the count of the string


    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    


# In[2]:


def capitalize(string):
    full_name = string.split(' ')
    return ' '.join((word.capitalize() for word in full_name))



if __name__ == '__main__':
    string = "My name is Nayana"
    capitalized_string = capitalize(string)
    print(capitalized_string)


# In[6]:


#If the inputs are given on one line separated by a space character, use split() to get the separate values in the form of a list:
a = input()

lis = a.split()
print (lis)

#If the list values are all integer types, use the map() method to convert all the strings to integers.
newlis = list(map(int, lis))
print (newlis)


# In[5]:


name = input("Please enter your name: ")
print(type(name))


name = float(input("Please enter your name: "))
print(type(name))


# In[1]:


total_secs = int(input("How many seconds, in total?"))
#hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
print(secs_still_remaining)

