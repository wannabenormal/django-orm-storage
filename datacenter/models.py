from django.db import models
from django.utils.timezone import localtime


def format_duration(duration):
    remaining_seconds = duration.total_seconds()
    hours = int(remaining_seconds // 3600)
    remaining_seconds = remaining_seconds - hours * 3600
    minutes = int(remaining_seconds // 60)
    seconds = int(remaining_seconds - minutes * 60)

    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )

    def get_duration(self):
        time_end = localtime(self.leaved_at)
        return time_end - localtime(self.entered_at)

    def is_visit_long(self, max_minutes=60):
        visit_minutes = self.get_duration().total_seconds() // 60

        return visit_minutes >= max_minutes
