from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User


class UserAPIView(APIView):

    def get(self, request):
        lst = User.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = User.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            cat_id = request. data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})