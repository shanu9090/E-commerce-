from django.shortcuts import render
from . models import  *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import views as auth_views
from auth1.forms import CustomerProfileForm
from django.views import View
from django.contrib import messages
from .forms import PaymentForm
import razorpay
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
#def home(request):
    #  request.session['cart']={}
    #  if cart ==None:       
        #  request.session['cart']={}
    #  print(dict(request.session))
    #  return render(request,"application/home.html")
def home(request):
    cart=request.session.get('cart')
    if cart==None:       
        request.session['cart']={}
  # print(dict(request.session))
    return render(request,"application/home.html")

def search(request):
    if request.method=="POST":
        search=request.POST.get('search')
        print(search)
        # data=Woman_item.objects.all()
        # data=Woman_item.objects.filter(Name=search)
        #print(data)
        if search: 
            data=Woman_item.objects.filter(Name__icontains=search)
            print(data)
            data1=Man_item.objects.filter(Name__icontains=search)
            print(data1)
            data2=Kids_item.objects.filter(Name__icontains=search)
            print(data2)
            if data:
               return render(request,"application/search.html",{'data':data})           
            if data1:
               return render(request,"application/search.html",{'data':data1})
            if data2:
               return render(request,"application/search.html",{'data':data2}) 
            else:
               msg="No Data are Found"
               return render(request,"application/search.html",{'msg':msg})    
                            
    return render(request,"application/search.html")

def woman_clothes(request):
    try:
        if request.method=="POST":
            requestuire=request.POST['requ']
            print(requestuire)
            stoke=request.POST['instoke']
            print(stoke)
            id=int(request.POST.get('product_id'))
            print(id)
            quen=Woman_item.Quantity
     
            if  requestuire>stoke:
                global data
                data=Woman_item.objects.all()
                msg="Out of Stoke"
                return render(request,"application/womancloth.html",{'data':data,'msg1':msg,'id':id})
                #print(id.value)  
            
            cat_id="woman"+str(id)
            cart=request.session.get('cart')
            old=cart.get(cat_id)
            print(cart)
            if old:
                cart[cat_id]=requestuire+old
            else:
                #cart={}
                cart[cat_id]=requestuire
            #print(cart)
            request.session['cart']=cart    
            cart=request.session.get('cart')   
                    
        cart=request.session.get('cart')
        print(cart)
        data=Woman_item.objects.all()
        return render(request,"application/womancloth.html",{'data':data})
    except:
      
        return render(request,"application/womancloth.html",{'data':data})
        

def man_clothes(request):
    try:  
        if request.method=="POST":
            requestuire=int(request.POST.get('requ'))
            print(requestuire)
            stoke=int(request.POST.get('instoke'))
            id=int(request.POST.get('product_id'))
            quen=Man_item.Quantity
            if requestuire>stoke:
                data=Man_item.objects.all()
                msg="Out of Stoke"
                return render(request,"application/womancloth.html",{'data':data,'msg1':msg,'id':id})
                #print(id.value)  
            
            cat_id="mancloth"+str(id)
            cart=request.session.get('cart')
            old=cart.get(cat_id)
            print(cart)
            if old:
                cart[cat_id]=requestuire+old
            else:
                #cart={}
                cart[cat_id]=requestuire
            #print(cart)
            request.session['cart']=cart    
            cart=request.session.get('cart')            
        cart=request.session.get('cart')
        print(cart)
        data=Man_item.objects.all()
        return render(request,"application/womancloth.html",{'data':data})
    except:
        return render(request,"application/womancloth.html",{'data':data})

    
