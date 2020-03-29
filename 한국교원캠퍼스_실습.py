#!/usr/bin/env python
# coding: utf-8

# ##1.주피터노트북이란?
# 

# 오픈소스로서 글, 이미지, 동영상, 수학공식, 데이터분석 등에 최적화된 웹어플리케이션입니다.

# ##2.출력 "Hello World"  
# 

# In[13]:


print("Hello World") 


# ##3.수학

# In[15]:


3+8


# #3-1.함수

# In[21]:


def add(a,b):
    return a+b


# In[20]:


add(6,9)


# #3-2.방정식

# \begin{align}
# \dot{x} & = \sigma(y-x) \\
# \dot{y} & = \rho x - y - xz \\
# \dot{z} & = -\beta z + xy
# \end{align}

# #3-3.The Cauchy-Schwarz Inequality (부등식)

# \begin{equation*}
# \left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
# \end{equation*}

# ##4.시각화

# #4-1.이미지

# In[11]:


from IPython.display import Image
 
Image("https://www.teacher21.co.kr/_img/logo_new.png")


# #4-2.동영상

# In[4]:


from IPython.display import YouTubeVideo
 
YouTubeVideo("BHrZmhXhh9g")


# #4-3.표

# In[19]:


import pandas as pd

df = pd.DataFrame([
        ['서울', 18189, 17925],
        ['인천', 10204, 10204],
        ['대구', 8080, 8080]
    ], columns=['지역', '2013년 12월', '2014년 1월'])

print(df)


# #4-4.크롤링

# In[ ]:


from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all('a'):
        print(anchor.get('href', '/'))


# #4-4.그래프 

# In[2]:


from cycler import cycler
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Define a list of markevery cases and color cases to plot
cases = [None,
         8,
         (30, 8),
         [16, 24, 30],
         [0, -1],
         slice(100, 200, 3),
         0.1,
         0.3,
         1.5,
         (0.0, 0.1),
         (0.45, 0.1)]

colors = ['#1f77b4',
          '#ff7f0e',
          '#2ca02c',
          '#d62728',
          '#9467bd',
          '#8c564b',
          '#e377c2',
          '#7f7f7f',
          '#bcbd22',
          '#17becf',
          '#1a55FF']

# Configure rcParams axes.prop_cycle to simultaneously cycle cases and colors.
mpl.rcParams['axes.prop_cycle'] = cycler(markevery=cases, color=colors)

# Create data points and offsets
x = np.linspace(0, 2 * np.pi)
offsets = np.linspace(0, 2 * np.pi, 11, endpoint=False)
yy = np.transpose([np.sin(x + phi) for phi in offsets])

# Set the plot curve with markers and a title
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.6, 0.75])

for i in range(len(cases)):
    ax.plot(yy[:, i], marker='o', label=str(cases[i]))
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.title('Support for axes.prop_cycle cycler with markevery')

plt.show()


# #5.성능체크

# In[1]:


get_ipython().run_line_magic('timeit', '3+8')


# #6.시계

# In[6]:


import datetime
datetime.datetime.utcnow()


# #7.서클런

# import turtle as t
#  
# n = 60    # 원을 60번 그림
# t.shape('turtle')
# t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
# for i in range(n):
#     t.circle(120)       # 반지름이 120인 원을 그림
#     t.right(360 / n)    # 오른쪽으로 6도 회전
