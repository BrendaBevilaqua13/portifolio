from django.db import models

# Model About

class About(models.Model):
    title = models.CharField(max_length=60)
    short_description = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title

# Model Skills
class Skills(models.Model):
    title = models.CharField(max_length=20)
    short_description = models.TextField()
    image= models.ImageField(upload_to='skills')

    def __str__(self):
        return self.title

# Model Projects
class Projects(models.Model):
    title = models.CharField(max_length=60)
    short_description = models.TextField()
    image = models.ImageField(upload_to='projects')

    def __str__(self):
        return self.title

# Model Contact 
class Contact(models.Model):
    title = models.CharField(max_length=20)
    short_description = models.TextField()
    telephone = models.CharField(max_length=15)
    email = models.EmailField(max_length=80)
    github = models.CharField(max_length=80)
    linkedIn = models.CharField(max_length=80)

    def __str__(self):
        return self.title
