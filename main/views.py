from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UUIDModel
from .serializers import UUIDSerializer
import uuid
from dateutil.parser import parse


class UUIDList(APIView):
    """Lists all uuids"""
    serializer_class = UUIDSerializer

    def get(self, request):
        """"create new uuid object before returning the request"""
        UUIDModel.objects.create(uuid=uuid.uuid1())
        items = UUIDModel.objects.all().order_by('-updated')
        uuid_serializer = UUIDSerializer(items, many=True)
        res_list = {}
        for item in uuid_serializer.data:
            res_list[str(parse(item['updated']).strftime("%Y-%m-%d %H:%M:%S.%f"))] = item['uuid']

        return Response(res_list)
