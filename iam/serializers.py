from rest_framework import serializers
from .models import User, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'bin', 'requisites', 'created_at']
        read_only_fields = ['id', 'created_at']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'company', 'is_self_employed']
        read_only_fields = ['id', 'role', 'company']



class RegisterContractorSerializer(serializers.Serializer):
    """Регистрация исполнителя — без company"""
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    is_self_employed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=User.Role.CONTRACTOR,
            is_self_employed=validated_data.get('is_self_employed', False),
        )
        return user



class RegisterCompanySerializer(serializers.Serializer):
    """ register company + 1 user admin """
    company_name = serializers.CharField(max_length=255)
    bin = serializers.CharField(max_length=20, required=False, allow_blank=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)

    def create(self, validated_data):
        company = Company.objects.create(
            name = validated_data['company_name'],
            bin = validated_data.get('bin', '')
        )

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=User.Role.ADMIN,
            company=company
        )
        return user