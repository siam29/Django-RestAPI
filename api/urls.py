from django.urls import path, include
from rest_framework import routers
from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewset,basename='employee')
router.register('blogs', views.BlogDetailView, basename='blog')
router.register('comments', views.CommentDetailView, basename='comment')

urlpatterns = [
    # path('students/', views.studentsView),
    # path('students/<int:pk>/', views.studentDetailView),
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/',views.EmployeeDetailView.as_view())

    path('', include(router.urls)),
    # path('blogs/',views.BlogsView.as_view()),
    # path('comments/',views.CommentsView.as_view()),
    # path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    # path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]