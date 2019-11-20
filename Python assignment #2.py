#!/usr/bin/env python
# coding: utf-8

# In[2]:


sub1 = int(input("enter marks of the first subject:"))
sub2 = int(input("enter marks of the second subject:"))
sub3 = int(input("enter marks of the third subject:"))
sub4 = int(input("enter marks of the fourth subject:"))
sub5 = int(input("enter marks of the fifth subject:"))
avg = (sub1 + sub2 + sub3 + sub4 + sub5)/5
if (avg >= 80 and avg <= 100):
    print ("A+")
elif (avg >= 70 and avg < 80):
    print ("A")
elif (avg >= 60 and avg < 70):
    print ("B")
elif (avg >= 50 and avg < 60):
    print ("C")
elif (avg >= 40 and avg < 50):
    print ("D")
elif (avg >= 33 and avg <40):
    print ("E")
elif (avg >= 0 and avg < 32):
    print ("Fail")
else :
    print ("You have give inappropriate number")


# In[12]:


input_num = int(input("Enter any number:"))
if input_num % 2 ==0:
    print ("its even")
else:
    print("its odd")


# In[14]:


input_num = int(input("Enter any number:"))
if input_num % 2 ==0:
    print ("its even")
else:
    print("its odd")


# In[15]:


len ("hi")


# In[20]:


len ([20,1,56,90,80,70])


# In[21]:


mylist = [1,2,3,4,5]
total = sum(mylist)
print(total)


# In[22]:


mylist = [20,1,56,90,80,70]
total = sum(mylist)
print(total)


# In[27]:


a = []
n = int(input("Enter number of element:"))
for i in range (1, n+1):
    b = int(input("Enter element:"))
    a.append (b)
a.sort()
print("largest element is :", a [n-1])


# In[42]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for nums in a:
    if nums < 5:
        print(nums)


# In[ ]:




