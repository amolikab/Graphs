import random
import math

def remove(newrow,keep,discard):
    vertex = newrow[0]
    i =1
    while(i<len(newrow)):        
        if((newrow[i] == keep)|(newrow[i] == discard)):
            del(newrow[i])
        else:
            i=i+1

def replace(row2,replace_var):
    delete_var = row2[0]
    numofneigh = len(row2)
    rows = len(arr)
    k=1
    i=0
    j=0
    while((k < numofneigh)&(i<rows)):
        if(arr[i][0] == row2[k]):
            #to avoid self loop
            if(arr[i][0] == replace_var):
                z = arr[i]
                m = 1
                while(m<len(z)):
                    if(z[m] == delete_var):
                        del(z[m])
                    else:
                        m = m+1 
                    arr[i] = z
            
            else:
                z = arr[i]
                m = 1
                while(m<len(z)):
                    if(z[m] == delete_var):
                        z[m] = replace_var
                        break
                    else:
                        m = m+1 
                    arr[i] = z
                      
            k = k+1
            i = 0
            
        else:
            i = i+1
            
    
    
    
def contract(x,y):
    row1 = arr[x]
    row2 = arr[y]
    #print("merging row %d into row %d" %(row2[0],row1[0]))
    #print("combined row is")
    newrow = row1 + row2 
    #print(newrow)
    remove(newrow,row1[0],row2[0])
    #print("new row after deleting %d" %row2[0])
    #print(newrow) 
    if(x>y):
        del(arr[y])
        del(arr[x-1])
    else:
        del(arr[x])
        del(arr[y-1])
    arr.append(newrow)
    #print("new array without removing neigh")
    #print(arr)
    replace(row2,row1[0])
    


#arr = [[1,2,3,4,5],[2,1,4,5],[3,1,4,6],[4,3,1,2,5,6],[5,2,4,1],[6,3,4]];



with open("kargerMinCut.txt","r") as f:
    arr = [map(int,line.split()) for line in f  ]


n = len(arr)
print n
n1 = int(math.ceil(n * n * math.log(n)))
print n1
n2 = 4
#print (arr)
mincut = n

while(n1 > 0):
    #print("value of n1 is %d" %n1)
    #arr = [[1,2,3,4,5],[2,1,4,5],[3,1,4,6],[4,3,1,2,5,6],[5,2,4,1],[6,3,4]];
    with open("kargerMinCut.txt","r") as f:
        arr = [map(int,line.split()) for line in f  ]

    n = len(arr)
    while(n>2):
        q = random.sample(range(0,n-1),1)
        q1 = q[0]
        #print ("value of first row %d " %q1)
        w = arr[q1]
        row = w[1:]
        #print row
        r = random.sample(row,1)
        i = 0
        while(i<n):
            if(arr[i][0] == r[0]):
                r1 = i
                break
            else:
                i = i+1            
        #print r1
        #print ("sending the index %d and %d" %(q1,r1))
        contract(q1,r1)
        #print(arr)
        n = n-1  
    mincut1 = len(arr[0])-1
    print ("mincut1 is %d" %mincut1)
    if(mincut1<mincut):
        mincut = mincut1
        print("mincut is changed to %d" %mincut)
    #print("Done")  
    n1 = n1-1

print("mincut is %d" %mincut)








