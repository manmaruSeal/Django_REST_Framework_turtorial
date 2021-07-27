from rest_framework import serializers
from .models import User, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name', 'mail')
        #read_only_fields = ('name', 'mail')



class PostSerializer(serializers.ModelSerializer):
    #author = UserSerializer(read_only=True)
    #authorのserializerを上書き、一覧でユーザ情報が見れるようになる
    #POSTできなくなる。。。
    #author = UserSerializer()
    class Meta:
        model = Post
        fields = ('id','title', 'body', 'created_at', 'status', 'author')
        