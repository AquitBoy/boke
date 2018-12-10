from django.db import models


class User(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    user_desc = models.CharField(max_length = 1000,null = True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'


class ArticleType(models.Model):
    types = models.CharField(max_length = 20)

    class Meta:
        db_table = 'articletype'


class Article(models.Model):
    title = models.CharField(max_length = 50,unique = True)
    content = models.TextField(null = True)
    is_delete = models.BooleanField(default = 0)
    desc = models.CharField(max_length = 200,null = True)
    icon = models.ImageField(upload_to = 'art_img',null = True)
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    article_type = models.ForeignKey(ArticleType)
    search_words = models.CharField(max_length = 50,null = True)
    class Meta:
        db_table = 'article'



