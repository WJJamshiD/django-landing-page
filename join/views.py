from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404, HttpResponseRedirect
from .models import Join
from django.urls import reverse
from django.views import generic
from .forms import JoinForm
# Create your views here.





def join(request):
    form=JoinForm(request.POST)
    if request.method=='GET':
        context={'form':form}
    if request.method=='POST':
        print(form)
        if form.is_valid():
            print('valiiiiiiddddddddddddddddddddddddddddddddddd')
            form.save(commit=False)
            form.save()
        else:
            print(form.errors)
        context={'form':form}
    return render(request,'index.html',context)



# class Malumot(generic.DetailView):
#     model=Join
#     template_name='join/malumot.html'

# class Natijalar(generic.DetailView):
#     model=Join
#     template_name='join/natijalar.html'


# # def ovoz_berish(request,savol_id):
# #     pol=get_object_or_404(Join,pk=savol_id)
# #     try:
# #         tanlangan_variant = pol.variant_set.get(pk=request.POST['variant'])
# #     except (KeyError, Variant.DoesNotExist):
# #         return render(request, 'join/malumot.html', {
# #             'pol': pol,
# #             'error_message': "Siz hechqaysi variantni tanlamadingiz!",
# #         })
# #     else:
# #         tanlangan_variant.ovozlar += 1
# #         tanlangan_variant.save()
# #         # Always return an HttpResponseRedirect after successfully dealing
# #         # with POST data. This prevents data from being posted twice if a
# #         # user hits the Back button.
# #         return HttpResponseRedirect(reverse('join:natijalar', args=(pol.pk,)))




