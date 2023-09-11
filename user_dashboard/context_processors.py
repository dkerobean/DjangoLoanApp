from .models import MessageReply


def user_replies_context(request):

    user = request.user
    if user.is_authenticated:
        user_replies = MessageReply.objects.filter(support__user=user)
    else:
        # handle unauthenticated user
        user_replies = None

    return {'user_replies': user_replies}
