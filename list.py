                        ####list
cap=['mca','mca2']
print(cap)
me=["archana","1234567894","11609160","a13"]
print(me)
##append function
me.append("student")
###negative index
print(me[-1])
print(me)
##empty string
empty=[]
print(empty)
empty.append(1)
print(empty)
####nested list
x=[[1,2,3],['a','b','c','d']]
print(x)

###length
print(len(x))


                  #####selfstudy
thelist=[0,5,10,15,20]
print(thelist)

##slice{5,10,15}
x=thelist[1:4]###take one+ index
print(x)

###assign the values to slice list
y=thelist[1:4]=[1,6,9]
print(y)
print(thelist)###list becomes[0,1,6,9,20]

###assigning unequal number arguments with respect to slice nus.
y=thelist[1:4]="we"
print(y)
print(thelist)####[0,w,e,10]

words=["we","are","family","so","we","have","to","love","each","others" ]
print(words)
x=words[1:5]=["do","not"]
print(x)
x=words[:5]
print(x)
x=words[:-5]
print(x)

print(words)

###delete elements from list
###1st method
y=words[1:5]=[]
print(y)
print(words)
##2nd method
x=['one','two','three','four','five']
print(x)
##y=del( x[3])                                    ###not working
print(y)

###slicing using single qutation
print("single qutation")
x=['one','two','three','four','five']
print(x)
n=x[1]=['a','b','c']
print(n)
print(x)###[one,[a,b,c],three,four,five]
n=x[1:1]=['a','b','c']                              ###d
print(x)
n=x[:1]=['a','b','c']    ###d
print(x)

###create copy of the list using slices
x=['one','two','three','four','five']
print(x)
y=x[:]
print(y)

###append
x=['one','two','three','four','five']
print(x)
y=x.append("six")
print(y)                        ###give none why?
print(x)

###reverse
x=['one','two','three','four','five']
print(x)
y=x.reverse()
print(x)

###
x=['one','two','three','four','five']
y=x[::]
print(y)

###length
x=['one','two','three','four','five']
y=len(x)
print(y)
###boolean
y="one" in x
print(y)
###
x=[1,2,3,4,5,6,7,8,9]
print(x)
y=x[1:5:2]
print(y)
y=x[1:2:]
print(y)+
y=x[:10]
print(y)
y=x[1:]
print(y)

###addition
l1=[7,8,1]
l2=[8,5,1]
a=l1+l2####concatination
print(a)
s=add(l1,l2)
print(s)
















