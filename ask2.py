#Making the Fibonacci exercise 2
t=int(input("Enter a Fibonacci term: "))# Getting the term of fibonacci
F=[0,1,2]
if t>3:#αυτο γιατι τα πρωτα στοιχεια του φιμπονατσι 0 1 2 ειναι πρωτα
   for j in range(3,t):
    num=F[j-2]+F[j-1]
    F.append(num)
    print(F[j])
   p = F[j]
   print("To p eixei timh,",p)
   import random
   for i in range(20):
     a=random.randint(1,p)
     print(a)
     if ((a**p)%p != a%p):
       break
   if (i==19):
      print("This number is prime")
   else:
     print("This number is not prime")
     print("We got out of loop in ",i+1," repetitions")
else:
    print("The numbers 0,1,2 are primes")