from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime

from .models import format_duration


def storage_information_view(request):
    # Программируем здесь
    non_leaved_visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []

    for visit in non_leaved_visits:
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(visit.get_duration()),
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
