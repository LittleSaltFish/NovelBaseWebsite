from django.contrib import admin
from user.models import User,Inform,Follow,Star

# Register your models here.
admin.site.register(User)
admin.site.register(Inform)
admin.site.register(Follow)
admin.site.register(Star)
