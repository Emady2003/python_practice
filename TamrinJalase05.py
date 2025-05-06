# 001
list1 = []
inlist1 = input("list1 : ? ")
while inlist1 != '':
    list1.append(inlist1)
    print(list1)
    inlist1 = input("list1 : ? ")
list2 = []
inlist2 = input("list2 : ? ")
while inlist2 != '':
    list2.append(inlist2)
    print(list2)
    inlist2 = input("list2 : ? ")
list3 = (set(list1)-set(list2))
print(list(list3))
# 001
# 002
listi = []
inlisti = input("listi : ? ")
while inlisti != '':
    listi.append(inlisti)
    print(listi)
    inlisti = input("listi : ? ")
numlist = []
for item in listi :
    numlist.append(int(item))
numlist.sort()
strlist = []
for item in numlist :
    strlist.append(str(item))
if strlist == listi :
    print("yes")
else :
    print("no")
# 002
# 003
import random
listi = ["hello","mello","tello","yello"]
listo = []
for i in range(1,101):
    listo.append(random.choice(listi))
hasele = filter(lambda x : x == "hello" ,listo)
print(list(hasele))
# 003
# 004
list_1=["milk","suger","butter","yogurt","cheese"]
list_2 =  [5,2,10,1,3]
shop_list = {}
counter = 0
for item in list_1:
    shop_list[str(item)] = list_2[counter]
    counter =+ 1
print(shop_list)
# 004
# 005
my_dict = {"yek":1,
            "do":2,
            "se":3,
            "chahar":4,
            "panj":5,
            "dah":10,
            "noh":9,
            "hasht":8}

my_list = list(my_dict.items())
my_list.sort(key=lambda x :x[1])
print(my_list)
# 005
# 006
listi = []
sentence = str(input(":: "))
sentence = sentence.split(" ")
set_sentence = list(set(sentence))
for item in set_sentence:
    counter = 0
    for ytem in sentence :
        if item == ytem :
            counter += 1
    print(item,"=",counter)
print(listi)
# 006

###
clip = '''Text Encoder: The text endoer is a transformer based on the famous Attention is All You Need paper. The team has used a 63M-parameter 12-layer 512-wide model with 8 attention heads.
Image Encoder: For the image encoder, the team considered two models - Resnet and ViT. The team experimented with different variations of these two models and ultimately found that ViT performed the best and used it as an image encoder
Dataset: Thea team constructed a new dataset of 400 million(image, text) pairs collected from a variety of publicly available sources on the Internet. The team focused on including all words that were present at least 100 times in the English version of Wikipedia which resulted in a set of 500000 words and ensured that each word was present at least in 20000 image text pairs. The dataset is referred to as WebImageText (WIT)'''
clip = clip.split()
result = {}
for item in clip:
    print(clip.count(item))
    result[item] = clip.count(item)
print(result)
