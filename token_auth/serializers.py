from .models import Courses, Instructor
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ["id", "tittle", "rating", "instructor"]


class InstruSerializer(serializers.ModelSerializer):
    # courses = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='courses-detail')
    courses = CourseSerializer(many=True)
    total_courses = serializers.IntegerField(
                    source='courses.count',
                    read_only=True
          )

    class Meta:
        model = Instructor
        fields = ["id", "name", "email", "total_courses", "courses"]

    def create(self, validated_data):
        print(f"validated data...................{validated_data}")
        tracks_data = validated_data.pop('courses')
        print(tracks_data)
        inst = Instructor.objects.create(**validated_data)
        print(inst.id)
        print(inst)
        for track_data in tracks_data:
            Courses.objects.create(tittle=track_data['tittle'], rating=track_data["rating"], instructor=inst)
        return inst

    def update(self, instance, validated_data):
        # print(f"validated data...................{validated_data}")
        # print(f"instanc data...................{instance}")
        # print(f"vali data...................{validated_data}")
        tracks_data = validated_data.pop('courses')
        # print(f"instanc data...................{validated_data}")
        instance.name = validated_data['name']
        instance.email = validated_data['email']
        coursz = (instance.courses).all()
        print(type(coursz), "here is type.....................................")
        coursz = list(coursz)
        print(type(coursz), "here is type.....................................")

        for item in tracks_data:
            if coursz:
                cours = coursz.pop(0)
                print(cours)
                print(item)
                # Courses.objects.get_or_create(tittle=item['tittle'], rating=item["rating"], instructor=instance)
                cours.tittle = item["tittle"]
                cours.rating = item["rating"]
                cours.save()
            else:
                Courses.objects.create(tittle=item['tittle'], rating=item["rating"], instructor=instance)
        instance.save()
        return instance

    # def update(self, instance, validated_data):
    #     # print(f"validated data...................{validated_data}")
    #     # print(f"instanc data...................{instance}")
    #     # print(f"vali data...................{validated_data}")
    #     tracks_data = validated_data.pop('courses')
    #     # print(f"instanc data...................{validated_data}")
    #     instance.name = validated_data['name']
    #     instance.email = validated_data['email']
    #     for item in tracks_data:
    #         Courses.objects.get_or_create(tittle=item['tittle'], rating=item["rating"])
    #     instance.save()
    #     return instance
