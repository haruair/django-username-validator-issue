from django.core import validators
from django.utils import six
from django.utils.translation import ugettext_lazy as _
from django.utils.deconstruct import deconstructible


@deconstructible
class CustomUsernameValidator(validators.RegexValidator):
    regex = r'^[\w]+$'
    message = _(
        'Enter a valid username. This value may contain only letters.'
    )
    flags = re.UNICODE if six.PY2 else 0
