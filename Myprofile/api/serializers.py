from rest_framework.serializers import  ModelSerializer, SerializerMethodField

from Myprofile.models import Post, Comments


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'id',
            'post',
            'user',
            'comment',
            'date',
        ]


class CreatePostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
        
            'post',
            'image',
        ]



class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'post',
            'likee',
            'image',
            'date',
        ]

class PostDetailSerializer(ModelSerializer):
    user  = SerializerMethodField()
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'post',
            'image',
            'likee',
            'date',
            'comments',
        ]
    def get_user(self, obj):
        return str(obj.user.username)

    def get_comments(self, obj):
        c_qs = Comments.objects.all().filter(post=obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments

