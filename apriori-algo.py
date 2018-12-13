transactions=[['A','C','D'],['B','C','E'],['A','B','C','E'],['B','E'],['A','B','C','F']]
tables=[{}]
supmin=2
for i in range(len(transactions)):
    for j in range(len(transactions[i])):
        if((transactions[i][j],) not in tables[0]):
            tables[0][(transactions[i][j],)]=1
        else:
            tables[0][(transactions[i][j],)]+=1
products=list(tables[0].keys())
print(tables[0])
poplist=[]
for i in range(len(tables[0])):
    if(tables[0][products[i]]<supmin):
        #print(tables[0][products[i]])
        poplist.append(products[i])
#print(poplist)
for i in range(len(poplist)):
        print("deleting:",poplist[i])
        tables[0].pop(poplist[i],None)
products=list(tables[0].keys())
print(tables[0])
#print(products)
c=2
def notin(new,tablelist):
  for existing in tablelist:
    if set(new)==set(existing):
      return False
  return True
scans=len(tables[0])-c+1
for i in range(scans):
    tables.append(tables[c-2])
    tablelist=list(tables[c-1].keys())
    tablelistnew=[]
    print("\n")
    for j in range(len(tables[c-1])):
      for k in range(0,len(products)):
        #print(products[k],tablelist[j])
        if products[k][0] not in tablelist[j] and notin(tablelist[j]+products[k],tablelist):      
          tablelistnew.append(tablelist[j]+products[k])
          tablelist.append(tablelist[j]+products[k])
    #print(tablelistnew)
    newtable={}
    for j in range(len(tablelistnew)):
      frequency=0
      for k in range(len(transactions)):
        flag=0
        for l in range(len(tablelistnew[j])):
          if(tablelistnew[j][l] not in transactions[k]):
            flag=-1
            break
        if flag==0:
          frequency+=1
      newtable[tablelistnew[j]]=frequency
    tables[c-1]=newtable
    entries=list(tables[c-1].keys())
    poplist=[]
    for j in range(len(tables[c-1])):
      if(tables[c-1][entries[j]]<supmin):
        #print(tables[0][products[i]])
        poplist.append(entries[j])
    #print(poplist)
    print(tables[c-1])
    for j in range(len(poplist)):
      print("deleting:",poplist[j])
      tables[c-1].pop(poplist[j],None)
    print(tables[c-1])
    c+=1
print("\n")
for table in tables:
  print(table)