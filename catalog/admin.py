from django.contrib import admin
from .models import Author, Genre, Book, BookInstance,Subcription_type_quarterly,Subscription_type_annual,Subscription_type_halfyearly,Subscription_type_monthly


admin.site.register( Subscription_type_monthly)
admin.site.register( Subscription_type_annual)
admin.site.register( Subscription_type_halfyearly)
admin.site.register( Subcription_type_quarterly)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# admin.site.register(Subscription_type)
admin.site.register(Genre)

# Register the Admin classes for Book using the decorator


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
# admin.site.register(SmartPhone)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


# admin.site.register(Membership)

#admin.site.register(Book)
