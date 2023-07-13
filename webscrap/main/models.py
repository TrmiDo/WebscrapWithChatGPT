from django.db import models

# Create your models here.
class WebContent(models.Model):
    webname= models.CharField(max_length=400)
    def __str__(self):
        return self.webname

class Detail(models.Model):
    websource= models.ForeignKey(WebContent, on_delete=models.CASCADE)
    weblink= models.CharField(max_length=200)
    webinfo= models.CharField(max_length=1000)
    def __str__(self):
        return self.weblink


