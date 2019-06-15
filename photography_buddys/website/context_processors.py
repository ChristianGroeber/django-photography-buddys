def loggedin_user(request):
    user = request.user
    if str(user) is not 'AnonymousUser':
        return {'login_required': False, 'user': user}
    else:
        return {'login_required': True}
