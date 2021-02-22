# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:05:00 2020

@author: wayne
"""

data = []
count = 0
with open ('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 ==0:  #% 為除的意思
            print(len(data))
print('檔案讀取完成，總共有', len(data),'筆資料')

# print(data[0])

newd = {}
for d in data:
    words = d.split()
    for w in words:   #read every word
        if w in newd:
            newd[w] += 1
        else:
            newd[w] = 1  #add new key in ditc
for w in newd:
    if newd[w] > 1000000:
        print(w, newd[w])
print(len(newd))
print(newd['Allen'])

while True:
    word = input('請問要查詢什麼字呢?')   
    if word == 'q':
        break
    if word in newd:
        print(word,'出現了',newd[word],'次數')
    else:
        print('沒有這個字')
print('感謝使用')

new = []
for d in data:
    if len(d) <100:
        new.append(d)
print('一共有', len(new) ,'筆留言長度小於100')
print(new[0])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有' , len(good),'筆留言')
print(good[0])

good = [1 for d in data if 'good' in d]
print(good)

