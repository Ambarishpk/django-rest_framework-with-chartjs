from django.views.generic import View
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import  JsonResponse
import csv


with open('charts/samplefiles/samplefile1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    columns = []
    records = []
    for row in csv_reader:
        if line_count == 0:
            columns.append(row)
            line_count += 1
        else:
            for i in row:
                records.append(int(i))
    


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "data" : records,
            "labels" : columns[0],
            "label" :'S Grade Students',
        }   

        return JsonResponse(data)
    
class ChartData3(APIView):
    def get(self, request, format=None):
        data = {
            "data": [10, 15, 23, 14, 33, 56, 76],
            "labels": ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'],
            "label": "Studies Hours"
        } 
        
        return JsonResponse(data)
    
    
class ChartData2(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "labels": ["SOA", "CNS", "CLOUD", "IR", "GTA", "RMT"],
            "data": [80, 60, 95, 75, 55, 50],
            "label" :'Passed Students',
        }   

        return JsonResponse(data)