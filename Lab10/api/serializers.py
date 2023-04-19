from api.models import Company, Vacancy
from rest_framework import serializers


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class CompanySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address')


class VacancySerializer1(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.TextField()
    salary = serializers.FloatField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('name', 'description', 'salary', 'company')
