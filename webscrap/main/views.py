from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .models import WebContent, Detail
from .form import TextForward
import openai
import requests
from bs4 import BeautifulSoup
from django.conf import settings
# Create your views here.

openai_api_key='somekey'
openai.api_key=openai_api_key

def scrape_website_text(url):
    response = requests.get(url)
    print(response)
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the paragraph elements in the HTML
        paragraph_elements = soup.find_all('p')

        # Extract the text from the paragraph elements
        paragraphs = [p.get_text() for p in paragraph_elements]
        message=''
        for x in paragraphs:
            message+=x
        return message
    return None

def ask_openai(message):
    message=settings.CURRENT_ARTICLE+message
    if "<" in message and ">"in message:
        start= message.index("<")
        end=message.index(">")
        settings.CURRENT_ARTICLE=scrape_website_text(message[start+1:end])
        message= 'summarize this:'+settings.CURRENT_ARTICLE
    print(message)
    response=openai.Completion.create(
        model='text-davinci-003',
        prompt= message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer=response.choices[0].text.strip()
    return answer

def index(response,id):
    ls = WebContent.objects.get(id=id)
    return render(response, "main/list.html",{"ls":ls})
def index2(request):
    if request.method == "POST":
        message= request.POST.get('message')
        response= ask_openai(message)
        return JsonResponse({'message':message,'response':response})
    return render(request, "main/webscrap.html",{})
def home(response):
    return render(response, "main/home.html",{"name": "test"})
