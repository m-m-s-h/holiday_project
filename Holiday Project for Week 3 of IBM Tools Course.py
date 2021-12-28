#!/usr/bin/env python
# coding: utf-8

# # Holiday Project
# 
# ***I did this for week 3 of one of the IBM Data Science Courses.***
# 
# It basically wants you to do a bunch of different types of markdown plus one piece of code. 
# 
# [Here is a markdown cheat sheet - and this is also an example of a way to create a link.](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
# 
# ##### Here is a random holiday table.
# |Movie|Actor|
# |---|---|
# |Die Hard|Bruce Willis|
# |Elf|Will Farrell|
# 
# 
# ##### Here is a numbered list of holiday movies.
# 1. The Holiday
# 2. National Lampoon's Christmas Vacation
# 3. Polar Express
# 
# ##### Below is the python code to output a Christmas tree.

# In[3]:


count=1
width=20

for i in range(10):
    print(("*"*count).center(width))
    count+=2
print("||".center(width))


# In[ ]:




