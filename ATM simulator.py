# PROJECT:- ATM SIMULATOR
cp="1234"
bal=10000
at=0
m="not logged in"
while at<3:
  p=input("Enter correct PIN:")
  if p!=cp:
    at+=1
    if at==3:
      print("Card blocked")
      break
    print("Wrong PIN ,","Attempt left : ",3-at)
  else:
    print(" LOGGED IN SUCCESSFULLY")
    m="logged in"
    break
print()
l=[]
while m=="logged in" :
  print()
  print()
  print(""" ##**##**OPTIONS**##**##
          1.Balance
          2.Deposit
          3.Withdraw
          4.Exit""")
  print()
  o=int(input("Enter your choice:"))
  print()
  if o==1:
    print("Balance:","₹"+str(bal))
  elif o==2:
    n=int(input("Enter amount you want to deposit: "))
    if n>0:
      bal+=n
      l.append("+"+str(n))
      print(" New Balance:","₹"+str(bal))
  elif o==3:
    n=int(input("Enter amount to withdraw : "))
    if bal>n:
      bal-=n
      l.append("-"+str(n))
      print("New balance : ","₹"+str(bal))
    else:
      print("Insufficient Balance :(")

  elif o==4:
    print(" Here is all your history ")
    for i in range(len(l)):
      if l[i].startswith("+"):
        print(str(i+1)+".","Deposit -","₹"+l[i].replace("+",""))
      elif l[i].startswith("-"):
        print(str(i+1)+".","Withdraw -","₹"+l[i].replace("-",""))

    print()
    print("""THANK YOU
    :)     """)
    break

  else:
    print("Invalid Choice!!")
    print("Enter again!")
