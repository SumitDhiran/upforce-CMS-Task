from rest_framework.permissions import BasePermission
from .models import Post


class UserPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.user == obj


class PostPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.user == obj.owner

class LikePermission(BasePermission):

    def has_permission(self, request, view):
        post_id = request.data.get('post',None)
        try:
            post = Post.objects.get(id=post_id)
        except Exception as e:
            self.message = 'Post does not Exists.'
            return False

        if post.type == "Private" and post.owner != request.user:
            return False

        return True