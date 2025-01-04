from django.contrib import admin

from tunes.models import Feedback, Quote


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    pass

