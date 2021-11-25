from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room, UserCall


@login_required
def index(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.order_by("title")

    # Render that in the index template
    return render(request, "index.html", {
        "rooms": rooms,
    })


@login_required
def user_button_calls(request):
    """
    user button calls page view.
    Ideally the business logic should be in interactors/services, also we shouldn't be accessing models directly
    we can have storages or daos to interact with db
    """
    # Get button calls made by the user
    button_calls = UserCall.objects.select_related('button_type').filter(user=request.user)
    # Render that in the button_calls template
    return render(request, "button_calls.html", {"button_calls": button_calls})
