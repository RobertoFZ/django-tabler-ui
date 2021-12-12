from django.utils.translation import ugettext_lazy as _
from django_app.apps.api.serializers.searchs_params import SearchParamsSerializer
from django_app.common.response import APIResponse

from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey


class SearchsView(APIView):
    permission_classes = [HasAPIKey]
    serializer_class = SearchParamsSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            search_params = serializer.data
            return APIResponse.success(search_params)
        else:
            return APIResponse.bad_request({
                'errors': serializer.errors
            })
