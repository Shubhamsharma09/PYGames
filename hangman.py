import random
import wordandmeaning
print("Hangman game .....................")
print("Guessing was never so much fun.............. ")
list1=[""]
while True:
 j=random.randint(0,9)
 str1=wordandmeaning.word(j)
 str2=wordandmeaning.meaning1(j)
 print("Hint for the word = ",str2)
 i=1
 n=len(str1)
 b=0
 count=0
 lists=[]
 while i<=n:
    lists.append("?")
    i=i+1
 i=1
 while i<=4:
    char=input()
    while True:
      a=str1.find(char, b, len(str1))
      if(a!=-1):
#        print(a)
        lists[a]=char
#        print("".join(lists))
        b=a+1
        count=1
        continue
      else:
        if(count==1):
            i=i-1
        break
    print("".join(lists))
    b=0
    count=0
    i=i+1
    c = "".join(lists)
    if(c==str1):
        break
 c="".join(lists)
 if(c==str1):
     print("You got the word ,Congragulations :)")
 else:
     print("""(x x)
  |
  |
  /\\ ,Hanged..............""")
     print("The word was ",str1)