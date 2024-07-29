from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer, Plan

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'description', 'price']

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    plan = PlanSerializer()

    class Meta:
        model = Customer
        fields = ['id', 'user', 'plan', 'name', 'email']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        plan_data = validated_data.pop('plan')
        user = UserSerializer().create(user_data)
        plan = Plan.objects.get(id=plan_data['id'])
        customer = Customer.objects.create(user=user, plan=plan, **validated_data)
        return customer


