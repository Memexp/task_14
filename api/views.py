from rest_framework.generics import ListAPIView
from restaurants.models import Restaurant
from .serialize import RestaurantListSerializer

# Complete me! I should be your APIListView
class RestaurantListView(ListAPIView):
	queryset= Restaurant.objects.all()
	serializer_class = RestaurantListSerializer