from django.contrib import admin

from sisitts.models import Sisit


@admin.register(Sisit)
class SisitAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'get_trimmed_content',
        'likes_count',
        'timestamp',
    ]

    def get_trimmed_content(self, obj):
        return obj.content[:32]
    get_trimmed_content.short_description = 'Trimmed content'