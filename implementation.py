import matplotlib.pyplot as plt
import resource, sys
#resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(100000)
import sys
import time
l=[]
output=""
performance=""
file_name=[]
#selection sort and insertion sort performance plot
qp=[]
ip=[]
mp=[]
insertion_plot=[]
quick_plot=[]
merge_plot=[]
avg=0
avg_sp=[]
c=0
#range to be considered
ran=[5000,10000,15000,20000,25000,30000]

#function to get the input file name for processing
def get_file_name(file_name,i):
      if (i==1):
         for num in ran:
            for j in range(0,3):
                       file_name.append(str(("input"+"_1_"+str(num)
		+"_"+str(j)+".txt")))

      elif (i==2):
         for num in ran:
            file_name.append(str(("input"+"_2_"+str(num)+".txt")))

      elif (i==3):
         for num in ran:
            file_name.append(str(("input"+"_3_"+str(num)+".txt")))

      elif (i==4):
         for num in ran:
            for j in range(0,3):
             file_name.append(str(("input"+"_4_"+str(num)+"_"+str(j)+".txt")))

      else:
         for j in range(0,3):
            file_name.append(str(("input"+"_5_"+str(j)+".txt")))
      return file_name

#function the returns the mean for input type 1 and input type 4
def get_average(l):
   avg_sp=[]
   num=0
   for j in range (6):
      avg=(l[num]+l[num+1]+l[num+2])/3
      num=num+3
      avg_sp.append(avg)
   return avg_sp

#function to write to files
def file_write(file_name,s):
   file=open(file_name,"a+")
   file.write(s)
   file.close()
   return

#function to convert the contents of input file to a list
def file_to_list (file_name):
   input_file=open(file_name,"r+")
   s=input_file.read()
   s.rstrip()
   s.lstrip()
   l=s.split(',')
   for nu in range(0,len(l)):
      l[nu]=int(l[nu])
   input_file.close()
   return l

#insertion sort algorithm implementation
def insertion_sort(l,n):
   l1=l
   for j in range(1,n):
         key=l1[j]
         i=j-1
         while i>=0 and (l1[i]>key):
               l1[i+1]=l1[i]
               i=i-1
         l1[i+1]=key
   return l1

#implementation of quick sort
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if(A[j]<=x):
            i=i+1
            A[i],A[j]=swap(A[i],A[j])
    A[i+1],A[r]=swap(A[i+1],A[r])
    return A,i+1

def quick_sort(A,p,r):
    if(p<r):
        A,q=partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)
    return A

#implementation of merge sort

