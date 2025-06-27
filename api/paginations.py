from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_query_param = 'page-num'
    page_size_query_param = 'page-size'
    max_page_size = 1

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data,
            'page_size': self.page_size,
        })