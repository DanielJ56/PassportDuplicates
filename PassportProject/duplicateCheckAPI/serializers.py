from rest_framework import serializers
from duplicateCheckAPI.models import PERSON

class PERSONSerializer(serializers.ModelSerializer):
    class Meta:
        model = PERSON
        fields = ("person_id","reserved_user_id","first_name",
                 "last_name","birthdate","gender",
                 "passport_num","passport_num_salt","passport_photo")
