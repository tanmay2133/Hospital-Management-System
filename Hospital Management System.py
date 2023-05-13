import mysql.connector as sqltor
mycon=sqltor.connect(host='127.0.0.1',user='root',passwd='Tanmay21',database='hospital')
cursor=mycon.cursor()

print("""
                                    ==========================================================================================

                                                                     WELCOME TO CITY HOSPITAL
                                                                 
                                    ==========================================================================================
""")
while True:
    print("    AVAILABLE USERS/MODES ARE:")
    print("        PRESS 1 FOR PATIENT")
    print("        PRESS 2 FOR DOCTOR")
    print("        PRESS 3 FOR NURSE")
    print("        PRESS 4 FOR PAYMENT")
    print("        PRESS 5 FOR EXIT")
    print()
    ch=int(input("Enter your choice here: "))
    if ch==1:
        while True:
            print('-------------------------------------------------------------------------------------------------------------------------')
            print("        To add new patient record PRESS A")
            print("        To view existing patient record PRESS B")
            print("        To update existing patient record PRESS C")
            print("        To delete patient record PRESS D")
            print("        To go back PRESS E")
            print('-------------------------------------------------------------------------------------------------------------------------')
            print()
            pch=input("Enter your choice: ")
            if pch=='A':
                pid=input("Enter the patient ID: ")
                pname=input("Enter patient's name: ")
                pdob=input("Enter date of birth of the patient in format YYYY-MM-DD: ")
                page=int(input("Enter the patient's age (in years): "))
                psex=input("Enter patient's gender M/F: ")
                pbgp=input("Enter patient's blood grp: ")
                pdoa=input("Enter date of admission of the patient in format YYYY-MM-DD: ")
                padd=input("Enter patient's address: ")
                ppno=int(input("Enter patient's phone number: "))
                pdis=input("Enter Patient's injury/Disease: ")
                pst="INSERT INTO PATIENT(PId,PName,DOB,Age,Sex,BloodGrp,DOA,Address,PhNo,Injury_Disease) values('{}','{}','{}',{},'{}','{}','{}','{}',{},'{}')".format(pid,pname,pdob,page,psex,pbgp,pdoa,padd,ppno,pdis)
                cursor.execute(pst)
                mycon.commit()
                print("Patient record successfully added")
                pst1="SELECT * FROM PATIENT WHERE PId='{}'".format(pid)
                cursor.execute(pst1)
                data=cursor.fetchone()
                print(data)
            elif pch=='B':
                pid=input("Enter the patient ID: ")
                print("The record is: ")
                pst1="SELECT * FROM PATIENT WHERE PId=pid"
                cursor.execute(pst1)
                data=cursor.fetchone()
                print(data)
            elif pch=='C':
                while True:
                    print('''The available columns are
                                 PId
                                 PName
                                 DOB
                                 Age
                                 Sex
                                 BloodGrp
                                 DOA
                                 Address
                                 PhNo
                                 Injury_Disease
                                 DOD
                                 PaymentMode
                                 AmountToBePaid''')
                    pid=input("Enter the patient ID: ")
                    pcol=input("Enter the column name you want to update: ")
                    if pcol in ['Age','PhNo','AmountToBePaid']:
                        pnew=int(input("Enter the new value: "))
                        pst="UPDATE PATIENT SET {}={} WHERE PId='{}'".format(pcol,pnew,pid)
                        cursor.execute(pst)
                        break
                    else:
                        pnew=input("Enter the new value: ")
                        pst="UPDATE PATIENT SET {}='{}' WHERE PId='{}'".format(pcol,pnew,pid)
                        cursor.execute(pst)
                        break
            elif pch=="D":
                pid=input("Enter the patient ID: ")
                pst="DELETE FROM PATIENT WHERE PId='{}'".format(pid)
                cursor.execute(pst)
                        
            elif pch=="E":
                break
            else:
                print("Invalid Choice")
                
                
                    
                
    elif ch==2:
        while True:
            print('-------------------------------------------------------------------------------------------------------------------------')
            print("        To add new doctor record PRESS A")
            print("        To view existing doctor record PRESS B")
            print("        To update existing doctor record PRESS C")
            print("        To delete doctor record PRESS D")
            print("        To go back PRESS E")
            print('-------------------------------------------------------------------------------------------------------------------------')
            print()
            dch=input("Enter your choice: ")
            if dch=='A':
                did=input("Enter the doctor id: ")
                dname=input("Enter the name of the doctor: ")
                dob=input("Enter the date of birth of the doctor in format YYYY-MM-DD: ")
                dage=int(input("Enter the age of the doctor (in years): "))
                dsex=input("Enter the gender of doctor M/F: ")
                doj=input("Enter the date of joining in format YYYY-MM-DD: ")        
                dadd=input("Enter the address of the doctor: ")
                dpno=int(input("Enter the phone number: "))
                dqual=input("Enter the qualification of the doctor: ")
                dspec=input("Enter the specialisation of the doctor: ")
                dsal=int(input("Enter the salary of the doctor: "))
                dst="INSERT INTO DOCTOR(DId,DName,DOB,Age,Sex,DOJ,Address,PhNo,Qualification,Specialisation,Salary) values('{}','{}','{}',{},'{}','{}','{}',{},'{}','{}',{})".format(did,dname,ddob,dage,dsex,doj,dadd,dpno,dqual,dspec,dsal)
                cursor.execute(dst)
                mycon.commit()
                print("Doctor record successfully added")
                dst1="SELECT * FROM DOCTOR WHERE DId='{}'".format(did)
                cursor.execute(dst1)
                data=cursor.fetchone()
                print(data)
            elif dch=='B':
                did=input("Enter the doctor ID: ")
                print("The record is: ")
                dst1="SELECT * FROM DOCTOR WHERE DId='{}'".format(did)
                cursor.execute(dst1)
                data=cursor.fetchone()
                print(data)
            elif dch=='C':
                while True:
                    print('''The available columns are
                                 DId
                                 DName
                                 DOB
                                 Age
                                 Sex
                                 DOJ
                                 Address
                                 PhNo
                                 Qualification
                                 Specialisation
                                 Salary''')
                    did=input("Enter the doctor ID: ")
                    dcol=input("Enter the column name you want to update: ")
                    if dcol in ['Age','PhNo','Salary']:
                        dnew=int(input("Enter the new value: "))
                        dst="UPDATE DOCTOR SET {}={} WHERE DId='{}'".format(dcol,dnew,did)
                        cursor.execute(dst)
                        break
                    else:
                        dnew=input("Enter the new value: ")
                        dst="UPDATE DOCTOR SET {}='{}' WHERE DId='{}'".format(dcol,dnew,did)
                        cursor.execute(dst)
                        break
            elif dch=="D":
                did=input("Enter the doctor ID: ")
                dst="DELETE FROM DOCTOR WHERE DId='{}'".format(did)
                cursor.execute(dst)
                        
            elif dch=="E":
                break
            else:
                print("Invalid Choice")
    elif ch==3:
        while True:
            print('-------------------------------------------------------------------------------------------------------------------------')
            print("        To add new nurse record PRESS A")
            print("        To view existing nurse record PRESS B")
            print("        To update existing nurse record PRESS C")
            print("        To delete nurse record PRESS D")
            print("        To go back PRESS E")
            print('-------------------------------------------------------------------------------------------------------------------------')
            print()
            nch=input("Enter your choice: ")
            if nch=='A':
                nid=input('Enter Nurse ID')
                nname=input('Enter name of nurse')
                ndob=input('Enter date of birth of nurse (YYYY-MM-DD)')
                nage=int(input("Enter nurse age"))
                nsex=input('Enter nurse gender (M/F)')
                ndoj=input('Enter date of joining of nurse')
                nadd=input('Enter nurse address')
                npno=int(input('Enter nurse phone number'))
                nqual=input('Enter nurse qualification')
                nsal=int(input('Enter nurse salary'))
                nst="INSERT INTO NURSE(NId,NName,DOB,Age,Sex,DOJ,Address,PhNo,Qualification,Salary) values('{}','{}','{}',{},'{}','{}','{}',{},'{}',{})".format(nid,nname,ndob,nage,nsex,ndoj,nadd,npno,nqual,nsal)
                cursor.execute(nst)
                mycon.commit()
                print("Nurse record successfully added")
                nst1="SELECT * FROM NURSE WHERE NId='{}'".format(nid)
                cursor.execute(nst1)
                data=cursor.fetchone()
                print(data)
            elif nch=='B':
                nid=input("Enter the nurse ID: ")
                print("The record is: ")
                nst1="SELECT * FROM NURSE WHERE NId='{}'".format(nid)
                cursor.execute(nst1)
                data=cursor.fetchone()
                print(data)
            elif nch=='C':
                while True:
                    print('''The available columns are
                                 NId
                                 NName
                                 DOB
                                 Age
                                 Sex
                                 DOJ
                                 Address
                                 PhNo
                                 Qualification
                                 Salary''')
                    nid=input("Enter the nurse ID: ")
                    ncol=input("Enter the column name you want to update: ")
                    if ncol in ['Age','PhNo','Salary']:
                        nnew=int(input("Enter the new value: "))
                        nst="UPDATE NURSE SET {}={} WHERE NId='{}'".format(ncol,nnew,nid)
                        cursor.execute(nst)
                        break
                    else:
                        nnew=input("Enter the new value: ")
                        nst="UPDATE NURSE SET {}='{}' WHERE NId='{}'".format(ncol,nnew,nid)
                        cursor.execute(nst)
                        break
            elif nch=="D":
                nid=input("Enter the nurse ID: ")
                nst="DELETE FROM DOCTOR WHERE NId='{}'".format(nid)
                cursor.execute(nst)
                        
            elif nch=="E":
                break
            else:
                print("Invalid Choice")
                         
                    
 
    elif ch==4:
        while True:
            print('-------------------------------------------------------------------------------------------------------------------------')
            print("        To add patient payment record PRESS A")
            print("        To view bill PRESS B")
            print("        To delete patient payment record PRESS C")
            print("        To go back PRESS D")
            print('-------------------------------------------------------------------------------------------------------------------------')
            print()
            pmch=input("Enter your choice: ")
            if pmch=='A':
                pid=input("Enter patient id")
                pname=input("Enter patient name")
                ad_fee=int(input("Enter admission fee"))
                room_fee=int(input("Enter room fee"))
                doc_fee=int(input("Entr doctor fee"))
                ph_fee=int(input("Enter pharmacy fee"))
                icu_fee=int(input("Enter ICU fee"))
                op_fee=int(input("Enter operation fee"))
                tot_fee=ad_fee+room_fee+doc_fee+ph_fee+icu_fee+op_fee
                pmst="INSERT INTO PAYMENT(PId,PName,Admission_Fee,Room_Charges,Doctor_Consultation_Fees,Pharmacy,ICU,Operation,Total_Fees) values('{}','{}',{},{},{},{},{},{},{})".format(pid,pname,ad_fee,room_fee,doc_fee,ph_fee,icu_fee,op_fee,tot_fee)
                cursor.execute(pmst)
                mycon.commit()
                print("Patient payment record successfully added")
                pmst1="SELECT * FROM Payment WHERE PId='{}'".format(pid)
                cursor.execute(pmst1)
                data=cursor.fetchone()
                print(data)
            elif pmch=='B':
                pid=input("Enter the patient ID: ")
                print("The record is: ")
                pmst1="SELECT * FROM PAYMENT WHERE PId='{}'".format(pid)
                cursor.execute(pmst1)
                data=cursor.fetchone()
                print(data)
            elif nch=="C":
                pid=input("Enter the patient ID: ")
                pmst="DELETE FROM PAYMENT WHERE PId='{}'".format(pid)
                cursor.execute(pmst)
           
            elif pmch=='D':
                break
            else:
                print("INVALID CHOICE!")
                                     
    elif ch==5:
        print("Thank You!")
        break
    else:
        print("INVALID CHOICE!")
mycon.close()

        
        
        
        


