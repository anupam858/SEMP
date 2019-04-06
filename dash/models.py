from djongo import models
from datetime import datetime
# Create your models here.

class OrganiList(models.Model):

      user_id = models.CharField(max_length= 50)

      class Meta:
            abstract = True

class SlotF(models.Model):

      date = models.DateField()
      time_s = models.TimeField()
      time_e = models.TimeField()

      class Meta:
            abstract = True

class Voccupy(models.Model):

      eid = models.CharField()
      edate = models.DateField()
      etime_s = models.TimeField()
      etime_e = models.TimeField()

      class Meta:
            abstract = True
            
      
class task_list(models.Model):

      task_line = models.CharField(max_length= 100,)
      task_stata = models.BooleanField()

      class Meta:
            abstract = True



            
class Events(models.Model):

      event_name = models.CharField(max_length= 50, blank= False)
      e_date = models.DateField(blank= False)
      Venue = models.CharField(max_length= 20)
      E_ptime_s = models.TimeField(auto_now= False)
      E_ptime_e = models.TimeField(auto_now= False)
      optional = models.BooleanField()
      slot1= models.ArrayModelField(model_container = SlotF)
      slot2 = models.ArrayModelField(model_container = SlotF)
      Venue_s = models.CharField(max_length= 20)
      rp = models.CharField(max_length= 50, blank= False)
      organi_names = models.ArrayModelField(model_container = OrganiList,null= True)
      enotes = models.TextField()
      active_stat = models.BooleanField()


      def __str__(self):

            return self.event_name


class Venue(models.Model):

      v_name = models.CharField(max_length= 20)
      room_no = models.CharField(max_length= 5,unique= True)
      floor = models.CharField(max_length= 10)
      capacity = models.IntegerField()
      occupancy = models.ArrayModelField(model_container = Voccupy)



      def __str__(self):

            return self.v_name

      

class Tasks(models.Model):

      e_id = models.CharField(max_length=20,)
      User_id = models.CharField(max_length= 50)
      Rp_id = models.CharField(max_length= 50)
      tasks = models.ArrayModelField(model_container= task_list)


      def __str__(self):

            return self.e_id
 

class UserRequest(models.Model):

      org_id = models.CharField(max_length=50, blank=True)
      name = models.CharField(max_length= 30)
      email = models.EmailField(max_length=50, blank=True, unique= True)
      phone = models.CharField(max_length=12, blank=True)
      designation = models.CharField(max_length= 30)
      gen_id = models.CharField(max_length= 15)

      def __str__(self):

            return self.email

      
      
      
      
