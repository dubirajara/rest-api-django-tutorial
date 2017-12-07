from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    path('bucketlists/', CreateView.as_view(), name="create"),
    path('bucketlists/<int:pk>/',
        DetailsView.as_view(), name="details"),
    path('auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    path('get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
