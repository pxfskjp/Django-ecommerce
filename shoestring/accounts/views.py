from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

from nap import http
from nap.rest import views

from . import mappers


class LoginView(views.BaseObjectView):
    mapper_class = mappers.UserMapper

    def get(self, request):
        if request.user.is_authenticated():
            return self.single_response(object=request.user)
        return http.Forbidden()

    def post(self, request):
        if request.user.is_authenticated():
            auth.logout(request)
        form = AuthenticationForm(request, self.get_request_data())
        if form.is_valid():
            auth.login(request, form.get_user())
            return self.get(request)
        return self.error_response(form.errors)
