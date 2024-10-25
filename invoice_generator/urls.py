from django.contrib import admin
from django.urls import path, include
from quotations.views import index_view, quotation_view , get_client_invoice_details,login_view   # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),  # Set the root URL to the login view
    path('index/', index_view, name='index'),  # Add an explicit route for index
    path('get-client-invoice-details/', get_client_invoice_details, name='get_client_invoice_details'),
    path('quotation/', include('quotations.url')),
]