from datetime import datetime, timedelta, date
from django.db.models import Q, F
from django.db.models.functions import ACos, Sin, Cos, Radians
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from .models import TestCenter
from .serializer import RegistrationSerializer, TestCenterSerializer


@api_view(["GET"])
def Home(request):
    return HttpResponse("I'm home")


@api_view(['POST'])
def find_available_test_centers(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # Extract data from the serializer
            student_data = request.data
            student_date = student_data['test_date']
            student_time = student_data['test_timing']
            student_duration_str = student_data['test_duration']
            student_latitude = student_data['preferred_location_lat']
            student_longitude = student_data['preferred_location_long']


            # Convert student_time to a timedelta object
            student_time = datetime.strptime(student_time, "%H:%M:%H").time()
            

            # Parse student_duration_str into a timedelta object
            try:
                student_duration = timedelta(hours=float(student_duration_str))
            except ValueError:
                return JsonResponse({'detail': 'Invalid test_duration format.'}, status=status.HTTP_400_BAD_REQUEST)

            # Calculate the end time of the student's test
            student_start_datetime = datetime.combine(student_date, datetime.min.time()) + student_time
            student_end_datetime = student_start_datetime + student_duration

            # Check for available test centers
            available_test_centers = TestCenter.objects.filter(
                Q(test_timing__gte=student_end_datetime) | Q(test_timing__lte=student_start_datetime),
                capacity__gt=0
            ).annotate(
                distance=(
                    ACos(
                        Cos(Radians(student_latitude)) * Cos(Radians(F('location_lat'))) *
                        Cos(Radians(F('location_long')) - Radians(student_longitude)) +
                        Sin(Radians(student_latitude)) * Sin(Radians(F('location_lat')))
                    ) * 6371  # 6371 km is the Earth's radius
                )
            ).order_by('distance')

            if available_test_centers:
                test_center_serializer = TestCenterSerializer(available_test_centers, many=True)
                return JsonResponse(test_center_serializer.data, safe=False)
            else:
                return JsonResponse({'detail': 'No available test centers found.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
