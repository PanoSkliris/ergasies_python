# EXERCISE 1 IN PYTHON
p=int(input("Enter the dimension:"))
lst=[] 
sum=0
import random
#Για να προκυψουν τετραδες πρεπει να ειναι μεγαλυτερος  η ισος των 4 διαστασεων οποτε
if (p>=4):
      value=(p*p)/2
      value1=(p*p) #Tetragwno exei idies diastaseis
      print("Plithos thesewn",value1)
      for w in range(100):
         d1=0 #γεμισμα ασσων
         if (value!=round(value)):
           value = round(value) + 1
         for i in range(value1):
           if (d1 < value):
             d1 += 1
             lst.append(1)
           else:
             lst.append(0)
         diag = 0  # DHMIOURGIA ARXIKWN APAITOUMENWN TIMWN
         kath = 0
         oriz = 0
         lst1=[]
         lst2=[]
         random.shuffle(lst)
         print(lst)
         lst =[lst[i:i+p]for i in range(0,len(lst),p)]#DHMIOURGIA 2D LISTAS
         for i in range(len(lst)):
            print(lst[i])
         for f in range(len(lst)):
           p1=0
           p2=0
           for y in range(len(lst)):
             if(lst[f][y]==1):#Υπολογισμος οριζοντιων ασσων
                 p1 += 1
                 if(p1>=4):
                     oriz += 1
             else:
                 p1=0
             if(lst[y][f]==1):#Υπολογισμος καθετων ασσων
                p2 += 1
                if(p2>=4):
                    kath += 1
             else:
                p2=0
         k=2*p-1#Για τις διαγωνιους
         for i in range(k):
            lst1.append([])
            lst2.append([])
         for i in range(len(lst)):
             for j in range(len(lst)):
                lst1[i+j].append(lst[j][i])#Για την πλευρα της δευτερουσας διαγωνιου
                lst2[i-j-1].append(lst[j][i])#Για την πλευρα της κυριας διαγωνιου
         print(lst1)
         print(lst2)
         for i in range(k):
              p3=0
              p4=0
              x=len(lst1[i])
              x1=len(lst2[i])
              if(x>=4):
                for j in range(x):
                  if(lst1[i][j]==1):
                     p3 += 1
                     if(p3>=4):
                        diag += 1
                  else:
                       p3=0
              if(x1>=4):
               for j in range(x1):
                  if(lst2[i][j]==1):
                    p4 += 1
                    if(p4>=4):
                      diag += 1
                  else:
                      p4=0
         print(oriz,diag,kath)
         sum=sum+diag+kath+oriz
         lst=[]
      print(oriz,diag,kath)
      print(sum)
      MO=sum/100
      print(MO)
else:
    print("OLA TA ZHTOUMENA EINAI 0")