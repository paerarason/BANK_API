from django.db import models
class Banks(models.Model):
    bank_name = models.CharField(max_length=49, blank=True, null=True)
    bank_id = models.BigIntegerField(primary_key=True)
    def __str__(self):
        return self.bank_name
class Branch(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=11)
    bank = models.ForeignKey(Banks, on_delete=models.CASCADE,related_name="bank_in_branch",blank=True, null=True)
    branch = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.ifsc
