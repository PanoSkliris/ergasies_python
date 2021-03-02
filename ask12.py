#ASKHSH 12 PYTHON
infile=open(input("ΔΩΣΕ ΟΝΟΜΑ ΑΡΧΕΙΟΥ: "),'r')
list_item=[line.rstrip()for line in infile]#τοποθετηση χαρακτηρων στην λιστα
lst_file=[]
if (len(list_item)==1):#ΠΕΡΙΠΤΩΣΕΙΣ ΓΙΑ ΔΙΑΧΩΡΙΣΜΟ ΓΡΑΜΜΩΝ και εντοπισμο κατoτροπτικου
  value=list_item[0]
  print(value)
  for i in range(len(value)):
     lst_file.append(value[i])
  print(lst_file)
else:
  value=list_item[0:len(list_item)]
  print(value)
  for i in range(len(value)):
    for j in range(len(value[i])):
            lst_file.append(value[i][j])
  print(lst_file)
for i in range(len(lst_file)):
     lst_file[i] = chr(128 - ord(lst_file[i]))
print(lst_file)
lst_file=lst_file[::-1]
print(lst_file)
x="".join(lst_file)
print(x)
infile.close()