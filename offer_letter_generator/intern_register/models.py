from django.db import models

# Create your models here.
class HR(models.Model):
    h_name = models.CharField('HR Name', max_length=120)
    h_email_id = models.EmailField('HR Email Address')
    h_address = models.CharField(max_length=300)
    h_mob_num = models.CharField('HR Mobile Number', max_length=10)

    def __str__(self):
        return self.h_name


class Intern(models.Model):
    i_name = models.CharField('Name', max_length=120)
    i_email_address = models.EmailField('Email Address')
    i_mob_num = models.CharField('Mobile Number', max_length=10)
    i_address = models.CharField('Address',max_length=300)
    i_job_position = models.CharField('Job Position',max_length=120)
    i_stipend = models.CharField('Stipend', max_length=3)
    i_join_date = models.DateTimeField('Join Date')
    i_description = models.CharField('Job Description', max_length=150,blank= True, null=True)
    # hr_name = models.CharField('HR name', max_length=120)
    hr_name = models.ForeignKey(HR,blank = True, null = True, on_delete=models.CASCADE)
    hr_email = models.EmailField('HR Mail', max_length=150,null=True)

    def __str__(self):
        return self.i_name





