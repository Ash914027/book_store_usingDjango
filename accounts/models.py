# Model to track user logins
# (Remove this duplicate import section)
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
	# You can add extra fields here if needed
	phone = models.CharField(max_length=20, blank=True)
	address = models.TextField(blank=True)
class LoginRecord(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)
	ip_address = models.GenericIPAddressField(blank=True, null=True)

	def __str__(self):
		return f"Login by {self.user.username} at {self.timestamp}"





class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(blank=True)
	avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

	def __str__(self):
		return f"Profile of {self.user.username}"

# Signal to create or update Profile automatically
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	else:
		instance.profile.save()
