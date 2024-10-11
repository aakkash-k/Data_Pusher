import secrets
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import  Response
from .serializer import DestinationSerializer
from django.shortcuts import get_object_or_404
from .models import Destination
from rest_framework  import status

class DestinationViews(APIView):
    def get(self, request):
        all_dest = Destination.objects.all()
        all_dest_ser = DestinationSerializer(all_dest, many=True).data
        return Response(all_dest_ser, status=status.HTTP_200_OK)

    def post(self, request):
        
        
        new_dest = DestinationSerializer(data=request.data)
        if new_dest.is_valid():
            new_dest.save()
            return Response({"message":"Data is valid"}, status=status.HTTP_201_CREATED)
        return Response(new_dest.errors, status=status.HTTP_400_BAD_REQUEST) 
    

class DestinationViewsById(APIView):
    def get(self, request, id):
        try:
            dest = Destination.objects.get(id=id)
        except dest.DoesNotExist:
            return Response({"message":"requesed record not found"},  status=status.HTTP_404_NOT_FOUND)
        dest = Destination.objects.get(id=id)

        ser_des = DestinationSerializer(dest)
        return Response(ser_des.data, status=status.HTTP_200_OK)
    def put(self, request, id):
    
        dest = get_object_or_404(Destination, id=id)
        dest_ser = DestinationSerializer(dest,data=request.data)
        if dest_ser.is_valid():
            dest_ser.save()
            return Response({"message":"record updated successfully"}, status=status.HTTP_200_OK)
        
        return Response(dest_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        dest = get_object_or_404(Destination, id=id)
        dest.delete()
        return Response({"message": "account deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class DestinationAccessByAccId(APIView):
    
    def delete(self, request, account_id):
        dest = Destination.objects.filter(account_id=account_id)
        dest.delete()
        return Response({"message": "account deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

class getAllDestination(APIView):
    def get(self, request, account_id):

        try:
            dest = Destination.objects.get(account_id=account_id)
        except dest.DoesNotExist:
            return Response({"message":"requesed record not found"},  status=status.HTTP_404_NOT_FOUND)
        dest = Destination.objects.get(account_id=account_id)

        ser_des = DestinationSerializer(dest)
        return Response(ser_des.data, status=status.HTTP_200_OK)



        