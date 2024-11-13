from rest_framework import serializers
from .models import Todo, Recommend


class TodoSerializer(serializers.ModelSerializer):
    class RecommendSerializerForTodo(serializers.ModelSerializer):
        class Meta:
            model = Recommend
            # fields = ("content",)
            exclude = ("todo",)


    # recommend_set = RecommendSerializerForTodo(many=True)
    # 역참조 필드 이름 바꾸기
    recommends = RecommendSerializerForTodo(many=True,source="recommend_set")

    class Meta:
        model = Todo
        fields = '__all__'
        # exclude = ("recommend_set",)

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('work', 'is_completed', )

class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = "__all__"
        read_only_fields = ("todo",)

