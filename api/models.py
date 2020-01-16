from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    pw = models.CharField(max_length=65)

    def register(self, cd):
        self.name = cd['name']
        self.email = cd['email']
        self.pw = encrypt(cd['pw'])
        self.save_into_cache()
        self.save()

    def save_into_cache(self):
        user_dict = json.dumps(to_dict(self.name, self.email, self.pw), ensure_ascii=False).encode('utf-8')
        cache.set(self.email, user_dict, timeout=EXPIRE_DAY)

    def __str__(self):
        return self.email
