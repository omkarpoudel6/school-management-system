from django.shortcuts import render
from .form import Student_Info,ViewInfo,Result,ResultForm,PaymentForm
from .models import Student_info,Results,Bill,Transaction
import random

# Create your views here.

def get_student_id():
    id=random.randint(1000,9999)
    obj=Student_info.objects.filter(student_id=id).first()
    if obj==None:
        return id
    else:
        get_student_id()

def Home(request):
    return render(request,'home.html')

def AddStudent(request):
    if request.method=="POST":
        form=Student_Info(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data['firstname']
            middlename = form.cleaned_data['middlename']
            lastname = form.cleaned_data['lastname']
            age = form.cleaned_data['age']
            grade = form.cleaned_data['grade']
            fathername = form.cleaned_data['fathername']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            #image=form.cleaned_data['image']
            if age<0 or age>50 or grade<0 or grade>10 or len(str(phone))<0 or len(str(phone))>10:
                context = {'information': 'Enter Valid Information'}
                return render(request, 'addstudent.html', context)
            else:
                if grade==1:
                    admission=3000
                elif grade==2:
                    admission=4000
                elif grade==3:
                    admission=5000
                elif grade==4:
                    admission=6000
                elif grade==5:
                    admission=7000
                elif grade==6:
                    admission=8000
                elif grade==7:
                    admission=9000
                elif grade==8:
                    admission=10000
                elif grade==9:
                    admission=11000
                elif grade==10:
                    admission=12000
                fee=0
                student_id=get_student_id()
                obj=Student_info(student_id=student_id,firstname=firstname,middlename=middlename,lastname=lastname,age=age,grade=grade,fathername=fathername,phone=phone,address=address)
                obj.save()
                obj2=Bill(student_id=student_id,admission=admission,baisakh=fee,jestha=fee,ashad=fee,shrawan=fee,bhadra=fee,aswin=fee,kartik=fee,mangsir=fee,poush=fee,magh=fee,falgun=fee,chaitra=fee)
                obj2.save()
                context={'information':'Student Added Sucessfully!!',
                         'student_id':student_id}

                return render(request, 'addstudent.html', context)
        else:
            context={'information':'Enter Valid Information'}
            return render(request,'addstudent.html',context)
    else:
        return render(request, 'addstudent.html')

def AddStudentResult(request):
    if request.method=="POST":
        form=Result(request.POST)
        if form.is_valid():
            student_id=form.cleaned_data['student_id']
            term=form.cleaned_data['term']
            grade=form.cleaned_data['grade']
            if term>0 and term<=4:
                obj=Student_info.objects.filter(student_id=student_id).first()
                if obj:
                    obj=Results.objects.filter(student_id=student_id, term=term).first()
                    if obj==None:
                        count=500
                        tpm=200
                        e=form.cleaned_data['english']
                        n = form.cleaned_data['nepali']
                        m = form.cleaned_data['math']
                        s = form.cleaned_data['science']
                        so = form.cleaned_data['social']

                        ehp = form.cleaned_data['ehp']
                        if ehp==None:
                            ehp=0
                        else:
                            if grade>0 and grade<8:
                                count = count + 50
                                tpm=tpm+20
                            elif grade>8 and grade<=10:
                                count = count + 100
                                tpm = tpm + 40

                        opti = form.cleaned_data['optionali']
                        if opti==None:
                            opti=0
                        else:
                            count=count+100
                            tpm = tpm + 40

                        optii = form.cleaned_data['optionalii']
                        if optii==None:
                            optii=0
                        else:
                            count = count + 100
                            tpm = tpm + 40

                        g = form.cleaned_data['grammar']
                        if g==None:
                            g=0
                        else:
                            count = count + 50
                            tpm = tpm + 20

                        optmath = form.cleaned_data['optionalmath']
                        if optmath==None:
                            optmath=0
                        else:
                            count = count + 50
                            tpm = tpm + 20

                        com = form.cleaned_data['computer']
                        if com==None:
                            com=0
                        else:
                            count = count + 50
                            tpm = tpm + 20

                        gk = form.cleaned_data['gk']
                        if gk==None:
                            gk=0
                        else:
                            count = count + 50
                            tpm = tpm + 20

                        draw = form.cleaned_data['drawing']
                        if draw==None:
                            draw=0
                        else:
                            count = count + 50
                            tpm = tpm + 20

                        total=e+n+m+s+so+ehp+opti+optii+g+optmath+com+gk+draw
                        percentage=(total/count)*100

                        if percentage>=90 and percentage <100:
                            division="A+"
                        elif percentage>=80 and percentage <90:
                            division="A"
                        elif percentage >=70 and percentage <80:
                            division="B+"
                        elif percentage >=60 and percentage<70:
                            division="B"
                        elif percentage >=50 and percentage <60:
                            division="C+"
                        elif percentage >=40 and percentage <50:
                            division="C"
                        else:
                            division="Fail"

                        print(percentage)
                        print(division)

                        obj=Results(student_id=student_id,term=term,grade=grade,english=e,nepali=n,math=m,science=s,social=so,ehp=ehp,optionali=opti,
                                      optionalii=optii,grammar=g,optionalmath=optmath,computer=com,gk=gk,drawing=draw,totalfullmark=count,totalpassmark=tpm,
                                      marksobtained=total,percentage=percentage,division=division)
                        obj.save()

                        context = {'information': 'Result Added Sucessfully!!!'}
                        return render(request, 'addstudentresults.html', context)
                    else:
                        context = {'information': 'Result Already Exists!!!'}
                        return render(request, 'addstudentresults.html', context)

                else:
                    context={'information':'No Student Found'}
                    return render(request,'addstudentresults.html',context)

                print("Form submission sucessfull!!!")
            else:
                context = {'information': 'Enter Valid Term'}
                return render(request, 'addstudentresults.html', context)
        else:
            context = {'information': 'Something Went Wrong'}
            return render(request, 'addstudentresults.html',context)
    else:
        return render(request,'addstudentresults.html')

def ViewResult(request):
    if request.method=="POST":
        form=ResultForm(request.POST)
        if form.is_valid():
            id=form.cleaned_data['student_id']
            term=form.cleaned_data['term']
            obj=Results.objects.filter(student_id=id, term=term).first()
            if obj:
                info=Student_info.objects.filter(student_id=id).first()
                context = {'information': 'Result Displayed',
                           'result':obj,
                           'studentinfo':info}
                return render(request, 'viewstudentresults.html', context)
            else:
                context = {'information': 'Result Doesnot Exists'}
                return render(request, 'viewstudentresults.html', context)

        else:
            context={'information':'Something Went Wrong'}
            return render(request, 'viewstudentresults.html',context)
    else:
        return render(request, 'viewstudentresults.html')

def StudentInfo(request):
    if request.method=="POST":
        id=ViewInfo(request.POST)
        if id.is_valid():
            student_id=id.cleaned_data['student_id']
            print(student_id)
            obj=Student_info.objects.filter(student_id=student_id)
            if obj:
                context={'info':obj}
                return render(request, 'viewstudentinfo.html',context)
            else:
                context={'error':'No Students Available!!'}
                return render(request, 'viewstudentinfo.html', context)
        else:
            print("Something went wrong")
        return render(request, 'viewstudentinfo.html')
    else:
        return render(request,'viewstudentinfo.html')

def ViewBillStatus(request):
    if request.method=="POST":
        form=ViewInfo(request.POST)
        if form.is_valid():
            id=form.cleaned_data['student_id']
            obj=Bill.objects.filter(student_id=id).first()
            if obj:
                studentinfo=Student_info.objects.filter(student_id=id).first()
                context={'billinfo':obj,
                        'studentinfo':studentinfo}
                return render(request, 'paybill.html', context)
            else:
                context = {'information': 'No Student Found'}
                return render(request, 'paybill.html', context)
        else:
            context = {'information': 'Form Invalid'}
            return render(request, 'paybill.html', context)
    else:
        return render(request, 'paybill.html')

def BillPayment(request):
    if request.method=="POST":
        form=PaymentForm(request.POST)
        #print(form)
        if form.is_valid():
            student_id=form.cleaned_data['student_id']
            grade=form.cleaned_data['grade']
            month=form.cleaned_data['month']
            amount=form.cleaned_data['amount']
            remarks=form.cleaned_data['remarks']
            obj=Bill.objects.filter(student_id=student_id).first()
            if obj:
                if month=='baisakh':
                    if obj.baisakh==0:
                        obj2=Bill.objects.get(student_id=student_id)
                        obj2.baisakh=amount
                        obj2.save()
                        transaction = Transaction(sid=student_id, amount=amount, remarks=remarks)
                        transaction.save()
                        context={'information':'Fee For Baisakh Paid'}
                        return render(request, 'billpayment.html', context)
                    else:
                        context={'information':'Fee Already Paid For Baisakh'}
                        return render(request, 'billpayment.html', context)
                elif month=='jestha':
                    if obj.jestha==0:
                        obj2 = Bill.objects.get(student_id=student_id)
                        obj2.jestha = amount
                        obj2.save()
                        transaction=Transaction(sid=student_id,amount=amount,remarks=remarks)
                        transaction.save()
                        context={'information':'Fee For Jestha Paid'}
                        return render(request, 'billpayment.html', context)
                    else:
                        context={'information':'Fee Already Paid For Jestha'}
                        return render(request, 'billpayment.html', context)
                elif month=='ashad':
                    if obj.ashad==0:
                        obj2 = Bill.objects.get(student_id=student_id)
                        obj2.ashad = amount
                        obj2.save()
                        transaction = Transaction(sid=student_id, amount=amount, remarks=remarks)
                        transaction.save()
                        context={'information':'Fee For Ashad Paid'}
                        return render(request, 'billpayment.html', context)
                    else:
                        context={'information':'Fee Already Paid For Ashad'}
                        return render(request, 'billpayment.html', context)
                elif month=='shrawan':
                    if obj.shrawan==0:
                        obj2 = Bill.objects.get(student_id=student_id)
                        obj2.shrawan = amount
                        obj2.save()
                        transaction = Transaction(sid=student_id, amount=amount, remarks=remarks)
                        transaction.save()
                        context={'information':'Fee For Shrawan Paid'}
                        return render(request, 'billpayment.html', context)
                    else:
                        context={'information':'Fee Already Paid For Shrawan'}
                        return render(request, 'billpayment.html', context)
                elif month=='bhadra':
                    if obj.bhadra==0:
                        obj2 = Bill.objects.get(student_id=student_id)
                        obj2.bhadra = amount
                        obj2.save()
                        transaction = Transaction(sid=student_id, amount=amount, remarks=remarks)
                        transaction.save()
                        context={'information':'Fee For Bhadra Paid'}
                        return render(request, 'billpayment.html', context)
                    else:
                        context={'information':'Fee Already Paid For Bhadra'}
                        return render(request, 'billpayment.html', context)
                elif month=='aswin':
                    if obj.aswin==0:
                        obj2 = Bill.objects.get(student_id=student_id)
                        obj2.aswin = amount
                        obj2.save()
                        transaction = Transaction(sid=student_id, amount=amount, remarks=remarks)
                        transaction.save()
                        context={'information':'Fee For Aswin Paid'}
                        return render(request, 'billpayment.html', context)
                    else:
                        context={'information':'Fee Already Paid For Aswin'}
                        return render(request, 'billpayment.html', context)
                elif month=='kartik':
                    if obj.kartik==0:
                        obj2 = Bill.objects.get(student_id=student_id)
                        obj2.kartik = amount
                        obj2.save()
                        transaction = Transaction(sid=student_id, amount=amount, remarks=remarks)
                        transaction.save()
                        context={'information':'Fee For Kartik Paid'}
                        return render(request, 'billpayment.html', context)
                    else:
                        context={'information':'Fee Already Paid For Kartik'}
                        return render(request, 'billpayment.html', context)
                elif month=='mangsir':
                    if obj.mangsir==0:
                        obj2 = Bill.objects.get(student_id=student_id)
                        obj2.mangsir = amount
                        obj2.save()
                        transaction = Transaction(sid=student_id, amount=amount, remarks=remarks)
                        transaction.save()
                        context={'information':'Fee For Mangsir Paid'}
                        return render(request, 'billpayment.html', context)
                    else:
                        context={'information':'Fee Already Paid For Mangsir'}
                        return render(request, 'billpayment.html', context)
                elif month=='poush':
                    if obj.poush==0:
                        obj2 = Bill.objects.get(student_id=student_id)
                        obj2.poush = amount
                        obj2.save()
                        transaction = Transaction(sid=student_id, amount=amount, remarks=remarks)
                        transaction.save()
                        context={'information':'Fee For poush paid'}
                        return render(request, 'billpayment.html', context)
                    else:
                        context={'information':'Fee Already Paid For Poush'}
                        return render(request, 'billpayment.html', context)
                elif month=='magh':
                    if obj.magh==0:
                        obj2 = Bill.objects.get(student_id=student_id)
                        obj2.magh = amount
                        obj2.save()
                        transaction = Transaction(sid=student_id, amount=amount, remarks=remarks)
                        transaction.save()
                        context={'information':'Fee For Magh Paid'}
                        return render(request, 'billpayment.html', context)
                    else:
                        context={'information':'Fee Already Paid For Magh'}
                        return render(request, 'billpayment.html', context)
                elif month=='falgun':
                    if obj.falgun==0:
                        obj2 = Bill.objects.get(student_id=student_id)
                        obj2.falgun = amount
                        obj2.save()
                        transaction = Transaction(sid=student_id, amount=amount, remarks=remarks)
                        transaction.save()
                        context={'information':'Fee For Falgun Paid'}
                        return render(request, 'billpayment.html', context)
                    else:
                        context={'information':'Fee Already Paid For Falgun'}
                        return render(request, 'billpayment.html', context)
                elif month=='chaitra':
                    if obj.chaitra==0:
                        obj2 = Bill.objects.get(student_id=student_id)
                        obj2.chaitra = amount
                        obj2.save()
                        transaction = Transaction(sid=student_id, amount=amount, remarks=remarks)
                        transaction.save()
                        context={'information':'Fee For Chaitra Paid'}
                        return render(request, 'billpayment.html', context)
                    else:
                        context={'information':'Fee Already Paid For Chaitra'}
                        return render(request, 'billpayment.html', context)
                else:
                    context = {'information': 'Enter Valid Month'}
                    return render(request, 'billpayment.html', context)
            else:
                context={'information':'Student not Found'}
                return render(request,'billpayment.html',context)
        else:
            context = {'information': 'Payment unsucessfull'}
            return render(request, 'billpayment.html', context)
    else:
        return render(request,'billpayment.html')

def Transactions(request):
    if request.method=="POST":
        form=ViewInfo(request.POST)
        if form.is_valid():
            id=form.cleaned_data['student_id']
            obj=Transaction.objects.filter(sid=id)
            if obj:
                obj2=Student_info.objects.filter(student_id=id).first()
                context={'transaction':obj,
                         'studentinfo':obj2}
                return render(request,'transaction.html',context)
            else:
                context={'information':'No record Found'}
                return render(request, 'transaction.html', context)
            print("Student id accepted")
        else:
            print("Invalid student id")
    return render(request,'transaction.html')