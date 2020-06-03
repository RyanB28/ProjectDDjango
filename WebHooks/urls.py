from django.urls import path, include
from WebHooks import views as WebHooksView

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', csrf_exempt(WebHooksView.TestRepsonse))
]