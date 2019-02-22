
# coding: utf-8

# In[3]:


for friend in ["Joe", "Zoe", "Zuki", "Thandi", "Paris"]:
               invite = "Hi " + friend + ". Please come to my party!"
               print(invite)
       


# In[7]:


for i in range(1, 7): 
    print(2 * i, end=" ")
print()


# In[10]:


total = 0
while True:
    response = input("Enter the next number. (Leave blank to end)")
    if response == "" or response == "-1":
        break
    total += int(response)
    print(total)
    


# In[15]:


celebs = [("Brad Pitt", 1963), ("Jack Nicholson", 1937),
                                ("Justin Bieber", 1994)]
for a, b in celebs: 
    if b < 1980:
            print(a)


# In[19]:


#count the odd numbers in a list
numbers =[10,4,25,8,6]
count =0
for number in numbers:
    if number %2 == 1:
        count+=1
print(count>0)


# In[20]:


numbers =[10,4,25,8,6]
count =0
for number in numbers:
    count += number % 2 ==1
print(count>0)


# In[22]:


### Function to take a day no and return the day name

day_dict= {1:'Sunday',2:'Monday',3:'Tuesday',4:'Thursday',5:'Friday'}
for day_num, day in day_dict:
    print(day)


# In[24]:


#Holiday exercise 
def dayw(n):
    d = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    return d[n]
a = 3                 # starting day
b = 137               # lenth of stay away
c = dayw((a+b%7)%7)   # day of return
print(c)


# In[25]:


#You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving on day number 3 (a Wednesday). You return home after 137 sleeps. Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the name of day of the week you will return on.

def dayw(n):
    d = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    return d[n]
a = 3                 # starting day
b = 137               # lenth of stay away
c = dayw(((a%7)+b)%7)   # day of return
print(c)


# In[27]:


#Count how many words in a list have length 5.
def numLen(sent, num):
    return(sum(1 for i in sent.split() if len(i)==num)) #add 1 for those that meet condition, finally add all the ones.

numLen('This is a test this', 5)


# In[1]:


#sum of the squares of the numbe
import random


xs=[]
for i in range(5):
    xs.append(random.randint(0,500))
    
def sumofsquares():
        return(sum(i*i for i in xs))

def sumofsquares():
        return(sum(map(lambda x,y: ))
    

               


# In[4]:


""""for i in range(len(seq)-1, -1, -1):    #traverse the list backwards
    if seq[i]== target:
        return i
    
return None"""





seq="abcd"
enumerate(seq)
def enumerate(seq):
    return zip(range(len(seq)),seq)



#range in reverse


# In[ ]:


griceries=["jkjd","iwd","jwjw"]

"|".join(groceries)   #string.join(sequence)

