from django.contrib import admin
from .models import ChatSession, ChatMessage

# Inline model to manage messages directly within ChatSession
class ChatMessageInline(admin.TabularInline):
    model = ChatMessage
    extra = 1  # Display one empty form by default

@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'created_at')
    search_fields = ('user_name',)
    list_filter = ('created_at',)
    inlines = [ChatMessageInline]  # Link the inline messages

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('session', 'message_text', 'sent_at')
    search_fields = ('session__user_name',)
    list_filter = ('sent_at',)
