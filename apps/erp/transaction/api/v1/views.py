from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .serializers import SaleTransactionSerializer, SaleTransactionItemSerializer
from ...models import SaleTransaction, SaleTransactionItem


class SaleTransactionAPI(APIView):

    def get_object(self, pk):
        try:
            return SaleTransaction.objects.get(id=pk)
        except SaleTransaction.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        sale_transaction = self.get_object(pk)
        serializer = SaleTransactionSerializer(sale_transaction)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = SaleTransactionSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.save():
                return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        object = self.get_object(pk)
        serializer = SaleTransactionSerializer(object, data=request.data)
        if serializer.is_valid():
            if serializer.save():
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, * args, **kwargs):
        sale_transaction = self.get_object(pk)
        sale_transaction.delete()
        sale_transaction.save()
        return Response(status.HTTP_204_NO_CONTENT)


class SaleTransactionItemAPI(APIView):

    def get_object(self, pk):
        try:
            return SaleTransactionItem.objects.get(id=pk)
        except SaleTransactionItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):

        sale_transaction_item = self.get_object(pk)
        serializer = SaleTransactionItemSerializer(sale_transaction_item)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = SaleTransactionItemSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.save():
                return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        object = self.get_object(pk)
        serializer = SaleTransactionItemSerializer(object, data=request.data)
        if serializer.is_valid():
            if serializer.save():
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        print("dentro delete pk :: ", pk)
        sale_transaction_item = self.get_object(pk)
        print("sale_transaction_item :: ", sale_transaction_item)

        if sale_transaction_item.delete():
            print('funcao delete ativada como true')
        else:
            print('funcao delete ativada como false')

        # sale_transaction_item.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
