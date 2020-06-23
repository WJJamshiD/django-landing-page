from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404, HttpResponseRedirect
from .models import Join,Subcriber
from django.urls import reverse
from django.views import generic
from .forms import JoinForm,SubscriberForm,AddressForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import uuid
from django.contrib.auth import authenticate

# Create your views here.





def join(request):
    form=JoinForm(request.POST)
    if request.method=='GET':
        context={'form':form}
    if request.method=='POST':
        print(form)
        if form.is_valid():
            a=form.save(commit=False)
            a.save()
            messages.add_message(request,messages.SUCCESS, 'You\'ve succesfully joined!')
            
            subject='Thank you for your Pre-Order'
            message='jlksjdfvpakdgvpojaodkvao[dvga.;asfka'
            from_mail=settings.EMAIL_HOST_USER
            to_list=[a.email]
            send_mail(subject,message,from_mail,to_list,fail_silently=True)
            
            print(a.email)
            return redirect('thank_you')
        else:
            print(form.errors)
        context={'form':form}
    return render(request,'index.html',context)


def thanks(request):
    return render(request,'thank_you.html')

def aboutus(request):
    return render(request,'about_us.html')

def get_ref_id():
    ref_id=str(uuid.uuid4()).replace('-','')[:10]
    try:
        Subcriber.objects.get(ref_id=red_id)
        get_ref_id()
    except:
        return ref_id

def lwc_index(request):
    form=SubscriberForm(request.POST or None)
    referrer_id=request.session.get('referrer')
    try:
        referrer=Subcriber.objects.get(id=referrer_id)
    except:
        referrer=None
    print(referrer)
    if request.method=="GET":
        return render(request,'lwc_index.html',{'form':form})
    if request.method=="POST":
        if form.is_valid():
            email=form.cleaned_data['email']
            new_subscriber,created=Subcriber.objects.get_or_create(email=email)
            if created:   
                try:
                    ip=request.META['HTTP_X_FORWARDED_FOR'].split()[0]
                    new_subscriber.ip_address=ip
                except:
                    ip=request.META['REMOTE_ADDR']
                    new_subscriber.ip_address=ip
                else:
                    pass
                new_subscriber.ref_id=get_ref_id()
                new_subscriber.referrer=referrer
                new_subscriber.save()
            return HttpResponseRedirect(reverse('lwc_referral', kwargs={'ref_id':new_subscriber.ref_id}))
        else:
            return redirect('lwc_index')

def lwc_referral(request,ref_id):
    obj=Subcriber.objects.get(ref_id=ref_id)
    friends=obj.referrals.count()
    sharelink='https://mathwj.com/en/lwc_index/?ref={}'.format(ref_id)
    context={
        'sharelink':sharelink,
        'friends':friends
    }
    return render(request,'lwc_share.html',context)


def contactus(request):
    form=AddressForm(request.POST or None)

    if form.is_valid():
        print(form)
        instance=form.save(commit=False)
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user=authenticate(username=username,password=password)
        if user:
            instance.user=user
            instance.save()
            messages.add_message(request,messages.SUCCESS,'Your address saved in your profile info succesfully!')
        else:
            messages.add_message(request,messages.ERROR,'Please check your password and username, did you type correctly?!')
    return render(request,'contact_us.html',{'form':form}) 