#from django.db import models
from djongo import models
from django import forms
from SEMP.settings import DBNAME



# Create your models here.

class UserAssociation(models.Model):

      event_id = models.CharField(max_length=20, null= True, default= 'noid')
      event_name = models.CharField(max_length=50, null= True, default= 'noname')

      class Meta:
            abstract = True
            
      def __str__(self):
           
            return self.event_id

class UserAssociationForm(forms.ModelForm):

      class Meta:
            model = UserAssociation
            fields = ('event_id', 'event_name')

class UserCollection(models.Model):
      
      org_name= models.CharField(max_length=120,blank=True)
      org_id = models.CharField(max_length=50, blank=True)
      email = models.EmailField(max_length=50, blank=True, unique= True)
      phone = models.CharField(max_length=12, blank=True)
      name = models.CharField(max_length= 30)
      designation = models.CharField(max_length= 30)
      gen_id = models.CharField(max_length= 15)
      user_type = models.CharField(max_length=200)
      user_acctd = models.ArrayModelField(model_container= UserAssociation, model_form_class=UserAssociationForm,)

      objects = models.DjongoManager()

      def __str__(self):

            return self.org_name
 


      
