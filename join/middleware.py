from .models import Subcriber


class ReferMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        ref_id=request.GET.get('ref')
        try:
            obj=Subcriber.objects.get(ref_id=ref_id)
        except:
            obj=None
        if obj:
            request.session['referrer']=obj.id
        response=self.get_response(request)
        return response

    
        
