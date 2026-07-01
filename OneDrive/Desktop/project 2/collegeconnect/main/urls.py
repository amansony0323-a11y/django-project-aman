from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

path('register/', views.register, name='register'),
path('login/', views.login, name='login'),
path('logout/', views.logout_user, name='logout'),
path('student/', views.student_dashboard, name='student_dashboard'),
path('college/', views.college_dashboard, name='college_dashboard'),
path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
path('create-event/', views.create_event, name='create_event'),
path('events/', views.events, name='events'),   # ✅ ADD THIS
path('event/<int:id>/', views.event_detail, name='event_detail'),
path('event/<int:id>/register/', views.register_event, name='register_event'),
path('my-events/', views.my_events, name='my_events'),
path('profile/', views.profile, name='profile'),
path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
path('college-dashboard/', views.college_dashboard, name='college_dashboard'),
path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
path("contact/", views.contact, name="contact"),
]
