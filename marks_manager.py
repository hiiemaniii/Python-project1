#STUDENT MARKS MANAGER
st={"Aman":[85,90,78],"Riya":[92,88,95],"Zoya":[70,65,80]}
while True:
    print()
    print("""##**OPTIONS##**
           1.Add Student
           2.View all
           3.Show topper
           4.Exit""")
    print()
    o=int(input("Enter your choice: "))
    if o==1:
        name=input("Enter your name: ")
        print("Now Enter your marks subjectwise: ")
        x,y,z=int(input("English: ")),int(input("Hindi: ")),int(input("Computer Science: "))
        if 0<x<=100 and 0<y<=100 and 0<z<=100:
            l=[x,y,z]
            if name not in st:
                st.setdefault(name,l)
            else:
                print("Student already exist")
        else:
            print("Invalid marks, try again")
    elif o==2:
        print()
        for i,j in st.items():
            print(i,":",j)
    elif o==3:
        h=0
        t=""
        for i,j in st.items():
            if sum(j)/3>h:
                h=sum(j)/3
                t=i
        print("Topper:",t)
    elif o==4:
      print("so,here are  name of all student with grades")
      for i,j in st.items():
            gr=sum(j)/3
            if gr>85:
                print(i,f"{gr:2f}","A")
            elif gr>70 and gr<85:
                print(i,f"{gr:2f}","B")
            elif gr>50 and gr<70:
                print(i,f"{gr:2f}","C")
            else:
                print(i,f"{gr:2f}","C")

      print("""Goodbye!
      :)""")
      break
    else:
      print(""" Invalid Choice
      Enter again""")