from  django.urls import  path
from  . import  views
urlpatterns=[
    path('',views.helloDjango, name='helloDjango'),
    path('index/<int:id>',views.detail,name='detail'),
    path('getAll/', views.getAll, name='getAll'),
    path('addCoach/', views.addCoach, name='addCoach'),
    path('getAll/update/<int:coach_id>', views.update_Coach),
    path('getAll/delete/<int:coach_id>', views.delete_book),
    path('getAll/getAllProject/', views.getAllProject, name='getAllProject'),
    path('getAll/addProject', views.addProject, name='addProject'),
    path('getAll/getAllProject/updatePorject/<int:p_id>', views.updateProject),
    path('getAll/getAllProject/deleteorject/<int:p_id>', views.delete_Project)
]