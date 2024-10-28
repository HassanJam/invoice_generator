from django.contrib import admin
from django.urls import path, include
from quotations.views import index_view, quotation_view , get_client_invoice_details,login_view   # Import your views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),  
    path('index/', index_view, name='index'),
    path('get-client-invoice-details/', get_client_invoice_details, name='get_client_invoice_details'),
    path('quotation/', include('quotations.url')),  # Fixed spelling here
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Using Django's logout
    path('login/', login_view, name='login'),
]