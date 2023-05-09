#!/usr/bin/env python
# coding: utf-8

# # type range()

# ## type range

# ### type range()

# In[3]:


range(10)


# In[6]:


for i in range(10):
    print(i)


# In[11]:


maListe=list(range(10))


# In[12]:


print(maListe)


# In[10]:


for i in range(5,20,2):
    print(i)


# #EXO

# ### Ecrire un programme qui va afficher les caractéres d'une chaine de caractére avec leurs indices réspectifs.

# In[16]:


s1="Cous d'automatisation"
p=0
for i in s1:
    print("Le caractére present a le position",p,"a pour indice ",i)
    p=p+1


# In[20]:


n=0
for i in range(0,30):
    if i%2!=0:
            print(i)


# ### Ecrire un programme qui va afficher les nombres en ordre decendant (30 à 1):

# In[22]:


for i in range(30,0,-1):
    print(i)


# ## Boucle while

# In[ ]:


for i in range(10):


# In[23]:


for i in range(10):
    if i == 7:
        break
    print(i)


# In[30]:


panier = [20, 60, 78, 52,142, 125]
for prix in panier:
    if prix > 100:
        print(prix,"ce prix est cher")
        continue

    print(prix)


# #### EXO aficher les nombres impaires entre 0 et 9: 

# In[40]:


for i in range(10):
    if (i % 2 == 0):
        continue
    print(i)


# In[41]:


for i in range(10):
    for j in range(5):
        print(i,j)


# In[42]:


i=1
while(i<=10):
    print(i)
    i += 1


# In[ ]:




