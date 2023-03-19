s  = int(input("enter no of S grades"))
a  = int(input("enter Attendance in percentage"))
p= int(input("No of sports activity participated"))
if s<=0 or a<=0 or p<=0:
   print("Invalid Input")
   exit()
if s>=3 and a>=90 and p>=2:
    print("Excellent")
elif s>=3 and a>=90 and p<2:
    print("Very Good")
elif s>=3 and a<90 and p>=2:
    print("Good")