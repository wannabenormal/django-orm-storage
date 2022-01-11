from datacenter.models import Passcard
from django.shortcuts import render

from .models import format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = passcard.visit_set.all()

    # Программируем здесь

    this_passcard_visits = []

    for visit in visits:
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'leaved_at': visit.leaved_at,
                'duration': format_duration(visit.get_duration()),
                'is_strange': visit.is_visit_long(),
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
