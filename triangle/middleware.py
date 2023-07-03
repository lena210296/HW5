import json

from django.utils import timezone

from .models import Log


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/admin'):
            log = Log(
                path=request.path,
                method=request.method,
                query=json.dumps(dict(request.GET)),
                body=json.dumps(dict(request.POST)),
                timestamp=timezone.now()
            )
            log.save()

        response = self.get_response(request)
        return response
