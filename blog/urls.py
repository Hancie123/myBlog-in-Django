from django.contrib import admin
from django.urls import path, include
from blog import views

admin.site.site_header='Hancie Phago'
admin.site.site_title="Welcome to Hancie Phago Dashboard"
admin.site.index_title="Hancie Phago Portal"


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index,name='index'),
    path('blog/',views.blog,name='blog'),
    path('blogpost/<str:slug>',views.blogpost,name='blogpost'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search,name='search')
]