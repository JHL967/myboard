# board/admin.py (업그레이드 버전)

from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']  # 목록에 보여줄 필드
    list_filter = ['created_at']                           # 오른쪽 필터
    search_fields = ['title', 'content']                   # 검색 기능


admin.site.register(Post, PostAdmin)