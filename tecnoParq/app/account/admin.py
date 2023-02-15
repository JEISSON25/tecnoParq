from django.contrib import admin
from .models import *
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter, NumericRangeFilter
# Register your models here.

# admin.site.register(Account)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('name', 'last_name', 'password',
                    'created', 'modified')

@admin.register(Input_Output)
class Input_OutputAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('account', 'date_in', 'time_in',
                    'date_out', 'time_out',
                    'created', 'modified')
    list_filter = (('date_in',DateRangeFilter), 'time_in')
    search_fields = (
        "=account__identify",
        "date_in",
    )

    def get_rangefilter_created_at_default(self, request):
        return (datetime.date.today, datetime.date.today)