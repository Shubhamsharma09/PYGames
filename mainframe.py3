#word game
import random
from collections import Counter


def loader(wlists1):
 """Function for loading the words"""
 wfile=open("words.txt",'r')
 for line in wfile:
    wlists1.append(line.strip().lower())
 print(len(wlists1), "words are loaded !")



def displayhand(hand1):
    str1=''
    co=Counter(hand1)
    for i in co.elements():
      str1=str1+i+" "
    print(str1)


def calcword(word1,hand1,count):
    co1=Counter(hand1)
    sum=0
    sum1=0
    sum2=0
    if(count[word1]!=0):
     for i in word1:
        sum=sum+slv[i]
     if((7 *len(word1)-3 * (len(co1)-len(word1)))>1):
        sum1=(7 *len(word1)-3 * (len(co1)-len(word1)))
     else:
        sum1=1
     sum2=sum+sum1
     print("You have earned " , sum2 , "points")
     return sum2
    else:
        print("Invalid word , Try again !")
        return 0



def calcwordW(word1,hand1,count):
    co1 = Counter(hand1)
    sum = 0
    sum1 = 0
    sum2 = 0
    for i in vowels:
     word2=word1.replace("*",i,1)
     if (count[word2] != 0):
        for i in word2:
            sum = sum + slv[i]
        if ((7 * len(word2) - 3 * (len(co1) - len(word2))) > 1):
            sum1 = (7 * len(word2) - 3 * (len(co1) - len(word2)))
        else:
            sum1 = 1
        sum2 = sum + sum1
        print("You have earned ", sum2, "points")
        return sum2
     else:
        continue
    else:
        print("Invalid word , Try again !")
        return 0


def updatehand(word1, count):
    lis1=list(word1)
    co1=Counter(lis1)
    count.subtract(co1)
    return count



def generatehand(n):
    str1=''
    i=1
    co2=Counter()
    while i<=n:
     num=random.randint(97,123)
     str1=str1+chr(num)
     i=i+1
    lis1=list(str1)
    co2.update(lis1)
    return co2


def generatewild(n):
    str1=''
    co2=Counter()
    i=1
    b=random.randint(1,n)
    while i<=n:
        num=random.randint(97,123)
        if(i==b):
            str1=str1+"*"
        else:
            str1 = str1 + chr(num)
        i = i + 1
    lis1=list(str1)
    co2.update(lis1)
    return co2


vowels = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

slv = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

wlists=[]
loader(wlists)
coun=Counter(wlists)
coun1=Counter()
print("NOW , LET'S BEGIN THE GAME .......")


while True:
    n1=int(input("No. of characters you want = "))
    x=input("Now press 'W' if you want characters with wildcard entry too else, press 'H ")
    if(x=='H'):
     hand=generatehand(n1)

     displayhand(hand)
     coun2 = Counter(hand)
     print(coun2)
     b = 0
     while True:
      if(len(list(coun2.elements()))==0):
          break
      word=input("Enter word = ")
      A=set(list(word))
      B=set(coun2)
      if(len(A.difference(B))>0):
        coun1.update(coun2)
        coun1 = updatehand(word, coun1)

        coun2.clear()
        coun2.update(coun1)
        displayhand(coun2)
        coun1.clear()
        continue
      b=calcword(word,hand,coun) +b
      coun1.update(coun2)
      coun1 = updatehand(word, coun1)
      coun2.clear()
      coun2.update(coun1)
      coun1.clear()
      displayhand(coun2)

     print("Total points : ",b)
     coun2.clear()
    else:
     hand = generatewild(n1)
     displayhand(hand)
     coun2 = Counter(hand)
     print(coun2)
     b = 0
     while True:
         if (len(list(coun2.elements())) == 0):
             break
         word = input("Enter word = ")
         A = set(list(word))
         B = set(coun2)
         if (len(A.difference(B)) > 0):
             coun1.update(coun2)
             coun1 = updatehand(word, coun1)

             coun2.clear()
             coun2.update(coun1)
             displayhand(coun2)
             coun1.clear()
             continue
         b = calcwordW(word, hand, coun) + b
         coun1.update(coun2)
         coun1 = updatehand(word, coun1)
         coun2.clear()
         coun2.update(coun1)
         coun1.clear()
         displayhand(coun2)
     print("Total points : ", b)
     coun2.clear()