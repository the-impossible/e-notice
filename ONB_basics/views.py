#Django Imports
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
#My App imports
from ONB_admin.models import (Notification, Comment)
from ONB_admin.form import AddCommentForm
from ONB_auth.models import Accounts



# Create your views here.
class HomeView(View):
    def get(self, request):
        notifications = Notification.objects.all().order_by('-date_created')
        context = {
            'notifications':notifications
        }
        return render(request,'basics/index.html', context)

class ViewNotificationView(View):
    def get(self, request, notification_id):
        try:
            notifications = Notification.objects.get(id=notification_id)
            comments = Comment.objects.filter(commented_on=notifications)
            context = {
                'post':notifications,
                'comments':comments,
                'form':AddCommentForm()
            }
        except Notification.DoesNotExist:
            messages.error(request, "Error Displaying notification")
            return redirect(to='basics:home')
        return render(request, 'basics/detail.html', context)

    def post(self, request, notification_id):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            try:
                user = Accounts.objects.get(id=request.user.id)
                post = Notification.objects.get(id=notification_id)

                form.posted_by = user
                form.commented_on = post
                form.save()
                messages.success(request, f'Comment has been posted!')
                return redirect('basics:view_notification', notification_id)
            except Notification.DoesNotExist:
                messages.error(request, "Error Commenting on post")
                return redirect(to='basics:home')
            except Accounts.DoesNotExist:
                messages.error(request, "Login to be able to comment")
                return redirect(to='auth:login')

class DeleteCommentView(View):
    def get(self, request, comment_id, notification_id):
        try:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            messages.success(request, f'Comment has been deleted')
        except Comment.DoesNotExist:
            messages.error(request, f'Error deleting comment')

        return redirect('basics:view_notification', notification_id)