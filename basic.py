def swaplist(newlist):
    le = len(newlist)
    temp = newlist[0]
    newlist[0] = newlist[le-1]
    newlist[le-1] = temp
    return newlist
    
newlist = [3,5,6,7,8]    
list2 = swaplist(newlist)   
print(list2)
    
    
 
 