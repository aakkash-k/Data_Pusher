from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import  Response
from .serializer import AccountSerializer
from django.shortcuts import get_object_or_404
from rest_framework  import status
from .models import Account
import secrets
import requests

class AccountView(APIView):
    def post(self, request):
        if "app_token" not in request.data:
            counter = 0
            token = ""
            while True:
                token = secrets.token_hex(16)
                check_tok = Account.objects.filter(app_token=token).exists()
                if check_tok==False or counter>=100:
                    break
                else:
                    counter+=1             
            request.data["app_token"] = token
        new_user = AccountSerializer(data=request.data)          
        if new_user.is_valid():
            new_user.save()
            return Response({"message":"Data is valid"}, status=status.HTTP_201_CREATED)
        return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)  
    def get(self, request):
        
        all_acc = Account.objects.all()
        ser_all_acc = AccountSerializer(all_acc, many=True).data
        return Response(ser_all_acc, status=status.HTTP_200_OK)
    

class AccountUserById(APIView):
    def get(self, request, id):
        try:
            account = Account.objects.get(id=id)
        except Account.DoesNotExist:
            return Response({"message":"requesed record not found"},  status=status.HTTP_404_NOT_FOUND)
        account = Account.objects.get(id=id)

        ser_acc = AccountSerializer(account)
        return Response(ser_acc.data, status=status.HTTP_200_OK)
    def put(self, request, id):
    
        account = get_object_or_404(Account, id=id)
        acc_ser = AccountSerializer(account,data=request.data)
        if acc_ser.is_valid():
            acc_ser.save()
            return Response({"message":"record updated successfully"}, status=status.HTTP_200_OK)
        
        return Response(acc_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        
        account = get_object_or_404(Account, id=id)
        
       
        requests.delete(f"http://127.0.0.1:8000/destination/api/{account.account_id}") 
        
        account.delete()
        
        return Response({"message": "account deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
class AccountUserByEmailId(APIView):
    def get(self, request, email_id):
       
        try:
            account = Account.objects.get(email_id=email_id)
        except Account.DoesNotExist:
            return Response({"message":"requesed record not found"},  status=status.HTTP_404_NOT_FOUND)
        account = Account.objects.get(email_id=email_id)

        ser_acc = AccountSerializer(account)
        return Response(ser_acc.data, status=status.HTTP_200_OK)
    def put(self, request, email_id):
    
        account = get_object_or_404(Account, email_id=email_id)
        acc_ser = AccountSerializer(account,data=request.data)
        if acc_ser.is_valid():
            acc_ser.save()
            return Response({"message":"record updated successfully"}, status=status.HTTP_200_OK)
        
        return Response(acc_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, email_id):
        account = get_object_or_404(Account, email_id=email_id)
        
       
        requests.delete(f"http://127.0.0.1:8000/destination/api/{account.account_id}") 
        
        account.delete()
        
        return Response({"message": "account deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class incomingData(APIView):
    def post(self, request):
        
        if "CL-X-TOKEN" not in request.headers:
            return Response({"message":"Un Authenticated"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            token = request.headers.get("CL-X-TOKEN")
            try:
                account = Account.objects.get(app_token=token)
            except Account.DoesNotExist:
                return Response({"message":"requesed record not found"},  status=status.HTTP_404_NOT_FOUND)
            account = Account.objects.get(app_token=token)

            ser_acc = AccountSerializer(account)
            
            
            data ={
                "account_id":account.account_id,
                "url":f"http://{request.META['SERVER_NAME']}:{request.META['SERVER_PORT']}",
                "http_method":request.method,
                "headers" : {
                        "APP_ID": account.account_id,
                        "APP_SECTET": token,
                        "ACTION": f"user.{request.method}",
                        "Content-Type": "application/json",
                        "Accept": "*"
                    }

            }
            req = requests.post("http://127.0.0.1:8000/destination/api", json=data, headers={"Content-Type":"application/json"})
            return Response({"message":"destination addedd"},  status=status.HTTP_201_CREATED)
    def get(self, request):
        
        return Response({"message":"asassa"},status=status.HTTP_405_METHOD_NOT_ALLOWED)


