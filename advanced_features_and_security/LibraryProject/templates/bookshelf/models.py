from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
["class CustomUser(AbstractUser):", "date_of_birth", "profile_photo"]
 ["class CustomUserManager(BaseUserManager):", "create_user", "create_superuser"]
["can_create", "can_delete"]
    def _ _str_ _(self)
    return f"{self.title} ({self.publication_year})"