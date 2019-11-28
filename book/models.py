from django.conf import settings
from django.db import models
from django.utils import timezone

class General_employee(models.Model):
    user_id= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, primary_key=True)
    name= models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    publisher=models.CharField(max_length=30)
    enrolled_date = models.DateTimeField(default=timezone.now)

    

    def enroll(self):
        self.enrolled_date= timezone.now()
        self.save()

        def __str__(self):
            return self.title
            return self.author
            return self.publisher


# Create your models here.
class Book_record(models.Model):
    book_record_id=models.IntegerField(primary_key=True)
    book_id = models.ForeignKey('Book',to_field='book_id',on_delete=models.PROTECT)
    user_id = models.ForeignKey('General_employee',to_field='user_id',on_delete=models.PROTECT)
    starting_rent = models.DateTimeField(default=timezone.now)
    finishing_rent= models.DateTimeField(default=timezone.now)

    def rent(self):
        self.starting_rent= timezone.now()
        self.save()

    def return_book(self):
        self.finishing_rent= timezone.now()
        self.save()



class Reservation(models.Model):
    reservation_id=models.IntegerField(primary_key=True)
    book_id = models.ForeignKey('Book',to_field='book_id',on_delete=models.PROTECT)
    user_id= models.ForeignKey('General_employee',to_field='user_id',on_delete=models.PROTECT)
    reservation_number= models.CharField(max_length=30)

    def reservation(self):
        self.reservation_date= timezone.now()
        self.save()


class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey('Book',to_field='book_id',on_delete=models.PROTECT)
    user_id = models.ForeignKey('General_employee',to_field='user_id',on_delete=models.PROTECT)
    published_date = models.DateTimeField(default=timezone.now)
    review=models.TextField()

    def publish(self):
        self.published_date= timezone.now()
        self.save()
