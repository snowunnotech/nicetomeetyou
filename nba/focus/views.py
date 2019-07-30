from django.shortcuts import render
from rest_framework import status

from .models import Entry
from .serializers import EntrySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def index(request):
    return render(request, 'focus/index.html')

@api_view(['GET'])
def enrty_list(request):
    entry = Entry.objects.all()
    serializer = EntrySerializer(entry,many=True)
    return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def entry_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        entry = Entry.objects.get(pk=pk)
    except Entry.DoesNotExist:
        print('not found')
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = EntrySerializer(entry)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = EntrySerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
