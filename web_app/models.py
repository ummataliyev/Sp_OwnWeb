from django.db import models
from django.utils import timezone
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Certificate.Status.Published) # noqa


class Comments(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    comment = models.TextField(blank=False)
    image = models.ImageField(null=True, upload_to='profile', default='profile/default.jpeg') # noqa
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


@property
def imageURL(self):
    """This function is used to fix image URLs."""
    try:
        url = self.image.url
    except Exception:
        url = ""

    return url


class MyResume(models.Model):
    file = models.FileField(upload_to='files/', default='resume.pdf')

    def __str__(self):
        return str(self.file)


class ProjectCategory(models.Model):
    name = models.CharField(max_length=500, null=True, blank=False)

    def __str__(self):
        return self.name


class MyProjects(models.Model):

    SIDE_CHOICES = (
        ("left", "left"),
        ("right", "right"),
    )

    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, null=True) # noqa
    side = models.CharField(blank=False, null=True, choices=SIDE_CHOICES, max_length=5) # noqa
    image = models.ImageField(null=True, blank=False)
    title = models.CharField(max_length=27, null=True, blank=False)
    body = models.CharField(max_length=500, null=True, blank=False)
    link = models.CharField(max_length=255, null=True, blank=False)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['published']


class MyBots(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, null=True) # noqa
    name = models.CharField(max_length=30, null=True, blank=False)
    image = models.ImageField(null=True, blank=False)
    link = models.CharField(max_length=255, null=True, blank=False)
    file = models.FileField(upload_to='videos/', null=True, verbose_name="Short Video") # noqa
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['published']


class GetInTouch(models.Model):
    fullname = models.CharField(max_length=255, null=True, blank=False)
    email = models.EmailField(max_length=255, null=True, blank=False)
    body = models.TextField(blank=False)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class Certificate(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="certificates/images")
    publish_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.Draft
    )
    objects = models.Manager()  # default manager
    published = PublishedManager()

    class Meta:
        ordering = ["-publish_time"]

    def __str__(self):
        return self.title

    # def get_queryset(self):
    #     return super().get_queryset().filter(status=Certificate.Status.Published.name) # noqa
