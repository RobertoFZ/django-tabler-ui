from rest_framework import status
from rest_framework.response import Response


class APIResponse:
    @staticmethod
    def success(data, message='Success'):
        return Response({
            'status': status.HTTP_200_OK,
            'data': data,
            'uuid': '',
            'message': message
        })

    @staticmethod
    def bad_request(data=None, message='Bad request'):
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'data': data,
            'message': message,
            'uuid': ''
        }, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def no_content():
        return Response(status=status.HTTP_204_NO_CONTENT)
