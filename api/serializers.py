from rest_framework import serializers
from  .models import Removebg


# Serializers define the API representation.
class RemovebgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Removebg
        fields = ['id','images']




class RemovebgUpdateSerializer(serializers.ModelSerializer):
	
	class Meta:
		 model = Removebg
		 fields = ['id','images']


class RemovebgPostSerializer(serializers.ModelSerializer):
	images = serializers.ImageField(max_length=None,use_url=True)
	class Meta:
		model = Removebg
		fields = ('id','images')
	def create(self, validated_data):
		return Removebg.objects.create(**validated_data)




