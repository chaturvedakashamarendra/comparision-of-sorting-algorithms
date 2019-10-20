import matplotlib.pyplot as plt
import time
l=[]
output=""
performance=""
file_name=[]
#selection sort and insertion sort performance plot
sp=[]
ip=[]
insertion_plot=[]
selection_plot=[]
avg=0
avg_sp=[]
#range to be considered
ran=[5000,10000,15000,20000,25000,30000]


#function to get the input file name for processing
def get_file_name(file_name,i):
      if (i==1):
         for num in ran:
            for j in range(0,3):
                       filename.append(str(("input"+"_1_"+str(num)
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
             file_name.append(str(("input"+"_4_"+str(num)
	  +"_"+str(j)+".txt")))

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
   #print(avg_sp)
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
   for j in range(1,n):
         key=l[j]
         i=j-1
         while i>=0 and (l[i]>key):
               l[i+1]=l[i]
               i=i-1
         l[i+1]=key
   return l

#selection sort algorithm implementation
def selection_sort(l,n):
    for i in range(0,len(l)):
        ind=l.index(min(l[i:len(l)]))
        temp=l[i]
        l[i]=l[ind]
        l[ind]=temp
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
      start_time=time.process_time()
      l=insertion_sort(l,n)
      end_time=time.process_time()
      performance+="Start time is "+str(start_time)+"\n"
      performance+="End time is "+str(end_time)+"\n"
      total_time=end_time-start_time
      output+=list_str_to_int(l)+"\n\n"
      insertion_plot.append(total_time)
      l=list_int_to_str(l)
      performance+="The process time is "+str(total_time)+"\n\n"
      performance+="Performing selection sort for file "+file_name+"\n"
      output+="The output of selection sort for file "+file_name+" is\n\n"
      start_time=time.process_time()
      l=selection_sort(l,n)
      end_time=time.process_time()
      performance+="Start time is "+str(start_time)+"\n"
      performance+="End time is "+str(end_time)+"\n"
      total_time=end_time-start_time
      output+=list_str_to_int(l)+"\n\n"
      selection_plot.append(total_time)
      performance+="The process time is "+str(total_time)+"\n\n\n"
      return performance,output,selection_plot,insertion_plot

#This function has been referred from geeks for geeks and is used to plot the graph
def plot_graph(insertion_plot,selection_plot,ran,input_type):
   y1=insertion_plot
   x1=ran
   plt.plot(x1,y1, label = "insertion sort")
   y2 = selection_plot
   x2 = ran
   plt.plot(x2,y2, label = "selection sort")
   plt.xlabel('Input')
   plt.ylabel('Time')
   plt.title('Graph for input %i' %input_type)
   plt.legend()
   plt.show()
   return


#Implementation of program for various input types
choice=input("Please enter the input for which the program must run . Enter q to quit\n")
if (choice == "2" or choice== "3"):
    for f in get_file_name(file_name,int(choice)):
        l=file_to_list(f)
        n= len(l)
        performance,output,sp,ip=perform(l,f,n)
        file_write("output.txt",output)
        file_write("performance.txt",performance)
    plot_graph(ip,sp,ran,int(choice))
elif (choice == "1" or choice == "4"):
    for f in get_file_name(file_name,int(choice)):
        l=file_to_list(f)
        n= len(l)
        performance,output,sp,ip=perform(l,f,n)
        file_write("output.txt",output)
        file_write("performance.txt",performance)
    sp=get_average(sp)
    ip=get_average(ip)
    plot_graph(ip,sp,ran,int(choice))
else:
        exit(0)

