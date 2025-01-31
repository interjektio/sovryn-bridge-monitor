from pyramid.view import notfound_view_config


@notfound_view_config(renderer='bridge_monitor:templates/404.tk')
def notfound_view(request):
    request.response.status = 404
    return {}
