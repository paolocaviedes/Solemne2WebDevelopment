from django.conf.urls import url 
from website import views

urlpatterns = [
                # Matches any html file - to be used for gentella   
                # Avoid using your .html in your resources. Or create a separate django app.
                # The home page  
                url(r'^$', views.index, name='index'),

              ]