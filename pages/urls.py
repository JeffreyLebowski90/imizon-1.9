from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('result', views.result, name='result'),
	path('valve', views.valve, name='valve'),
	path('contact_', views.contact, name='contact_'),
	path('shipping', views.shipping, name='shipping'),
	path('deliver', views.deliver, name='deliver'),
	path('terms', views.terms, name='terms'),
	path('feedbacks', views.feedbacks, name='feedbacks'),
]