def kids_clothes(request):
    try:
        if request.method=="POST":
            requestuire=int(request.POST.get('requ'))
            stoke=int(request.POST.get('instoke'))
            id=int(request.POST.get('product_id'))
            quen=Kids_item.Quantity
            if requestuire>stoke:
                data=Kids_item.objects.all()
                msg="Out of Stoke"
                return render(request,"application/womancloth.html",{'data':data,'msg1':msg,'id':id})
                #print(id.value)  
           # cat="woman"
            cat_id="kids"+str(id)
            print(cat_id,"kidsclothes are available")
            cart=request.session.get('cart')
            old=cart.get(cat_id)
            print(cart)
            if old:
                cart[cat_id]=requestuire+old
            else:
                #cart={}
                cart[cat_id]=requestuire
            print(cart)
            request.session['cart']=cart    
            cart=request.session.get('cart')            
        cart=request.session.get('cart')
        #print(cart)
     
        data=Kids_item.objects.all()
        return render(request,"application/womancloth.html",{'data':data})
    except:
        return render(request,"application/womancloth.html",{'data':data})

  
# def mycart(request):
    # return render(request,"application/mycart.html")
def mycart(request): 
    if request.method=="POST":
        if request.POST.get('remove'):
            remove=request.POST.get('remove')
            print(remove)
            id=request.POST.get('id')
            print(id)
            cart=request.session.get('cart')
            cat=request.POST.get('cart')
            catid=cat+str(id) 
            print(catid)
            car=cart.pop(catid)
            print(car)
            request.session['cart']=cart
            return HttpResponseRedirect('/mycart/')        
        updatequen=request.POST.get('update')  
        print(updatequen)       
        cat=request.POST.get('cart')
        cart=request.session.get('cart')
        id=request.POST.get('id')
        catid=cat+str(id)   
        print(catid)
        cart[catid]=updatequen
        request.session['cart']=cart
        print(cart)

        #return render(request,"application/mycart.html")       

    data=request.session.get('cart')
    global TAmount
    global list_final
    list_final=[]
    global GT
    GT=0
    shipping_Amount=70
    try:
        for i ,j in data.items():
            
            if "woman" in i:
                id=int(i[5:])
                d1=Woman_item.objects.get(pk=id)
                price1=d1.Price
                total=int(j)*price1
                # total1=total+shipping_Amount
                lis=[d1,j,total]
                list_final.append(lis)
                GT+=total
                TAmount=GT+shipping_Amount
       
            if "mancloth" in i:
              #print(i,"mancloth")
              id=int(i[8:])
              d1=Man_item.objects.get(pk=id)
              price1=d1.Price          
              total=int(j)*price1
              lis=[d1,j,total]
              list_final.append(lis)
              GT+=total   
              TAmount=GT+shipping_Amount   
            if "kids" in i:
               #print(i,"kidcloth")
               id=int(i[4:])
               d1=Kids_item.objects.get(pk=id)
               price1=d1.Price
               total=int(j)*price1
               lis=[d1,j,total]
               list_final.append(lis)
               GT+=total
               TAmount=GT+shipping_Amount
        return render(request,"application/mycart.html",{'list_final':list_final,'GT':GT,'TAmount':TAmount})     
    except:
        return render(request,"application/mycart.html",{'msg':'Mycart Empty'})
    return render(request,"application/mycart.html",{'list_final':list_final,'GT':GT})

