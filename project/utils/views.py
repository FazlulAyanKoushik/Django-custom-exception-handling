# views.py

from django.http import JsonResponse


def custom_404_view(request, exception):
    return JsonResponse({
        'error': 'Endpoint not found.',
        'status_code': 404
    }, status=404)


def custom_500_view(request):
    return JsonResponse({
        'error': 'Server error. Please try again later.',
        'status_code': 500
    }, status=500)
