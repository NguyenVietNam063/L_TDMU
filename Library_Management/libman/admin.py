from django.contrib import admin
from .models import Books, Employer, Issue, Return, Contact

# Register your models here.
admin.site.register(Books)
admin.site.register(Employer)
admin.site.register(Issue)
admin.site.register(Return)
admin.site.register(Contact)