def make_payment(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            user=request.user
            print(user)
            data=request.session.get('cart')
            print(data)
            # cat=request.method.get('cat')
            for i,j in data.items():
                if  'woman' in i:
                    cat1='woman'
                    id=int(i[5:])
                    quanti=j
                    ins=Transaction(user=user,cat=cat1,cat_id=id,purchased_quan=quanti)
                    ins.save()

                if  'mancloth' in i:
                     cat1='womancloth'
                     id=int(i[8:])
                     quanti=j
                     ins=Transaction(user=user,cat=cat1,cat_id=id,purchased_quan=quanti)
                     ins.save()

                if  'kids' in i:
                      cat1='kids'
                      id=int(i[4:])
                      quanti=j
                      ins=Transaction(user=user,cat=cat1,cat_id=id,purchased_quan=quanti)
                      ins.save()
                return HttpResponseRedirect('/item_payment/')      
            # request.session['cart']={}
            return HttpResponseRedirect("/item_payment/")            


            # return HttpResponse('please proceed for payment')
        else:
            return HttpResponseRedirect('/login/')
    # return render(request,"application/checkout.html")
# def changepassword(request):
    # return render(request,"application/changepassword.html")


def item_payment(requestuest):
    # if requestuest.method=="POST":    
    name=requestuest.user
    GT
    amount=GT
    name = name
    # requestuest.POST['name']
    amount =  amount * 100
    # int(requestuest.POST['amount'])
    client = razorpay.Client(auth=("rzp_test_m2qsd9L3YJ43ki"
    , "424fkMkup1MFkVNuFMZVLCUb" ))
    response_payment = client.order.create({'amount':amount, 'currency':'INR',
                          'payment_capture':'1' })
    
    print(response_payment)
    order_status = response_payment['status']
    order_id = response_payment['id']
    
    if order_status=='created':
        product = ItemModel(name=name , amount =amount , order_id = response_payment['id'],)
        product.save()
        response_payment['name'] = name
        fm = PaymentForm( requestuest.POST or None)
        return render(requestuest,'application/checkout.html',{'form':fm,'add':add,'GT':GT,'list_final':list_final,'payment':response_payment,'TAmount':TAmount})

    fm = PaymentForm()
    return render(requestuest,'application/paymentitem.html',{'form':fm})

@csrf_exempt
def payment_status(requestuest):
    # print(requestuest.POST)
    if requestuest.method=='POST':
        response = requestuest.POST
        print(response)
        params_dict = {
            'razorpay_order_id': response['razorpay_order_id'],
            'razorpay_payment_id': response['razorpay_payment_id'],
            'razorpay_signature': response['razorpay_signature']
        }

        # client instance
        client = razorpay.Client(auth=("rzp_test_m2qsd9L3YJ43ki"
, "424fkMkup1MFkVNuFMZVLCUb" ))

        try:
            status = client.utility.verify_payment_signature(params_dict)
            item = ItemModel.objects.get(order_id=response['razorpay_order_id'])
            item.razorpay_payment_id = response['razorpay_payment_id']
            item.paid = True
            item.save()
            return render(requestuest, 'application/paymentstatus.html', {'status': True})
        except:
            return render(requestuest, 'application/paymentstatus.html', {'status': False})
    return render(requestuest, 'application/paymentstatus.html')

def userprofile(request):
   try: 
    if request.method=="POST":
        user=request.user
        img=request.get.POST("img")
        name=request.get.POST("name")
        email=request.get.POST("email")
        age=request.get.POST("age")
        number=request.get.POST("number")
        usr=Profile(user=user,name=name,email=email,age=age,mobilenumber=number,image=img)
        usr.save()
        return render(request,"application/user-profile.html",{'usr':usr})
   except:     
      return render(request,"application/user-profile.html")

class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'application/profile.html',{'form':form})
    
    def post(self,request):      
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            usr=request.user
            # name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            state=form.cleaned_data['state']
            city=form.cleaned_data['city']
            zipcode=form.cleaned_data['zipcode']
            global reg
            reg=Customer(user=usr,locality=locality,state=state,city=city,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratualations Data is Inserted")
            return render(request,"application/profile.html",{'form':form})
        return render(request,"application/profile.html",{'form':form})
    
        
def address(request):
    add=Customer.objects.filter(user=request.user)   
    return render(request,"application/address.html",{'add':add,'active':'btn-primary'})

def userprofile(request):
    if request.method=="POST":
        user=user.request
        usr=Profile.objects.filter(user=user)
        print(usr)
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        age=request.POST.get('age')
        image=request.FILES.get('img')
        if usr:
           data=Profile(id=id,name=usr.name,email=usr.email,number=usr.number,age=usr.age,image=usr.image)
           data.save()
           print(data)
        
        #    data=Profile.objects.get(id=id)
        return render(request,"application/user-profile.html")
    return render(request,"application/user-profile.html")


def addresscrud(request,id):
    add=Customer.objects.filter(user=request.user)
    if request.method=="POST": 
        if request.POST.get('remove'):
            remove=request.POST.get('remove')
            print(remove)
            ad=Customer.objects.get(id=id)
            ad.delete() 
            return render(request,"application/address.html",{'add':add})
        
        # elif request.POST.get('update'):
            # update=request.POST.get('remove')
            # print(update)
            # locality=request.POST.get('locality')
            # state=request.POST.get('state')
            # city=request.POST.get('city')
            # zipcode=request.POST.get('zipcode')
            # 
            # if locality==None:
            #    reg=Customer.objects.filter(id=id).update(locality=locality,state=state,city=city,zipcode=zipcode)
            #    return render(request,"application/address.html",{'add':add})

            # else:
                # reg=Customer(id=id ,locality=locality,state=state,city=city,zipcode=zipcode)
                # reg.save()
                # return render(request,"application/address.html",{'add':add})
            # 
    # data=Customer.objects.get(id=id)
        # return render(request,"application/update-address.html",{'data':data,'active':'btn-primary'})
    # return render(request,"application/update-address.html",{'data':data,'active':'btn-primary'})

def addresscrudupdate(request,id):
        if request.method=="POST":
            update=request.POST.get('update')
            print(update)
            name=request.POST.get('name')
            locality=request.POST.get('locality')
            state=request.POST.get('state')
            city=request.POST.get('city')
            zipcode=request.POST.get('zipcode')
            if city==None: 
                reg=Customer.objects.filter(id=id).update(locality=locality,state=state,city=city,zipcode=zipcode)
                return render(request,"application/address.html")
            else:         
                reg=Customer(id=id ,locality=locality,state=state,city=city,zipcode=zipcode)
                reg.save()
                return render(request,"application/address.html")
        data=Customer.objects.get(id=id)
        #return render(request,"application/update-address.html",{'data':data,'active':'btn-primary'})
        return render(request,"application/update-address.html",{'data':data})      
    



def mycart_search(request):
    return render(request,"application/mycart.html")

# def profile(request):
    # return render(request,"application/profile.html")

def order(request):
    return render(request,"application/order.html")

def checkout(request):
    
    user=request.user
    global add
    add=Customer.objects.filter(user=user)
    # item1=Woman_item.objects.filter(Category=user)
    # item2=Man_item.objects.filter(Category=user)
    # item3=Kids_item.objects.filter(Category=user)

    # data=request.session.get('cart')
    # list_final=[]
    # global GT
    # GT=0
    # shipping_Amount=70
    # for i ,j in data.items():
        # 
        # if "woman" in i:
            # id=int(i[5:])
            # d1=Woman_item.objects.get(pk=id)
            # price1=d1.Price
            # total=int(j)*price1
            # total1=total+shipping_Amount
            # lis=[d1,j,total]
            # list_final.append(lis)
            # GT+=total
            # TAmount=GT+shipping_Amount
   
        # if "mancloth" in i:
        #   print(i,"mancloth")
        #   id=int(i[8:])
        #   d1=Man_item.objects.get(pk=id)
        #   price1=d1.Price          
        #   total=int(j)*price1
        #   lis=[d1,j,total]
        #   list_final.append(lis)
        #   GT+=total   
        #   TAmount=GT+shipping_Amount   
        # if "kids" in i:
        #    print(i,"kidcloth")
        #    id=int(i[4:])
        #    d1=Kids_item.objects.get(pk=id)
        #    price1=d1.Price
        #    total=int(j)*price1
        #    lis=[d1,j,total]
        #    list_final.append(lis)
        #    GT+=total
        #    TAmount=GT+shipping_Amount
    return render(request,"application/checkout.html",{'list_final':list_final,'add':add,'GT':GT,'TAmount':TAmount})


def paymentdone(request):
    if request.method=="POST":
        user=request.user
        custid=request.GET.get('custid')
        customer=Customer.objects.get(id=custid)
        cart=request.session.get('cart')
        for c in cart:
            Orderplace(user=user,customer=customer,product=c.Category, 
            quantity=c.Quantity).save()
            c.delete()
        return HttpResponseRedirect('/order/')    
    # uyser=request.user
    # custid=request.get('custid')
    # customer=Customer.objects.get(id=custid)
    # cart=Transaction.objects.filter(user=user)
    # for c in cart:
        # Orderplace(user=user,customer=customer,product=c.product, quantity=c.quantity).save()
        # c.delete()
    return render(request,"application/order.html")
   