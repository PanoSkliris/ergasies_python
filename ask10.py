#ASKHSH 10 PYTHON
dictfile=open(input("ΔΩΣΕ ΟΝΟΜΑ ΑΡΧΕΙΟΥ: "),'r')
dict2=dictfile.read()
print(dict2)
print(type(dict2))
import json
dict2=json.loads(dict2)
print(type(dict2))
vathos=0
p=0
if(dict2=={}):
    print("to vathos einai",vathos)
else:
    vathos += 1
    d=len(dict2)
    if(d==1):
      if(type(dict2)=={} or type(dict2)==[] ):
           vathos += 1
           boolean=True
           p=0
           d1=len(dict2)
           while boolean:
             for val in range(d1):
                 if(type(val)=={} or type(val)==[]):
                     vathos += 1
                     v=val
                     lv=len(val)
                     p=1
             if(p!=0):
                val=v
                d1=lv
             else:
              boolean=False
    print("to vathos einai,",vathos)
#ο κωδικας μου δεν ειναι λειτουργικος οσο θα ηθελα και απλα δεν μου εβγαινε το επιθυμητο αποτελεσμα
# και ουσιαστικα η ασκηση που σας εστειλα ειναι ενα σκεπτικο που ειχα πανω στην ασκηση αυτη