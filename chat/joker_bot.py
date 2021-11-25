import random
from .constants import (
    JOKES_RELATED_TO_DUMP, JOKES_RELATED_TO_STUPID, JOKES_RELATED_TO_FAT
)
from .exceptions import ClientError
from .models import UserCall, ButtonType
from .enums import ButtonChoices


class Joker:
    """
    this class is responsible for providing jokes based on user message
    also updating model that is keeping track of user calls
    """

    def __init__(self, user):
        self._user = user

    @staticmethod
    def fetch_button_type_object_using_button_type(button_type):
        # fetches button type record for given button type
        try:
            return ButtonType.objects.get(button_type=button_type)
        except ButtonType.DoesNotExist:
            ClientError("INVALID BUTTON TYPE")

    @staticmethod
    def choose_random_joke_from_choices(choices):
        # takes an iterable object as input and returns random item
        random_choice_index = random.randint(0, len(choices) - 1)
        return choices[random_choice_index]

    def create_new_user_button_call_record(self, button_type):
        button_type_obj = self.fetch_button_type_object_using_button_type(button_type)
        try:
            UserCall.objects.create(user=self._user, button_type=button_type_obj)
        except Exception as e:
            ClientError("FAILED TO CREATE UserCall RECORD")

    def get_joke_related_to_stupid(self):
        self.create_new_user_button_call_record(ButtonChoices.STUPID.value)
        return self.choose_random_joke_from_choices(JOKES_RELATED_TO_STUPID)

    def get_joke_related_to_fat(self):
        self.create_new_user_button_call_record(ButtonChoices.FAT.value)
        return self.choose_random_joke_from_choices(JOKES_RELATED_TO_FAT)

    def get_joke_related_to_dump(self):
        self.create_new_user_button_call_record(ButtonChoices.DUMP.value)
        return self.choose_random_joke_from_choices(JOKES_RELATED_TO_DUMP)
