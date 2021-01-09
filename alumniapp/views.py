from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import pymysql
import webbrowser
import json

db=pymysql.connect("localhost","root","","dbalumniweb")
c=db.cursor()

def sendsms(ph,msg):

    sendToPhoneNumber= ph
    url = "http://sms.mdsmedia.in/http-api.php?username=7000183&password=LCCCOK123&senderid=LCCCOK&route=23&number="+sendToPhoneNumber+"&message="+msg
    # contents = urllib.request.urlopen(url)
    webbrowser.open(url)

######################################################################
#                           LOAD INDEX PAGE
######################################################################
def index(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    return render(request,"index.html")
######################################################################
#                           LOGIN
######################################################################
def login(request):
    """ 
        The function to load login
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        email=request.POST.get("txtEmail")
        pwd=request.POST.get("txtPassword")
        s="select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            s="select * from tbllogin where username='"+email+"'"
            c.execute(s)
            i=c.fetchone()
            if(i[1]==pwd):
                request.session['email'] = email
                if(i[3]=="1"):
                    if(i[2]=="admin"):
                        return HttpResponseRedirect("/adminhome")
                    elif(i[2]=="eventmanager"):
                        return HttpResponseRedirect("/emhome")
                    elif(i[2]=="alumni"):
                        return HttpResponseRedirect("/alumnihome")
                elif(i[3]=="inactive"):
                    msg="Your registration is incomplete. Please register"
                else:
                    msg="You are not authenticated to login"
            else:
                msg="Incorrect password"
        else:
            msg="User doesnt exist"
    return render(request,"login.html",{"msg":msg})
######################################################################
#                           REGISTRATION
######################################################################
def registration(request):
    """ 
        The function to load registration
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        yop=request.POST["yop"]
        name=request.POST["txtName"]
        gender=request.POST["txtGender"]
        dob=request.POST["txtDob"]
        address=request.POST["txtAddress"]
        phone=request.POST["txtContact"]
        qual=request.POST["txtQual"]
        email=request.POST["txtEmail"]
        fname=request.FILES["txtFile"]
        fs=FileSystemStorage()
        filename=fs.save(fname.name,fname)
        uploaded_file_url=fs.url(filename)
        rec=request.POST["rec"]
        company=request.POST["txtcompany"]
        desig=request.POST["txtdesig"]
        whatsapp=request.POST["txtwhatsapp"]
        currentcompany=request.POST["txtcurrentcompany"]
        currentdesig=request.POST["txtcurrentdesignation"]
        martial=request.POST["txtstatus"]
        spousename=request.POST["txtspousename"]
        spousecompany=request.POST["txtspousecompanyname"]
        spousedesig=request.POST["txtspousedesignation"]
        s="select alumniid from tblbatchdetails where name='"+name+"' and yop='"+yop+"'"
        c.execute(s)
        i=c.fetchone()
        alumniid=i[0]
        
        s="insert into tblalumni(alumniid,alumniname,gender,dob,address,phone,qual,image,email,recruited,company,designation,whatsapp,currentcompany,currentdesig,martialstatus,spousename,spousecompany,spousedesig) values('"+alumniid+"','"+name+"','"+gender+"','"+dob+"','"+address+"','"+phone+"','"+qual+"','"+uploaded_file_url+"','"+email+"','"+rec+"','"+company+"','"+desig+"','"+whatsapp+"','"+currentcompany+"','"+currentdesig+"','"+martial+"','"+spousename+"','"+spousecompany+"','"+spousedesig+"')"
        try:
              
                c.execute(s)
                db.commit()
        except:
                msg="Sorry some error occured"
        else:
                s="update tbllogin set status='0' where username='"+alumniid+"'"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry some error occured"
                else:
                    msg="Registration successfull"

            
    s="select distinct yop from tblbatchdetails"
    c.execute(s)
    data=c.fetchall()
    return render(request,"registration.html",{"msg":msg,"batch":data})
def getnames(request):
    print("Hi")
    y=request.GET.get("yop")
    print(y)
    s="select name from tblbatchdetails where yop='"+str(y)+"'"
    c.execute(s)
    data=c.fetchall()
    print(data)
    jsonStr = json.dumps(data)
    print(jsonStr)
    return HttpResponse(jsonStr)
######################################################################
#                                                                    #
#                                                                    #
#                           ADMIN                                    #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD ADMIN PAGE
######################################################################
def adminhome(request):
    """ 
        The function to load admin page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    return render(request,"adminhome.html")
######################################################################
#                           ADMIN BATCH
######################################################################
def adminbatch(request):
    if(request.POST):
        i=""
        import pandas as pd
        xl = pd.read_excel(request.FILES["txtfile"])
        df=pd.DataFrame(xl,columns=['Name','YOP','Regno','Contact'])
        for row in df.itertuples():
            s="select count(*) from tblbatchdetails where name='"+str(row.Name)+"' and yop='"+str(row.YOP)+"' and contact='"+str(row.Contact)+"' "
            c.execute(s)
            i=c.fetchone()
            if(i[0]==0):
                q="select count(*) from tblbatchdetails"
                c.execute(q)
                cn=c.fetchone()
                regno="ALMN"+str(cn[0]+1)
                c.execute("insert into tblbatchdetails(name,yop,regno,alumniid,contact) values('"+str(row.Name)+"','"+str(row.YOP)+"','"+str(row.Regno)+"','"+regno+"','"+str(row.Contact)+"')")
                c.execute("insert into tbllogin(username,password,utype,status) values('"+str(regno)+"','"+str(row.Contact)+"','alumni','inactive')")
                msg="You have been added to the alumni group. You can confirm your registration with Username:"+str(regno)+" and Password:"+str(row.Contact)
                sendsms(str(row.Contact),msg)
            db.commit()
    s="select * from tblbatchdetails "
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminbatch.html",{"data":data})

def loadbatch():
    """ 
        The function to load batch 
        -----------------------------------------------
        Parameters: 
            Nill
          
        Returns: 
            Batch data
    """
    s="select * from tblbatch where status='1'"
    c.execute(s)
    data=c.fetchall()
    return data
######################################################################
#                          ADMIN ALUMNI
######################################################################
def adminalumni(request):
    """ 
        The function to approve alumni
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select tblalumni.* from tblalumni where tblalumni.alumniid in(select username from tbllogin where status='0')"
    c.execute(s)
    data=c.fetchall()
    s="select tblalumni.* from tblalumni where tblalumni.alumniid in(select username from tbllogin where status='1')"
    c.execute(s)
    data1=c.fetchall()
    return render(request,"adminalumni.html",{"data":data,"data1":data1})
######################################################################
#                          ADMIN UPDATE ALUMNI
######################################################################
def adminupdatealumni(request):
    """ 
        The function to approve alumni
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    if(request.GET):
        email=request.GET.get("id")
        status=request.GET.get("status")
        s="update tbllogin set status='"+status+"' where username='"+email+"'"
        c.execute(s)
        db.commit()
        return HttpResponseRedirect("/adminalumni")
######################################################################
#                           ADMIN EVENT
######################################################################
def adminevent(request):
    """ 
        The function to load admin event page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    
    if(request.POST):
        name=request.POST["txtEvent"]
        date=request.POST["txtDate"]
        time=request.POST["txtTime"]
        venue=request.POST["txtVenue"]
        
        desc=request.POST["txtDesc"]
        ratea=request.POST["ratea"]
        rateb=request.POST["rateb"]
        s="insert into tblevent(eventname,eventdate,eventtime,eventvenue,description,adultrate,otherrate,status) values('"+name+"','"+date+"','"+time+"','"+venue+"','"+desc+"','"+ratea+"','"+rateb+"','1')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Event updated"
    s="select *  from tblevent where status=1 order by eventid desc"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminevent.html",{"data":data,"msg":msg})
######################################################################
#                           ADMIN EVENT UPDATE
######################################################################
def adminupdateevent(request):
    """ 
        The function to load admin event page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    id=request.GET.get("id")
    if(request.POST):
        name=request.POST["txtEvent"]
        date=request.POST["txtDate"]
        time=request.POST["txtTime"]
        venue=request.POST["txtVenue"]
        
        desc=request.POST["txtDesc"]
        ratea=request.POST["ratea"]
        rateb=request.POST["rateb"]
        # import datetime
        # edate=datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S.%f')
        # print(edate)
        s="update tblevent set eventname='"+name+"',eventdate='"+date+"',eventtime='"+time+"',eventvenue='"+venue+"',description='"+desc+"',adultrate='"+ratea+"',otherrate='"+rateb+"' where eventid='"+id+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Event updated"
            return HttpResponseRedirect("/adminevent")
    s="select *  from tblevent where eventid='"+id+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminupdateevent.html",{"data":data,"msg":msg})
def admindeleteevent(request):
    id=request.GET.get("id")
    s="update tblevent set status=0 where eventid='"+id+"'"
    print(s)
    try:
            c.execute(s)
            db.commit()
    except:
            msg="Sorry some error occured"
    else:
            msg="Event deleted"
            return HttpResponseRedirect("/adminevent")
######################################################################
#                           ADMIN EVENT
######################################################################
def adminemanager(request):
    """ 
        The function to load admin event manager page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    
    if(request.POST):
        name=request.POST["txtName"]
        address=request.POST["txtAddress"]
        contact=request.POST["txtContact"]
        email=request.POST["txtEmail"]
        event=request.POST["event"]
        s="select count(*) from tbllogin where username='"+email+"' and status='1'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Email already registered"
        else:
            s="insert into tbleventmanager(managername,address,contact,email,eventid,status) values('"+name+"','"+address+"','"+contact+"','"+email+"','"+event+"','1')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                s="insert into tbllogin(username,password,utype,status) values('"+email+"','"+email+"','eventmanager','1')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg="Sorry some error occured"
                else:
                    msg="Event manager registered"
    s="select *  from tbleventmanager where email in(select username from tbllogin where status='1')"
    c.execute(s)
    data=c.fetchall()
    s="select *  from tblevent where eventdate>(select sysdate()) and eventid not in(select eventid from tbleventmanager)"
    c.execute(s)
    event=c.fetchall()
    return render(request,"adminemanager.html",{"data":data,"msg":msg,"event":event})
######################################################################
#                                                                    #
#                                                                    #
#                           EVENT MANAGER                            #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD EVENT MANAGER PAGE
######################################################################
def emhome(request):
    """ 
        The function to load event manager page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tbleventmanager.*,tblevent.eventname from tbleventmanager,tblevent where tbleventmanager.email='"+email+"' and tblevent.eventid=tbleventmanager.eventid"
    c.execute(s)
    data=c.fetchall()
    return render(request,"emhome.html",{"data":data})
######################################################################
#                           EM GALLERY
######################################################################
def emgallery(request):
    """ 
        The function to change password of event manager
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        email=request.session["email"]
        s="select eventid from tbleventmanager where email='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        event=i[0]
        desc=request.POST["txtDesc"]

        img=request.FILES["txtFile"]
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        uploaded_file_url=fs.url(filename)

        s="insert into tblimage (eventid,image,description) values('"+str(event)+"','"+uploaded_file_url+"','"+desc+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Data updated successfully"
        
    return render(request,"emgallery.html",{"msg":msg})
######################################################################
#                           EM EVENT
######################################################################
def emevent(request):
    """ 
        The function to add events
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    s="select eventid from tbleventmanager where email='"+email+"'"
    c.execute(s)
    i=c.fetchone()
    event=i[0]
    if(request.POST):
        
        pgm=request.POST["txtPgm"]
        time=request.POST["txtTime"]

        

        s="insert into tbleventprograms (eventid,pgm,pgmTime) values('"+str(event)+"','"+pgm+"','"+time+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Data updated successfully"
    s="select * from tbleventprograms where eventId='"+str(event)+"' order by pgmTime"
    c.execute(s)
    data=c.fetchall()
    return render(request,"emevent.html",{"msg":msg,"data":data})
######################################################################
#                           EM EVENT DELETE
######################################################################
def emeventdelete(request):
    """ 
        The function to add events
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    if(request.GET):
        eid=request.GET.get("id")
        s="delete from tbleventprograms where pId='"+str(eid)+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            pass
        else:
            return HttpResponseRedirect("/emevent")
    return render(request,"emevent.html")
######################################################################
#                           CHANGE PASSWORD
######################################################################
def emchangepwd(request):
    """ 
        The function to change password of event manager
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        email=request.session["email"]
        current=request.POST["txtCPassword"]
        new=request.POST["txtNPassword"]
        s="select * from tbllogin where username='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[1]==current):
            s="update tbllogin set password='"+new+"' where username='"+email+"'"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Data updated successfully"
        else:
            msg="Incorrect password"
    return render(request,"emanagerchangepwd.html",{"msg":msg})
######################################################################
#                                                                    #
#                                                                    #
#                           ALUMNI                                   #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD ALUMNI PAGE
######################################################################
def alumnihome(request):
    """ 
        The function to load alumni home page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    s="select tblalumni.* from tblalumni where tblalumni.alumniid='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    if(request.POST):
        name=request.POST["txtName"]
        gender=request.POST["txtGender"]
        dob=request.POST["txtDob"]
        address=request.POST["txtAddress"]
        phone=request.POST["txtContact"]
        qual=request.POST["txtQual"]
        eemail=request.POST["txtEmail"]
        whatsapp=request.POST["txtwhatsapp"]
        currentcompany=request.POST["txtcurrentcompanyname"]
        currentdesig=request.POST["txtcurrentdesignation"]
        martial=request.POST["txtstatus"]
        spousename=request.POST["txtspousename"]
        spousecompany=request.POST["txtspousecompanyname"]
        spousedesig=request.POST["txtspousedesignation"]
        s="update tblalumni set alumniname='"+name+"', gender='"+gender+"',dob='"+dob+"',address='"+address+"',phone='"+phone+"',qual='"+qual+"',email='"+eemail+"',whatsapp='"+whatsapp+"',currentcompany='"+currentcompany+"',currentdesig='"+currentdesig+"',martialstatus='"+martial+"',spousename='"+spousename+"',spousecompany='"+spousecompany+"',spousedesig='"+spousedesig+"' where alumniid='"+email+"'"
        print(s)
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Profile updated"
    return render(request,"alumnihome.html",{"data":data,"msg":msg})
######################################################################
#                           ALUMNI PROFILE
######################################################################
def alumniprofile(request):
    """ 
        The function to load alumni profile page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    if(request.POST):
        designation=request.POST["txtDesignation"]
        jdate=request.POST["txtJdate"]
        ldate=request.POST["txtLdate"]
        fun=request.POST["txtFun"]
        place=request.POST["txtPlace"]
        web=request.POST["txtUrl"]
        s="insert into tblprofileinfo(alumniemail,designation,joiningdate,leavingdate,functionalarea,place,orgwebsite) values('"+email+"','"+designation+"','"+jdate+"','"+ldate+"','"+fun+"','"+place+"','"+web+"')"
        print(s)
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Profile updated"
    s="select * from tblprofileinfo where alumniemail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"alumniprofile.html",{"data":data,"msg":msg})
######################################################################
#                           ALUMNI EVENTS
######################################################################
def alumnievent(request):
    """ 
        The function to load alumni event page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
   
    s="select * from tblevent where eventdate>(select sysdate()) and status='1'"
    print(s)
    c.execute(s)
    data=c.fetchall()
    return render(request,"alumnievent.html",{"data":data})
######################################################################
#                       ALUMNI EVENT PROGRAMS
######################################################################
def alumnieventpgm(request):
    """ 
        The function to load alumni event programs page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    if(request.GET):
        eid=request.GET.get("id")
        s="select * from tbleventprograms where eventId='"+eid+"'"
        c.execute(s)
        data=c.fetchall()
    return render(request,"alumnieventpgm.html",{"data":data})
    ######################################################################
#                           ALUMNI VACCANCY
######################################################################
def alumnivaccancy(request):
    """ 
        The function to load vaccancy of alumni
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    if(request.POST):
        vaccancy=request.POST["txtVaccancy"]
        company=request.POST["txtCompany"]
        role=request.POST["txtRole"]
        qual=request.POST["txtQual"]
        exp=request.POST["txtExp"]
        place=request.POST["txtPlace"]
        desc=request.POST["txtDesc"]
        web=request.POST["txtUrl"]
        s="insert into tblvaccancy(alumniEmail,vacName,company,role,qual,exp,place,descrip,link) values('"+email+"','"+vaccancy+"','"+company+"','"+role+"','"+qual+"','"+exp+"','"+place+"','"+desc+"','"+web+"')"
       
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Vaccancy updated"
    s="select * from tblvaccancy where alumniEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"alumnivaccancy.html",{"data":data,"msg":msg})
######################################################################
#                           ALUMNI OTHER VACCANCY
######################################################################
def alumniovaccancy(request):
    """ 
        The function to load vaccancy of alumni
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    
    s="select * from tblvaccancy where alumniEmail<>'"+email+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"alumniothervacc.html",{"data":data,"msg":msg})



######################################################################
#                           ALUMNI CHAT
######################################################################
def alumnichat(request):
    """ 
        The function to load chat
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    if(request.POST):
        email=request.session["email"]
        s="select alumniid from tblalumni where email='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        aid=i[0]
        msg=request.POST["txtmsg"]
        s="insert into tblchatmaster (alumniid,msg) values('"+str(aid)+"','"+msg+"')"
        c.execute(s)
        db.commit()
    s="select tblalumni.alumniname,tblchatmaster.msg from tblalumni,tblchatmaster where tblalumni.alumniid=tblchatmaster.alumniid order by tblchatmaster.chatid desc"
    c.execute(s)
    data=c.fetchall()
    return render(request,"alumnichat.html",{"data":data})
def eventregistration(request):
    msg=""
    if(request.POST):
        email=request.session["email"]
        eventid=request.GET.get("eventid")
        adultrate=request.GET.get("adultrate")
        otherrate=request.GET.get("otherrate")
        
        ar=request.POST.get("ar")
        otr=request.POST.get("otr")
        
        totalprice=int(adultrate)*int(ar)+int(otherrate)*int(otr)
        
        

        s="insert into tbl_eventregistration (eventid,aemail,ar,otr,totalprice,status) values('"+str(eventid)+"','"+str(email)+"','"+str(ar)+"','"+str(otr)+"','"+str(totalprice)+"','registered')"
            
        try:
            c.execute(s)
               
            db.commit()
        except:
            s="Some error occured"
        else:
            s=c.execute("select max(id) from tbl_eventregistration")
            i=c.fetchone()
            return HttpResponseRedirect("/alumnipayment?regid="+str(i[0]))
                         
        
    return render(request,"eventregistration.html",{"msg":msg})
def selecteventregistration():
    s="select totalprice from tbl_eventregistration where id in(select max(id) from tbl_eventregistration)"
    c.execute(s)
    data=c.fetchone()
    print(data[0])
    return data[0]
def alumnipayment(request):
    s=""
    msg=""
    if(request.POST):
        regid=request.GET.get("regid")
        a=request.POST.get("name")
        b=request.POST.get("cnumber")
        ed=request.POST.get("exdate")
        d=request.POST.get("cvv")
        totalprice=request.POST.get("totalprice")
        s=c.execute("insert into tbl_payment(regid,name,cnumber,exdate,cvv,totalprice,status) values('"+str(regid)+"','"+str(a)+"','"+str(b)+"','"+str(ed)+"','"+str(d)+"','"+str(totalprice)+"','paid')")      
        msg="Payment Successfull"
        db.commit()
        return HttpResponseRedirect("/alumnihome")
    s="select totalprice from tbl_eventregistration where id in(select max(id) from tbl_eventregistration)"
    c.execute(s)
    data=c.fetchone()
    reg=data[0]
    return render(request,"alumnipayment.html",{"reg":reg,"msg":msg})
def batchreport(request):
    data=""
    c.execute("select * from tblbatchdetails")
    cat=c.fetchall()
    if(request.POST):
        z=request.POST["year"]
        c.execute("select * from tblbatchdetails where yop='"+z+"' ")
        data=c.fetchall()        
    return render (request,"batchreport.html",{"data":data,"cat":cat})
def alumnireport(request):
    data=""
    c.execute("select * from tblbatchdetails where alumniid IN (select alumniid from tblalumni)")
    data=c.fetchall() 
    return render(request,"alumnireport.html",{"data":data})
def unregisteredreport(request):
    data=""
    c.execute("select * from tblbatchdetails where alumniid NOT IN (select alumniid from tblalumni)")
    data=c.fetchall() 
    return render(request,"unregisteredreport.html",{"data":data})
def eventreport(request):
    data=""
    c.execute("select * from tblevent")
    data=c.fetchall() 
    return render(request,"eventreport.html",{"data":data})
def meetreport(request):
    data=""
    c.execute("select tbl_eventregistration.aemail,tblevent.eventname,tblevent.eventdate,tblevent.eventtime,tbl_eventregistration.ar,tbl_eventregistration.otr,tbl_eventregistration.totalprice from tblevent,tbl_eventregistration where tblevent.eventid=tbl_eventregistration.eventid")
    data=c.fetchall() 
    return render(request,"meetreport.html",{"data":data})
    
def alumnibatchview(request):
    data=""
    c.execute("select * from tblbatchdetails")
    cat=c.fetchall()
    if(request.POST):
        z=request.POST["year"]
        c.execute("select * from tblalumni where alumniid in (select alumniid from tblbatchdetails where yop='"+z+"') ")
        data=c.fetchall()       
    return render(request,"alumnibatchview.html",{"data":data,"cat":cat})