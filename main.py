import mysql.connector
data_bases=mysql.connector.connect(host="localhost",user="root",password="Shubham@2001",database="bank_management")



def OpenAcc():
    n=input("Enter the Name: ")
    ac=input("Enter the Account No: ")
    dob=input("Enter the Date of Birth: ")
    add=input("Enter the Address: ")
    cnn=input("Enter the contact Number: ")
    ob=input("Enter the opening balance: ")

    data1=(n,ac,dob,add,cnn,ob)
    data2=(n,ac,ob)

    sql01=("insert into Account value(%s,%s,%s,%s,%s,%s)")
    sql02=("insert into Amount values(%s,%s,%s)")
    data_bases.cursor().execute(sql01,data1)
    data_bases.cursor().execute(sql02,data2)
    
    data_bases.commit()

    print("Data entered.....done....")
    main()

def depAmo():
    amount=input("Enter the amount you want to deposit: ")
    ac=input("Enter the Account No: ")
    x="select Balance from Amount where Account_No=%s"
    data=(ac,)
    data_bases.cursor().execute(x,data)
    result=data_bases.fetchone()
    t=result(0)+amount
    sql=("update Amount set Balance where Account_No=%s")
    d=(t,ac)
    data_bases.cursor().execute(sql,d)
    data_bases.commit()
    main()
     
def withdrawAmo():
    amount=input("Enter the amount you want to Withdraw: ")
    ac=input("Enter the Account No: ")
    x="select Balance from Amount where Account_No=%s"
    data=(ac,)
    data_bases.cursor().execute(x,data)
    result=data_bases.fetchone()
    t=result(0)-amount
    sql=("update Amount set Balance where Account_No=%s")
    d=(t,ac)
    data_bases.cursor().execute(sql,d)
    data_bases.commit()
    main()

def balEnq():
    ac=input("Enter the Account No: ")
    a=("select * from Amount where Account_No=%s")
    data=(ac,)
    data_bases.cursor().execute(a,data)
    result=data_bases.fetchone()
    print("Balance for Account",ac,"is",result[-1])
    main()

def  DisDetails():
    ac=input("Enter the Account No: ")
    a="select * from Account where Account_No=%s"
    data=(ac,)
    data_bases.cursor().execute(a,data)
    result=data_bases.fetchone()
    for i in result:
        print(i)
    main()

def CloseAcc():
    ac=input("Enter the Account No: ")
    sql1=("delete from Account where Account_No=%s")
    sql2=("delete from Amount where Account_No=%s")
    data=(ac,)
    data_bases.cursor().execute(sql1,data)
    data_bases.cursor().execute(sql2,data)
    data_bases.commit()
    main()

def main():
    print("""
    1.Open New Account
    2.Deposite Amount
    3.Withdraw Amount
    4.Balance Enquiry
    5.Display Customer Details
    6.Close Account """)

    choise=input("Enter the task want to perform: ")
    if (choise=="1"):
       OpenAcc()
    elif(choise=="2"):
       depAmo()
    elif(choise=="3"):
       withdrawAmo()
    elif(choise=="4"):
       balEnq()
    elif(choise=="5"):
       DisDetails()
    elif(choise=="6"):
       CloseAcc()
     
    else:
       print("Invalid Choice")
       main()

main()