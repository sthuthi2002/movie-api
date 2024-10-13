from django.utils.deprecation import MiddlewareMixin
import threading

class RequestCounterMiddleware:
    counter = 0
    lock = threading.Lock()

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        with self.lock:
            RequestCounterMiddleware.counter += 1
        response = self.get_response(request)
        return response

    @classmethod
    def get_request_count(cls):
        with cls.lock:
            return cls.counter

    @classmethod
    def reset_count(cls):
        with cls.lock:
            cls.counter = 0
