from django.contrib.auth.models import User
from django.db import models

from .enums import ButtonChoices


class BaseModel(models.Model):
    created_at = models.DateTimeField(blank=True, null=False, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=False, auto_now_add=True)

    class Meta:
        abstract = True


class Room(models.Model):
    """
    A room for people to chat in.
    """

    # Room title
    title = models.CharField(max_length=255)

    # If only "staff" users are allowed (is_staff on django's User)
    staff_only = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def group_name(self):
        """
        Returns the Channels Group name that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return "room-%s" % self.id


class ButtonType(BaseModel):
    """
       Stores different type of buttons
    """
    button_type = models.SmallIntegerField(blank=False, null=False, choices=ButtonChoices.get_choices())

    @property
    def button_type_str(self):
        """
        Returns the str format of button type
        """
        return ButtonChoices(self.button_type).name


class UserCall(BaseModel):
    """
    Model to keep track of user requests/button calls
    """
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE,
                             related_name="my_button_calls")
    button_type = models.ForeignKey(ButtonType, blank=False, null=False, on_delete=models.CASCADE,
                                    related_name="button_calls")
