from django.urls import path
from .views import index_view, quotation_view, invoices_view, get_client_invoice_details, login_view, signup_view

urlpatterns = [
    path('', index_view, name='index'),  # Make the login page the main page
    path('quotation/', quotation_view, name='quotation'),
    path('invoices/', invoices_view, name='invoices'),
    path('create-invoice/', index_view, name='create_invoice'),
    path('get-client-invoice-details/', get_client_invoice_details, name='get_client_invoice_details'),
    path('signup/', signup_view, name='signup'),  # Add signup URL
    path('login/', login_view, name='login'),  # Ensure this is included

]