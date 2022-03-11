
from django.contrib import admin
from .models import publisher,questions,survey,post,ask_question,comments,review

# Register your models here.
admin.site.register(publisher),
admin.site.register(questions),
admin.site.register(survey),
admin.site.register(post),
admin.site.register(ask_question),
admin.site.register(comments),
admin.site.register(review)






