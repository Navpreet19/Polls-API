from polls.models import Question, Choices
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from polls.serializers import QuestionSerializer, QuestionDetailSerializer
from django.http import HttpResponse, JsonResponse


# class QuestionList(APIView):
# def polls_list(request):
#     if request.method == 'GET':
#         questions = Question.objects.all()
#         serializer = QuestionSerializer(questions, many=True)
#         return JsonResponse(serializer.data, safe=False)

class QuestionList(APIView):
    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
        

class QuestionDetail(APIView):
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        # choices = question.choices_set.all()
        serializer = QuestionDetailSerializer(question)
        return Response(serializer.data)