from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
import spacy

# Create your views here.
class Main(APIView):

    def post(self,request):
        try:
            nlp = spacy.load('en_core_web_sm')
            about_doc = nlp(request.data['paragraph'])
            data = []
            for token in about_doc:
                print (type(str(token)))
                data.append({'word':str(token), 'pos':token.pos_ ,'explain':spacy.explain(token.tag_)})
            return Response(data)
        except:
            print("An exception occurred")
            dta  = {"message":"An exception occurred"}
            return Response(dta)