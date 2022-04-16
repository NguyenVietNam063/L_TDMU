from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, validate_email, ValidationError
import datetime

# Create your models here.

#book table
class Books(models.Model):
    DEPARTMENT = (
        ('Kinh tế', 'Kinh tế'),
        ('Chính trị', 'Chính trị'),
        ('Công nghệ', 'Công nghệ'),
        ('Khoa học', 'Khoa học'),
        ('Lịch sử', 'Lịch sử'),
        ('Văn học', 'Văn học'),
        ('Toán học', 'Toán học'),
        ('Y khoa', 'Y khoa'),
        ('Giáo dục', 'Giáo dục'),
        ('Xây dựng', 'Xây dựng'),
        ('Nghệ thuật', 'Nghệ thuật'),
        ('Địa lý', 'Địa lý'),
        ('Vật lý', 'Vật lý'),
    )
    isbn_no = models.CharField(max_length=20, blank=True)
    #barcode = models.CharField(max_length=20, unique=True)
    book_id = models.CharField(max_length=20)
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    no_of_books = models.IntegerField()
    #book_detail = models.TextField(default='text')
    department = models.CharField(max_length=20, choices=DEPARTMENT)
    publisher = models.CharField(max_length=100)
    rack_no = models.CharField(max_length=3)

    def Claimbook(self):
        if self.no_of_books>1:
            self.no_of_books=self.no_of_books-1
            self.save()
        else:
            print("Không đủ sách để yêu cầu")

    def Addbook(self):
        self.no_of_books=self.no_of_books+1
        self.save()


    def __str__(self):
        return self.book_name

#borrower table
class BORROWER(models.Model):
    Fname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    phone = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)

    def __str__(self):
        return self.Fname+" "+self.Lname

class Employer(BORROWER):
    TIMER = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    )
    emp_id = models.CharField(max_length=20, unique=True)
    timer = models.CharField(max_length=20, choices = TIMER)

    def __str__(self):
        return self.Fname+" "+self.Lname

class Issue(models.Model):
    borrower_id = models.CharField(max_length=20)
    borrower_name = models.CharField(max_length=100)
    book_name = models.CharField(max_length = 200)
    book_id = models.CharField(max_length=20)
    issue_date = models.DateField(default=datetime.date.today)
    issue_id = models.CharField(max_length=20)
    isbn = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.book_name

class Return(models.Model):
    return_id = models.CharField(max_length=20)
    return_date = models.DateField(default=datetime.date.today)
    borrower_id = models.CharField(max_length=20)
    borrower_name = models.CharField(max_length = 100)
    book_id = models.CharField(max_length=20)
    book_name= models.CharField(max_length=200)
    isbn_no = models.CharField(max_length=20)

    def __str__(self):
        return self.book_name

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email