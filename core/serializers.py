from rest_framework import serializers
from .models import Post,Like
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = super(self.__class__, self).create(validated_data)
        return user

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = super().update(instance, validated_data)
        return user


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at','user')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id','title','description','content','type','created_at',
            'updated_at','owner','total_likes','total_dislikes','total_vote_count',
        ]
        read_only_fields = ('created_at', 'updated_at', 'owner',)


class PostDetailSerializer(serializers.ModelSerializer):
    like_set = LikeSerializer(read_only=True,many=True)
    class Meta:
        model = Post
        fields = [
            'id','title','description','content','type','created_at',
            'updated_at','owner','total_likes','total_dislikes','total_vote_count','like_set',
        ]
        read_only_fields = ('created_at', 'updated_at', 'owner',)