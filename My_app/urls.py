from django.urls import path
from . import views
from .views import updateBook

urlpatterns = [
    path("create-book/", views.creatBook,name='createbook'),
    path('author/', views.Create_Author, name='author'),
    path('', views.listBook,name='booklist'),
    path('detailsview/<int:book_id>/', views.detailsView, name='details'),
    path('updateview/<int:book_id>/', views.updateBook, name='update'),
    path('deleteview/<int:book_id>/', views.deleteView, name='delete'),
    path('book/<int:pk>/', updateBook, name='book_detail'),
    path('book/update/<int:book_id>/', updateBook, name='update_book'),
    path('index/', views.index, name='index'),
    path('search/',views.Search_book,name='search'),# Corrected path
    # path('register/',views.Register_user,name='register'),
    # path('login/',views.loginUser,name='login'),
    # path('logout/',views.logOut,name='logout'),
    # path('home/',views.HomePage,name='home'),
    path("register/",views.userRegistration,name='register'),
    path("login/",views.loginPage,name='login'),
    path("admin_view/",views.admin_view,name='admin_view'),
    path("user_view/",views.user_view,name='user_view'),
    path("logout/", views.logout_view, name='logout'),



]
