from django.contrib import admin
from goals.models import GoalCategory, Goal, GoalComment, Board, BoardParticipant


@admin.register(GoalCategory)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")


@admin.register(GoalComment)
class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ("text", "user", "goal", "created", "updated")
    search_fields = ("title", "user")


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    list_display_links = ("title",)


@admin.register(BoardParticipant)
class BoardParticipantAdmin(admin.ModelAdmin):
    list_display = ("user_id", "board_id", "role")
    list_display_links = ("user_id", "board_id", "role")



