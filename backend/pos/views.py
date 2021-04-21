from drf_spectacular.utils import extend_schema
from rest_framework.generics import UpdateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .filters import OrderAdminFilter, OrderWaiterFilter, OrderCookFilter
from .serializers import CategorySerializer, OrderCookSerializer, ProductSerializer, \
    TableSerializer, OrderSingleSerializer, OrderItemSingleSerializer, OrderNestedSerializer
from .models.category import Category
from .models.order import Order
from .models.order_item import OrderItem
from .models.product import Product
from .models.table import Table
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from rest_framework.response import Response
from .permissions import IsAdmin, IsWaiter, IsCook


@extend_schema(description='Admin only')
class TableListCreateView(ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


@extend_schema(description='Admin only')
class TableSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


@extend_schema(description='Admin only')
class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated & IsAdmin]


@extend_schema(description='Admin only')
class CategorySingleView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated & IsAdmin]


@extend_schema(description='Admin only')
class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


@extend_schema(description='Admin only')
class ProductSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


@extend_schema(description='Admin and Waiter')
class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSingleSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsWaiter)]


@extend_schema(description='Admin and Waiter')
class OrderSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSingleSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsWaiter)]


@extend_schema(description='Admin and Waiter')
class OrderItemListCreateView(ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSingleSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsWaiter)]


@extend_schema(description='Admin only')
class OrderItemSingleView(RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSingleSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


@extend_schema(description='Admin and Waiter')
class OrderNestedAdminListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderNestedSerializer
    filterset_class = OrderAdminFilter
    permission_classes = [IsAuthenticated & (IsAdmin | IsWaiter)]

    def get(self, request, *args, **kwargs):
        order = Order.objects.all()
        filterset = OrderAdminFilter(request.GET, queryset=order)
        if filterset.is_valid():
            order = filterset.qs
        serializer = OrderNestedSerializer(order, many=True)
        total_income = order.aggregate(Sum('order_cost'))['order_cost__sum']
        return Response({'Total income': total_income if total_income else 0, 'Orders': serializer.data})


@extend_schema(description='Admin and Waiter')
class OrderNestedWaiterListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderNestedSerializer
    filterset_class = OrderWaiterFilter
    permission_classes = [IsAuthenticated & (IsAdmin | IsWaiter)]


@extend_schema(description='Admin and Cook')
class OrderItemCookerListView(ListAPIView):
    queryset = OrderItem.objects.all().order_by('is_ready')
    serializer_class = OrderCookSerializer
    filterset_class = OrderCookFilter
    permission_classes = [IsAuthenticated & (IsAdmin | IsCook)]


@extend_schema(description='Admin and Cook')
class OrderItemCookerUpdateView(UpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderCookSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsCook)]
