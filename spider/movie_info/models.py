from django.db import models


class movieinfo(models.Model):
    id = models.AutoField(primary_key=True)
    mName=models.CharField(max_length=256)
    mDirectors=models.CharField(max_length=256)
    mScore=models.CharField(max_length=50)
    mQuote=models.CharField(max_length=256, null=True)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.mName,self.mDirectors,self.mActors,self.mType)