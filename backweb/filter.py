"""
author:何凯
date:
"""
import django_filters
from rest_framework import filters
from backweb.models import Article,ArticleType

class ArticleFilter(filters.FilterSet):
    title = django_filters.CharFilter('title',lookup_expr = 'contains')
    word = django_filters.CharFilter('search_words',lookup_expr = 'contais')
    before_time = django_filters.DateTimeFilter('update_time',lookup_expr = 'lt')
    after_time = django_filters.DateTimeFilter('update_time',lookup_expr = 'gt')
    type = django_filters.CharFilter('article_type',lookup_expr = 'contains')
    class Meta:
        model = Article
        fields = ['title','search_words','update_time','article_type']