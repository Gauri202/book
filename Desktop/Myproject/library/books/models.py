from email.policy import default
from tabnanny import verbose
from tkinter import CHAR
from xml.dom import ValidationErr
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator 
from datetime import datetime

alphabets = RegexValidator(r'^[a-zA-Z]','Only alphanumeric characters are allowed.')

class Books(models.Model):
  booktitle = models.CharField(max_length=100, blank=True,validators=[alphabets])
  author = models.CharField(max_length=100, blank=True,validators=[alphabets])
  bookcode = models.IntegerField(default='')
  class Meta:
    verbose_name_plural = "books"
     
  def __str__(self):
    return self.booktitle
       
       
class Student(models.Model):
  Name = models.CharField(max_length=100,null=0)
  Class = models.CharField(max_length=100)
  #books = models.ForeignKey(to=Books, on_delete=models.CASCADE)
  #phone = models.IntegerField(default=0)
  book_issued = models.CharField(max_length=100,default=0)

  
  class Meta:
    verbose_name_plural = "Student"

  def __str__(self):
    return self.Name

       
    

 
  