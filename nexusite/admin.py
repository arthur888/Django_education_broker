from django.contrib import admin
from nexusite.models import Profile, Blog, AcademiRecord, University, Category, EducationLevel, LengthTimeWorkedEducator, Agreement, UserRating, ExperienceLevel, PostRequest, HourlyPrice


admin.site.register(Blog)
admin.site.register(Profile)
admin.site.register(AcademiRecord)
admin.site.register(UserRating)
admin.site.register(University)
admin.site.register(Category)
admin.site.register(ExperienceLevel)
admin.site.register(EducationLevel)
admin.site.register(LengthTimeWorkedEducator)
admin.site.register(Agreement)
admin.site.register(PostRequest)
admin.site.register(HourlyPrice)
