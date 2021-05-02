# class StackOverflowMiddleware:
#     def process_exception(self, request, exception):
#         print(exception.__class__.__name__)
#         print(exception.message)
#         return None

from django.utils.deprecation import MiddlewareMixin


class JSONTranslationMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response
        self.translations = {
            "en": {"greeting": "Hello", "header": "Welcome Django!"},
            "nl": {"greeting": "Hallo", "header": "Welkom Django!"},
        }

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        if "en" in request.META["HTTP_ACCEPT_LANGUAGE"]:
            response.context_data["translations"] = self.translations
            return response
        return response


class MySimpleMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        print("something")
        try:
            request.session['my_message'] = "boss"
        except:
            request.session['my_message'] = "ok"


class CountRequestsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.count_requests = 0
        self.count_exceptions = 0

    def __call__(self, request):
        self.count_requests += 1
        print(f"Handled {self.count_requests} requests so far")
        return self.get_response(request)

    def process_exception(self, request, exception):
        self.count_exceptions += 1
        print(f"Encountered {self.count_exceptions} exceptions so far")
