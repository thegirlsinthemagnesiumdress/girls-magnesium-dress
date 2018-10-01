from django.contrib import admin
from core.models import User, Survey, SurveyResult


class UserAdmin(admin.ModelAdmin):
    view_on_site = False


admin.site.register(User, UserAdmin)
admin.site.register(Survey)
admin.site.register(SurveyResult)
