"""my_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from profiles.views import (
    login_view,
    logout_view,
    register_view,
    edit_user,
    detail_user,
    list_users,
    status_user,

    )
from list_trans.views import (
    all_car, 
    detail_car, 
    delete_car,
    create_car,
    edit_car,
    create_car_in_task,
    )
from tasks.views import(
    index,
    all_tasks,
    detail_tasks,
    delete_task,
    create_task,
    edit_task,
    comments_view,
    comments_edit,
    comments_delete,
    likes_view,
    dnot_likes_view,
    # edit_car_in_task,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('logout/', logout_view),
    path('login/',login_view),
    path('register/', register_view),
    path('allcar/', all_car, name='all_car'),
    path('allcar/car/<int:pk>/', detail_car, name='detail_car'),
    path('car/create/', create_car, name='create_car'),
    path('allcar/car/delete/<int:pk>/', delete_car),
    path('allcar/car/edit/<int:pk>/', edit_car),
    path('profile/<int:pk>/', detail_user, name='detail_user'),
    path('profile/edit/<int:pk>/', edit_user),
    path('list_users/', list_users),
    path('all_tasks/', all_tasks, name='all_tasks'),
    path('all_tasks/<int:pk>/', detail_tasks, name='detail_tasks'),
    path('all_tasks/delete/<int:pk>/', delete_task),
    path('all_tasks/edit/<int:pk>/', edit_task),
    path('all_tasks/create/', create_task, name='create_task'),
    path('commentary/<int:pk>/', comments_view, name='comments_view'),
    path('commentary/<int:pk>/edit/<int:pk1>/', comments_edit, name='comments_edit'),
    path('commentary/delete/<int:pk>/', comments_delete, name='comments_delete'),
    path('task/like/<int:pk>/', likes_view, name='likes_view'),
    path('task/dlike/<int:pk>/', dnot_likes_view, name='dnot_likes_view'),
    path('working/<int:pk>/', status_user, name='status_user'),
    path('all_tasks/<int:pk>/editcarrier/', create_car_in_task, name='create_car_in_task'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

