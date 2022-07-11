from rest_framework.generics import CreateAPIView, ListAPIView,UpdateAPIView, RetrieveAPIView
from .models import FlightDetails
from .serializers import FlightSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class CreateFlightsView(CreateAPIView):
    model = FlightDetails
    queryset = FlightDetails.objects.all()
    serializer_class = FlightSerializer


class GetAllFlightsView(ListAPIView):
    model = FlightDetails
    queryset = FlightDetails.objects.all()
    serializer_class = FlightSerializer

    def get(self,request,*args,**kwargs):
        departure_city = request.query_params.get('departure_city')
        departure_time = request.query_params.get('departure_time')
        arrival_city = request.query_params.get('arrival_city')
        if departure_city and arrival_city and departure_time:
            queryset = FlightDetails.objects.filter(departure_city__icontains=departure_city,arrival_city__icontains=arrival_city,departure_time__icontains=departure_time)
            serializer = FlightSerializer(queryset,many=True)
            return Response({'msg':'Flights fetched successfully','data':serializer.data},status=HTTP_200_OK)
        queryset = FlightDetails.objects.all()
        serializer = FlightSerializer(queryset,many=True)
        return Response({'msg':'Flights fetched successfully','data':serializer.data},status=HTTP_200_OK)

class UpdateFlightsView(UpdateAPIView):
    model = FlightDetails
    queryset = FlightDetails.objects.all()
    serializer_class = FlightSerializer


class GetFlightsDetailsView(RetrieveAPIView):
    model = FlightDetails
    queryset = FlightDetails.objects.all()
    serializer_class = FlightSerializer
