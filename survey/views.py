
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from .forms import SurveyForm
from .models import SurveyResponse


# Public homepage
def home(request):

    if request.method == 'POST':

        form = SurveyForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Survey submitted successfully!'
            )

            return redirect('home')

    else:
        form = SurveyForm()

    return render(
        request,
        'home.html',
        {'form': form}
    )


# Protected survey results page
@login_required
def results(request):

    responses = SurveyResponse.objects.all().order_by(
        '-submitted_at'
    )

    total_responses = responses.count()

    average_rating = responses.aggregate(
        Avg('rating')
    )['rating__avg']

    context = {
        'responses': responses,
        'total_responses': total_responses,
        'average_rating': average_rating,
    }

    return render(
        request,
        'results.html',
        context
    )
