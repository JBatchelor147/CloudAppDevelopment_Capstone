from django.contrib import admin
from .models import CarMake, CarModel
# from .models import related models


# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModel)

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
