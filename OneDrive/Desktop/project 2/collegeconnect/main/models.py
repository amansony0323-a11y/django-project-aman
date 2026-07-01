from django.db import models
from django.contrib.auth.models import User

# Role choices
ROLE_CHOICES = (
    ('student', 'Student'),
    ('college', 'College'),
    ('admin', 'Admin'),
)


# -----------------------
# Profile Model
# -----------------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='student'
    )

    phone = models.CharField(max_length=15, blank=True)
    college_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


# -----------------------
# Event Model
# -----------------------
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_events"
    )

    def __str__(self):
        return self.title


# -----------------------
# Registration Model
# -----------------------
# -----------------------
# Registration Model
# -----------------------
class Registration(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="registrations"
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="registrations"
    )

    registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} → {self.event.title}"


# -----------------------
# Notification Model
# -----------------------
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message