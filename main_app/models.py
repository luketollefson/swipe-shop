from django.db import models


class Users(models.Model):
    username = models.CharField(
        primary_key=True,
        max_length=25,
    )
    password = models.CharField(
        max_length=100,
    )
    bio = models.TextField(
        blank=True,
        null=True,
    )
    profilePicture = models.ImageField(
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username


class Messages(models.Model):
    MessageID = models.AutoField(
        primary_key=True,
    )
    UserIDFrom = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
        related_name='userFrom',
    )
    UserIDTo = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
        related_name='userTo',
    )
    MessageSent = models.DateTimeField(auto_now=True)
    ProductID = models.ForeignKey(
        'Products',
        on_delete=models.CASCADE,
        related_name='message_product',
    )
    MessageBody = models.TextField()

    def __str__(self):
        return str(self.MessageID)


class Products(models.Model):
    ProductID = models.AutoField(
        primary_key=True,
    )
    UserID = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
        related_name='user',
    )
    ProductName = models.CharField(
        max_length=250,
    )
    Price = models.PositiveSmallIntegerField()
    Description = models.TextField(
        blank=True,
        null=True,
    )
    Picture1 = models.ImageField(
        blank=True,
        null=True,
    )
    Picture2 = models.ImageField(
        blank=True,
        null=True,
    )
    Picture3 = models.ImageField(
        blank=True,
        null=True,
    )
    Picture4 = models.ImageField(
        blank=True,
        null=True,
    )
    Picture5 = models.ImageField(
        blank=True,
        null=True,
    )
    Picture6 = models.ImageField(
        blank=True,
        null=True,
    )
    Picture7 = models.ImageField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.ProductID)


class Likes(models.Model):
    likeId = models.AutoField(
        primary_key=True,
    )
    user = models.ForeignKey(
        'Users',
        unique=False,
        on_delete=models.CASCADE,
        related_name='like_users',
        null=True,
    )
    product = models.ForeignKey(
        'Products',
        on_delete=models.CASCADE,
        related_name='liked_product',
    )

    def __str__(self):
        return str(self.likeId)


class Hates(models.Model):
    HateID = models.AutoField(
        primary_key=True,
    )
    user = models.ForeignKey(
        'Users',
        unique=False,
        on_delete=models.CASCADE,
        related_name='hate_users',
        null=True,
    )
    product = models.ForeignKey(
        'Products',
        on_delete=models.CASCADE,
        related_name='hated_product',
    )

    def __str__(self):
        return str(self.HateID)
