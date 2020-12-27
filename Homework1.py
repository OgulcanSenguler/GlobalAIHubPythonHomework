#!/usr/bin/env python
# coding: utf-8

# In[7]:


a = input(" What is your name ?")
print(type(a))
b = input(" What İs your Surname ?") 
print(type(b))
c = int(input(" How old are you ? "))
print(type(c))
d = float(input(" How tall are you ?")) #You must use (.) for the float numbers other wise you get a error.
print(type(d))
e = input(" Where are you from ? ")
print(type(e))
print(f"Your Name is {a} . Your Surname is {b} . Your Old is {c} . Your Tall is {d} Your Country is {e}".format(a, b, c, d, e))
print()


# In[ ]:




