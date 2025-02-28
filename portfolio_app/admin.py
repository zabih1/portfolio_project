from django.contrib import admin
from .models import Profile, Skill, Technology, Education, Experience, Project, Message

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'location')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'skill_type')
    list_filter = ('skill_type',)

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'time_period', 'order')
    list_editable = ('order',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'time_period', 'order')
    list_editable = ('order',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured')
    list_filter = ('featured', 'technologies')
    filter_horizontal = ('technologies',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'date_sent', 'is_read')
    list_filter = ('is_read', 'date_sent')
    readonly_fields = ('date_sent',)