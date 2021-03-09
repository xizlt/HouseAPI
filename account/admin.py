from django.contrib import admin
from django.contrib.auth.models import User

from account.models import Profile, Status
from ad.models import Ad
from application.models import Application
from meter.models import ItemMeter
from reservation.models import Reservation


class AdInline(admin.TabularInline):
    model = Ad
    extra = 0
    readonly_fields = ("title", "type", "created", "beginning", "ending", "text",)
    show_change_link = ('title',)


class ItemMeterInline(admin.TabularInline):
    model = ItemMeter
    extra = 0
    readonly_fields = ("meter",)


class ReservationInline(admin.TabularInline):
    model = Reservation
    extra = 0
    readonly_fields = ("type", "created", "update", "data_begin", "data_end", "executed",)


class ApplicationInline(admin.TabularInline):
    model = Application
    extra = 0
    readonly_fields = ("title", "type", "created", "due_data", "executed", "mark",)
    show_change_link = ('title',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    save_on_top = True
    inlines = (ItemMeterInline, AdInline, ApplicationInline, ReservationInline)
    list_display = ('user', 'street', 'house', 'flat',
                    'status', 'photo', 'ban', 'ban_start',
                    'ban_end', 'user')

    fieldsets = (
        (None, {
            'fields': ('user', 'date_of_birth', 'photo', 'status', 'phone')
        }),
        ('Address', {
            'fields': ('city', 'street', 'house', 'flat')
        }),
        ('Ban', {
            'fields': ('ban', ('ban_start', 'ban_end',))
        }),

    )


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('title',)
    fields = ('title',)
