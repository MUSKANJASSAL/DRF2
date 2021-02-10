from django.contrib import admin
from .models import Article

# Register your models here.
# As we want to access the model through administration panel

admin.site.register(Article)
