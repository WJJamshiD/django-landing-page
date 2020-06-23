from django.urls import path, include,re_path
from .views import join,thanks,contactus,lwc_index,lwc_referral,aboutus


urlpatterns = [
	path('tankyou/',thanks,name='thank_you'),
	path('contactus/',contactus,name='contact_us'),
	path('aboutus/',aboutus,name='about_us'),
	path('lwc_index/',lwc_index,name='lwc_index'),
	path('<ref_id>/',lwc_referral,name='lwc_referral'),
]