def merge_sort(l):
    if len(l) >1:
        mid = len(l)//2
        Left = l[:mid]
        Right = l[mid:]

        merge_sort(Left)
        merge_sort(Right)

        i = j = k = 0
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                l[k] = Left[i]
                i+=1
            else:
                l[k] = Right[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(Left):
            l[k] = Left[i]
            i+=1
            k+=1

        while j < len(Right):
            l[k] = Right[j]
            j+=1
            k+=1
        return l
#function to convert list containing integer values to string values
def list_str_to_int(l):
   for num in range(0,len(l)):
      l[num]=str(l[num])
   s=','.join(l)
   return s

#function to convert list containing string values to integer values
def list_int_to_str(l):
   for num in range(0,len(l)):
      l[num]=int(l[num])
   return l

#function to run the algorithm and store the corresponding results
def perform(l,file_name,n):
      performance="Performing insertion sort for file "+file_name+"\n"
      output="The output of insertion sort for file "+file_name+" is\n\n"
      l1=list(l)
      s=[]
      if(c==1):
          start_time=time.process_time()
          for i in range(100000):
            s.append(insertion_sort(l1[i],50))
          end_time=time.process_time()
          output+=str(s)+"\n\n"
      else:
          start_time=time.process_time()
          l1=insertion_sort(l1,n)
          end_time=time.process_time()
          output+=list_str_to_int(l1)+"\n\n"
      s=[]
      performance+="Start time is "+str(start_time)+"\n"
      performance+="End time is "+str(end_time)+"\n"
      total_time=end_time-start_time
      insertion_plot.append(total_time)
      performance+="The process time is "+str(total_time)+"\n\n"
      performance+="Performing quick sort for file "+file_name+"\n"
      output+="The output of quick sort for file "+file_name+" is\n\n"
      l2=list(l)
      if(c==1):
          start_time=time.process_time()
          for i in range(100000):
            s.append(quick_sort(l2[i],0,49))
          end_time=time.process_time()
          output+=str(s)+"\n\n"
      else:
        start_time=time.process_time()
        l2=quick_sort(l2,0,len(l2)-1)
        end_time=time.process_time()
        output+=list_str_to_int(l2)+"\n\n"
      performance+="Start time is "+str(start_time)+"\n"
      performance+="End time is "+str(end_time)+"\n"
      total_time=end_time-start_time
      quick_plot.append(total_time)
      performance+="The process time is "+str(total_time)+"\n\n\n"
      s=[]
      l3=list(l)
      output+="The output of merge sort for file "+file_name+" is\n\n"
      if(c==1):
          start_time=time.process_time()
          for i in range(100000):
            s.append(merge_sort(l3[i]))
          end_time=time.process_time()
          output+=str(s)+"\n\n"
      else:
        start_time=time.process_time()
        l3=merge_sort(l3)
        end_time=time.process_time()
        output+=list_str_to_int(l3)+"\n\n"
      performance+="Performing merge sort for file "+file_name+"\n"
      performance+="Start time is "+str(start_time)+"\n"
      performance+="End time is "+str(end_time)+"\n"
      total_time=end_time-start_time
      merge_plot.append(total_time)
      performance+="The process time is "+str(total_time)+"\n\n\n"
      return performance,output,quick_plot,insertion_plot,merge_plot

#This function has been referred from geeks for geeks and is used to plot the graph
def plot_graph(insertion_plot,quick_plot,merge_plot,ran,input_type):
   y1=insertion_plot
   x1=ran
   plt.plot(x1,y1, label = "insertion sort")
   y2 = quick_plot
   x2 = ran
   plt.plot(x2,y2, label = "quick sort")
   y3= merge_plot
   x3=ran
   plt.plot(x3,y3, label = "merge sort")
   plt.xlabel('Input')
   plt.ylabel('Time')
   plt.title('Graph for input type %i' %input_type)
   plt.legend()
   plt.show()
   return


#Implementation of program for various input types
choice=input("Please enter the input for which the program must run . Enter q to quit\n")

if (choice == "2" or choice== "3"):
    for f in get_file_name(file_name,int(choice)):
        l=file_to_list(f)
        n=len(l)
        performance,output,qp,ip,mp=perform(l,f,n)
        file_write("output.txt",output)
        file_write("performance.txt",performance)
    plot_graph(ip,qp,mp,ran,int(choice))
elif (choice == "1" or choice == "4"):
    for f in get_file_name(file_name,int(choice)):
        l=file_to_list(f)
        n= len(l)
        performance,output,qp,ip,mp=perform(l,f,n)
        file_write("output.txt",output)
        file_write("performance.txt",performance)
    sp=get_average(qp)
    ip=get_average(ip)
    mp=get_average(mp)
    plot_graph(ip,sp,mp,ran,int(choice))
elif (choice=="5"):
    c=1
    for f in get_file_name(file_name,int(choice)):
        l=file_to_list(f)
        k=0
        l2,l1=[],[]
        for i in range(100000):
            for j in range(50):
                    l1.append(l[k+j])
            k+=50
            l2.append(l1)
            l1=[]
        performance,output,qp,ip,mp=perform(l2,f,50)
        file_write("output.txt",output)
        file_write("performance.txt",performance)

      








