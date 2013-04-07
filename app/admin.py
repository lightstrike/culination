from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import (Home, HomeBlock, Press, PressLinkBlock, PressTeamBlock, PressExpertBlock, PressPartnerBlock, PressTestimonialBlock,
                     Lesson, Step, About, FeaturedChef, LessonIngredient, Ingredient, Tool, DietaryRestrictions, Cuisine, Course, Video,
                     ChefPledge, LessonPledge, LessonRequest, UserSignupRequest)


####################################
### Mezzanine Page administation ###
####################################

class HomeBlockAdmin(admin.TabularInline):
    model = HomeBlock


class HomeAdmin(PageAdmin):
    inlines = (HomeBlockAdmin,)


class PressLinkBlockAdmin(admin.TabularInline):
    model = PressLinkBlock


class PressTeamBlockAdmin(admin.TabularInline):
    model = PressTeamBlock
    
    
class PressExpertBlockAdmin(admin.TabularInline):
    model = PressExpertBlock
    
    
class PressPartnerBlockAdmin(admin.TabularInline):
    model = PressPartnerBlock
    
    
class PressTestimonialBlockAdmin(admin.TabularInline):
    model = PressTestimonialBlock


class PressAdmin(PageAdmin):
    inlines = (PressLinkBlockAdmin, PressTeamBlockAdmin, PressExpertBlockAdmin, PressPartnerBlockAdmin, PressTestimonialBlockAdmin,)

####################################
### Application adminstration    ###
####################################

class StepAdmin(admin.TabularInline):
    model = Step
    fk_name = 'lesson'

class LessonIngredientAdmin(admin.TabularInline):
    model = LessonIngredient


class LessonAdmin(admin.ModelAdmin):
    inlines = (StepAdmin,LessonIngredientAdmin)

class ChefPledgeAdmin(admin.TabularInline):
    model = ChefPledge

class LessonPledgeAdmin(admin.TabularInline):
    model = LessonPledge

class LessonRequestAdmin(admin.ModelAdmin):
    inlines = (LessonPledgeAdmin, ChefPledgeAdmin)


class FeaturedChefAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        field = super(FeaturedChefAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'chef':
            field.queryset = field.queryset.filter(profile__professional_chef = True)

        return field



admin.site.register(Home, HomeAdmin)
admin.site.register(Press, PressAdmin)
admin.site.register(About, PageAdmin)
admin.site.register(FeaturedChef, FeaturedChefAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(DietaryRestrictions, admin.ModelAdmin)
admin.site.register(Ingredient, admin.ModelAdmin)
admin.site.register(Tool, admin.ModelAdmin)
admin.site.register(Course, admin.ModelAdmin)
admin.site.register(Cuisine, admin.ModelAdmin)
admin.site.register(Video, admin.ModelAdmin)
admin.site.register(LessonRequest, LessonRequestAdmin)
admin.site.register(UserSignupRequest, admin.ModelAdmin)