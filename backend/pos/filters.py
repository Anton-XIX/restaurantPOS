from django_filters import DateRangeFilter, DateFilter, FilterSet, NumberFilter


class OrderAdminFilter(FilterSet):
    order_id = NumberFilter(field_name='id')
    date_range = DateRangeFilter(field_name="start_date")
    start_date = DateFilter(field_name="start_date", lookup_expr='gte')
    end_date = DateFilter(field_name="start_date", lookup_expr='lte')
    table_id = NumberFilter(field_name='table')


class OrderWaiterFilter(FilterSet):
    order_id = NumberFilter(field_name='id')
    table_id = NumberFilter(field_name='table')


class OrderCookFilter(FilterSet):
    order_id = NumberFilter(field_name='order')
    table_id = NumberFilter(field_name='order__table')