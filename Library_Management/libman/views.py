from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import BookForm, EmployerForm, IssueForm, ReturnForm, ContactForm
from .models import Books, Employer, Issue
from django.views.generic import UpdateView, DeleteView
from django.db.models import Q

# Create your views here.
#main site
def index(request):
    return render(request, 'libman/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def view_books(request):
    books = Books.objects.order_by('department')
    query = request.GET.get('q')
    if query:
        books = Books.objects.filter(Q(book_name__icontains=query) | Q(department__icontains=query))
    else:
        books = Books.objects.order_by('department')
    return render(request, 'libman/view_book.html', {'books': books})

@login_required(login_url='/login/')
def view_employer(request):
    employer = Employer.objects.order_by('timer')
    query = request.GET.get('q')
    if query:
        employer = Employer.objects.filter(Q(Fname__icontains=query) | Q(Lname__icontains=query) | Q(phone__icontains=query) | Q(timer__icontains=query) | Q(emp_id__icontains=query))
    else:
        employer = Employer.objects.order_by('timer')
    return render(request, 'libman/view_employer.html', {'employer': employer})

@login_required(login_url='/login/')
def view_issue(request):
    issue = Issue.objects.order_by('borrower_name', 'issue_date')
    return render(request, 'libman/view_issue.html', {'issue': issue})

@login_required(login_url='/login/')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    context = {'form': form}
    return render(request, 'libman/contact.html', context)

def redir(request):
    return redirect('home')