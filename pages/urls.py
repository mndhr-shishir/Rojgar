from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.SearchResultsView.as_view(), name='search-results'),

    path('tags/', views.TagListView.as_view(), name='tag-list'),
    path('tags/<slug:slug>/', views.TagDetailsView.as_view(),
         name='tag-details'),

    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('public/<int:pk>/', views.PublicProfileView.as_view(), name='public_profile'),
    path('public/<int:pk>/<str:action>/', views.UserActionView.as_view(), name='user-action'),
    path('public/comment/<int:pk>/', views.CommentView.as_view(), name='comment-view'),

    path('favourite_profile/<int:pk>/', views.add_favourite, name="add-favourite"),
    path('favourites/', views.list_favourites, name="list-favourites"),


    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<str:cat>/', views.CategoryDetailsView.as_view(), name='category-details'),
]
