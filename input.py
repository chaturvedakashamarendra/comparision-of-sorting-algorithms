import random
#list to store the values for various input types
l=[]
file_name=""
s=""

#range of inputs to be considered
r=[5000,10000,15000,20000,25000,30000]

def generate_input(input_option):
#code to generate input type 1
    if (input_option == "1" ):
        l=[]
        for num in r:
            for j in range(3):
                file_name="input"+"_1_"+str(num)+"_"+str(j)+".txt"
                #generating random numbers for each range
                for i in range(num):
                    l.append(str((random.randrange(1,num))))
                file_write(file_name,l)
                l=[]

#code to generate input type 2
    elif (input_option == "2"):
        l=[]
        for num in r:
            file_name="input"+"_2_"+str(num)+".txt"
            for i in range(num):
                l.append(((random.randrange(1,num))))
            l.sort()
            #converting the int values in the list to string values
            for s in range(0,len(l)):
                l[s]=str(l[s])
            file_write(file_name,l)
            l=[]

#code to generate input type 3
    elif (input_option == "3"):
        l=[]
        for num in r:
            file_name="input"+"_3_"+str(num)+".txt"
            for i in range(num):
                l.append(((random.randrange(1,num))))
            l.sort(reverse=True)
            for s in range(0,len(l)):
                l[s]=str(l[s])
            file_write(file_name,l)
            l=[]

#code to generate input type 4
    elif (input_option== "4"):
        l=[]
        for num in r:
            for j in range(3):
                file_name="input"+"_4_"+str(num)+"_"+str(j)+".txt"
                for i in range(num):
                    l.append(((random.randrange(1,num))))
                l.sort()
                for e in range(50):
                    #picking random indices of the list to swap
                    a=random.randrange(1,num,2)
                    b=random.randrange(1,num,2)
                    #swapping the values of the random indices picked
                    temp=l[a]
                    l[b]=l[a]
                    l[a]=temp
                for s in range(0,len(l)):
                    l[s]=str(l[s])
                file_write(file_name,l)
                l=[]

#code to generate input type 5
    else:
        l=[]
        for j in range(3):
            file_name="input"+"_5_"+str(j)+".txt"
            for i in range(5000000):
                l.append(str((random.randrange(1,50,1))))
            file_write(file_name,l)
            l=[]


#function to write contents to file
def file_write(file_name,l):
  #concatenating the elements of the list to a string
  s=','.join(l) #This line was referred from geeks for geeks
  fp= open(file_name,"a+")
  fp.write(s)
  fp.close()
  return

#function call to generate 5 input types
for num in range(1,6):
    generate_input(str(num))
