from django.shortcuts import render

from django_app.apps.web.views.base_view import BaseView


class IndexView(BaseView):
    template_name = 'dashboard.html'
    def get(self, request):
        return render(request, self.template_name)
