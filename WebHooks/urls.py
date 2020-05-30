from django.urls import path, include
from WebHooks import views as WebHooksView

urlpatterns = [
    path('', WebHooksView.TestRepsonse)
]