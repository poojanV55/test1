
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name="home" ),
    path('intern_list', views.intern_list, name="intern-list" ),
    path('add_intern', views.add_intern, name="add-intern" ),
    path('edit_intern/<intern_id>', views.edit_intern, name="edit-intern" ),
    path('delete_intern/<intern_id>', views.delete_intern, name="delete-intern" )

]
