from django.urls import path
from . import views
from .webhooks import webhook
from .views import send_test_email

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
    path('send-test-email/', send_test_email, name='send_test_email'),
]
