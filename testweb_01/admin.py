from django.contrib import admin
from .models import Project, New, Question, Answer

# Register your models here.


admin.site.register(Project)

admin.site.register(New)

class QuestionInline(admin.TabularInline):
    model = Question

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):

    inlines = [AnswerInline]
    print (inlines)

    def get_fields(request, obj=None):
        print("QuestionAdmin.get_inline_instances, obj =", obj)
        return [inline(self.model, self.admin_site) for inline in self.inlines]


class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

