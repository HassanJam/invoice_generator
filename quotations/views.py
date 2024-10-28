from django.shortcuts import render, redirect
from .models import Quotation
from django.http import JsonResponse
from .models import Client
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the index view after successful login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'quotations/login.html')


# Sign Up View
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')  # Redirect to the login page after successful signup
        except Exception as e:
            messages.error(request, str(e))  # Handle error in user creation
    
    return render(request, 'quotations/signup.html')
def get_client_invoice_details(request):
    client_name = request.GET.get('client_name')
    print("Client name received:", client_name)  # Debug log
    try:
        quotation = Quotation.objects.get(customer_name=client_name)
        print("Quotation found:", quotation)  # Debug log
        response_data = {
            'invoice_number': quotation.quotation_number,  # Adjust according to your model field
            'date': quotation.date.strftime('%Y-%m-%d'),  # Format the date as needed
            'phone': quotation.telephone,  # Add the phone number field
            'chassis-number': quotation.chassis_no,  # Add the chassis number field
            'color': quotation.color,  # Make sure this field exists
            'type': quotation.car_brand,  # Make sure this field exists
            'engine-number': quotation.engine_no,  # Add the engine number field
            'car-value': quotation.selling_price,  # Add the car value field
            'vat': quotation.vat,  # Add the VAT field
            'total-amount': quotation.total,  # Add the total field
            'down-payment': quotation.downpayment,  # Add the downpayment field
            'balance-amount': quotation.balance,  # Add the balance field
        }
        return JsonResponse(response_data)
    except Quotation.DoesNotExist:
        return JsonResponse({'error': 'Quotation not found'}, status=404)
    except Quotation.MultipleObjectsReturned:
        return JsonResponse({'error': 'Multiple quotations found'}, status=400)


@login_required(login_url='login')  # Redirect to login if not logged in
def index_view(request):
    # Count the total number of quotations (invoices)
    total_quotations = Quotation.objects.count()
    total_balance = Quotation.objects.aggregate(Sum('total'))['total__sum'] or 0  # Sum of total field

    # Pass the counts to the template
    context = {
        'total_quotations': total_quotations,
        'total_balance': total_balance,  # Pass total balance to template

    }

    return render(request, 'quotations/index.html', context)

@login_required(login_url='login')  # Redirect to login if not logged in
def quotation_view(request):
    
    # Get the last quotation number and increment for the display
    last_quotation = Quotation.objects.order_by('quotation_number').last()
    next_quotation_number = last_quotation.quotation_number + 1 if last_quotation else 1

    if request.method == 'POST':
        # Capture form data
        customer_name = request.POST.get('customer_name')
        telephone = request.POST.get('telephone')
        car_type = request.POST.get('car_type')
        cpr = request.POST.get('cpr')
        date = request.POST.get('date')
        to = request.POST.get('to')
        car_brand = request.POST.get('car_brand')
        chassis_no = request.POST.get('chassis_no')
        engine_no = request.POST.get('engine_no')
        color = request.POST.get('color')
        selling_price = request.POST.get('selling_price')
        vat = request.POST.get('vat')
        total = request.POST.get('total')
        downpayment = request.POST.get('downpayment')
        balance = request.POST.get('balance')

        # Create a new Quotation object and save it to the database
        quotation = Quotation(
            quotation_number=next_quotation_number,
            customer_name=customer_name,
            telephone=telephone,
            car_type=car_type,
            cpr=cpr,
            date=date,
            to=to,
            car_brand=car_brand,
            chassis_no=chassis_no,
            engine_no=engine_no,
            color=color,
            selling_price=selling_price,
            vat=vat,
            total=total,
            downpayment=downpayment,
            balance=balance
        )
        quotation.save()  # Save the new quotation

        # Redirect to the home page after saving the quotation
        return redirect('quotations/index.html')  # or any appropriate redirect

    # Render the form with the next quotation number
    return render(request, 'quotations/quotation.html', {'next_quotation_number': next_quotation_number})
def invoices_view(request):
    quotations = Quotation.objects.all()  # Fetch all quotations from the database
    client_names = [quotation.customer_name for quotation in quotations]  # Extract client names

    return render(request, 'quotations/invoices.html', {'client_names': client_names})

