from django.shortcuts import render, HttpResponse


# Create your views here.
def chgrecord_list(request):
    # return HttpResponse('Hello chage record.')
    return render(request, 'chgrecord/index.html')
