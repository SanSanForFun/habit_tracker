import re

from rest_framework.exceptions import ValidationError


class VideoValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('http://www.youtube.com')
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError('URL can be "http://www.youtube.com" only')
