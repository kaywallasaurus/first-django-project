from django.http import JsonResponse

# Create your views here.

data = {
   "Name": "Kayla Wong",
   "Track": "Backend(Python)",
   "Message": "Loving all of the things I've learned so far!"
}


def index(request):
    return JsonResponse(data)
