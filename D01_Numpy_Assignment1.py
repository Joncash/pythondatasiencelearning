#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
arr = np.arange(0,21) # 產生一個等差數列，起始為 0，結束為 20
print(arr)

evenArr = arr[0:21:2] #取得 arr 陣列中元素為偶數的元素
print(evenArr)

arr3 = [item for item in arr[1:21] if item %3 == 0] #取得 arr 陣列中元素為 3 的倍數的元素
print(arr3)

