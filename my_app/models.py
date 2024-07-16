from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return(f'{self.first_name} {self.last_name}')
    

class AccountsApp(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, default=1, blank=False, null=False)
    account_name = models.CharField(max_length=20)

    def __str__(self):
        return(f'{self.account_name} ')
    

class PersonAccount(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, default=1, null=False, blank=False)
    account_app = models.ForeignKey(AccountsApp, on_delete=models.CASCADE, null=False, blank=False)
    account_url = models.URLField(max_length=50)
    password = models.CharField(max_length=20)
    notes = models.CharField(max_length=250)

    def __str__(self):
        return(f'{self.person} {self.account_app}')