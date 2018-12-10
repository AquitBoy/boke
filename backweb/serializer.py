"""
author:何凯
date:
"""
from rest_framework import serializers
from backweb.models import Article


class BackWebSerializers(serializers.ModelSerializer):
    # 对Article字段序列化；保证数据的可靠
    # 个人博客不想过多限制
    title = serializers.CharField(min_length = 1,
                                  error_messages = {
                                      'required': '标题必填'
                                      })

    class Meta:
        model = Article
        fields = ['article_type','title', 'desc', 'content', 'update_time', 'icon']

    def to_representation(self, instance):
        # 对序列化结果中的article_type进行处理
        data = super().to_representation(instance)
        data['article_type'] = instance.article_type.types
        return data
