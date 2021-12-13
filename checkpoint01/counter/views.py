from django.shortcuts import render

from .models import Person, Counter
from .serializers import CounterSerializer, PersonSerializer
from django.http import JsonResponse


def persons_json(request):
    persons = Person.objects.all()
    serizalizer = PersonSerializer(persons, many=True)
    return JsonResponse(serizalizer.data, safe=False, status=200)

def increment_counter(request, cid):
    counter = Counter.objects.get(id=cid)
    counter.counter_value += 1
    counter.save()
    serializer = CounterSerializer(counter)
    return JsonResponse(serializer.data, safe=False, status=200)