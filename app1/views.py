from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import math



def dist(n1,n2):
    dim_no = len(n1)
    sum = 0
    i=0
    while i < dim_no:
        sum += pow(n2[i] - n1[i],2)
        i+=1

    distance = math.sqrt(sum)
    return distance


def index(request):

    list1 = [3, 4, 5, 6]
    list2 = [3, 4, 4, 4]

    #list2[2] = 5

    out_var = dist(list1, list2)
    return render(request, 'app1/index.html', {'out_var': out_var})

