"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from library.views import AuthorModelViewSet, AuthorLimitOffsetPaginationViewSet, BookModelViewSet
from todoapp.views import ProjectViewSet, TodoView
from user.views import UserRegistrationView, UserProfileView

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('authors_with_pagination', AuthorLimitOffsetPaginationViewSet)
router.register('users', UserRegistrationView)
router.register('todoapp', TodoView)
router.register('project', ProjectViewSet)
router.register('books', BookModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/profile/<int:pk>/', UserProfileView.as_view(), name='profile_user'),
    path('api-token-auth/', views.obtain_auth_token),
]
