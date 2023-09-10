from .models import MessageReply


def user_replies_context(request):
    user = request.user
    user_replies = MessageReply.objects.filter(support__user=user)
    return {'user_replies': user_replies}
