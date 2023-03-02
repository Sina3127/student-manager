from django.contrib import admin

from .models import Contract, Duration, Agreement


class DurationInline(admin.TabularInline):
    model = Duration
    extra = 1
    min_num = 1
    max_num = 12


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    inlines = [DurationInline]


admin.site.register(Contract)
admin.site.register(Duration)
