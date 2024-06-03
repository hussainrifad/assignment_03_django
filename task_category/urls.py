from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_category, name='addcategory'),
    path('delete/<int:id>', views.delete_category, name='deletecategory'),
    path('update/<int:id>', views.update_category, name='updatecategory'),
]