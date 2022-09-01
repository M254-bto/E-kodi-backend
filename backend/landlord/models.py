from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save




class Landlord(User, models.Model):
    contact = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Landlord'
        verbose_name_plural = 'Landlords'
       


class Profile(models.Model):
    user = models.OneToOneField(Landlord, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)




class Appartments(models.Model):
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    units = models.IntegerField()
    unit_price = models.IntegerField()

    


    def __str__(self):
        return f'{self.name}'

    
    class Meta:
        verbose_name = 'Appartment'
        verbose_name_plural = 'Appartments'

    
# class AppartmentToken(models.Model):
#     appartment = models.OneToOneField(Appartments, on_delete=models.CASCADE, related_name='app_token')
#     token = models.CharField(max_length=100)

#     @classmethod
#     def generate_key(cls):
#         return binascii.hexlify(os.urandom(20)).decode()


#     def __str__(self):
#         return f'{self.appartment.name}{self.token}'

#     class Meta:
#         verbose_name = 'Appartment Token'
#         verbose_name_plural = 'Appartment Tokens'

    