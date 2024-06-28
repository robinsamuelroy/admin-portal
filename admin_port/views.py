from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Customer, Invoice
from .forms import CustomerForm, InvoiceForm
from.forms import *
from django.views.decorators.cache import never_cache
from django.contrib import messages


# Login view
@never_cache
def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('admin_portal')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                return HttpResponseRedirect('admin_portal')
            else:
                form.add_error(None, 'Wrong username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
@never_cache
def user_logout(request):
    logout(request)
    request.session.flush()
    return HttpResponseRedirect(reverse('admin_login'))

# Admin portal view
@never_cache
@login_required
def admin_portal(request):
   return render(request, 'admin_portal.html')

# Customer views
@never_cache
@login_required
def customer_list(request):
    customers = Customer.objects.order_by('-created_at')
    return render(request, 'customer_list.html', {'customers': customers})

@login_required
@never_cache
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customer_list'))  # Redirect to customer list page
    else:
        form = CustomerForm()
    return render(request, 'customer_create.html', {'form': form})


@login_required
@never_cache
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customer_list'))
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_edit.html', {'form': form})

@login_required
@never_cache
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return JsonResponse({'message': 'Customer deleted successfully.'})
    return JsonResponse({'error': 'Method not allowed.'}, status=405)

# Invoice views
@login_required
@never_cache
def invoice_list(request):
    invoices = Invoice.objects.order_by('-created_at')
    return render(request, 'invoice_list.html', {'invoices': invoices})

@login_required
@never_cache
def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('invoice_list'))  # Redirect to invoice list page
    else:
        form = InvoiceForm()
    return render(request, 'invoice_create.html', {'form': form})


@login_required
@never_cache
def invoice_edit(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('invoice_list'))
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'invoice_edit.html', {'form': form})

@never_cache
def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        invoice.delete()
        return JsonResponse({'message': 'Invoice deleted successfully.'})
    return JsonResponse({'error': 'Method not allowed.'}, status=405)

