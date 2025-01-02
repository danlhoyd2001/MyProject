from django.urls import path
from .views import HomePageView, PostPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', PostPageView.as_view(), name='post'),
]