# Django Imports
from django.urls import path

# My app imports
from ONB_basics.views import (
    HomeView,
    ViewNotificationView,
    DeleteCommentView,
)

app_name = 'basics'

urlpatterns = [
    # Static pages
    path('', HomeView.as_view(), name='home'),
    path('view_notification/<int:notification_id>', ViewNotificationView.as_view(), name='view_notification'),
    path('delete_comment/<int:comment_id>/<int:notification_id>', DeleteCommentView.as_view(), name='delete_comment'),
]