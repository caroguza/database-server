from django.urls import path
from key_value.views import IndexView, SetKeyValueView, GetKeyValueView

urlpatterns = [    
    path('set/', SetKeyValueView.as_view()),
    path('get/', GetKeyValueView.as_view()),
    path('', IndexView.as_view()),
]
