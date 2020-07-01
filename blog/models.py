from django.db import models




# Create a BLog Models
#title
#pub_date
#body
#image

# Add the blog app to the settings --> en settings.py del project

#create a migrations --> terminal= python3 manage.py makemigrations

#Migrate --> python3 manage.py migrate

#add to the admin -->admin.py del model que estoy trabajando


class Blog(models.Model):
    image= models.ImageField(upload_to='images/')
    title= models.CharField(max_length=255)
    pu_date= models.DateTimeField()
    body= models.TextField()
    
