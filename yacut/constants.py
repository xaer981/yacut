INDEX_TEMPLATE = 'index.html'
INTERNAL_SERVER_ERROR_TEMPLATE = '500.html'
NOT_FOUND_TEMPLATE = '404.html'

SHORT_PATTERN = '[0-9a-zA-Z]+$'
URL_PATTERN = ('https?:\\/\\/(?:www\\.)?'
               '[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.'
               '[a-zA-Z0-9()]{1,6}\\b'
               '(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$')

CUSTOM_ID_MAX_LENGTH = 16
CUSTOM_ID_MIN_LENGTH = 1
LINK_MAX_LENGTH = 256
LINK_MIN_LENGTH = 1
RANDOM_SHORT_MAX_LENGTH = 6

LENGHT_ERROR = 'Длина должна быть от {min} до {max} символов.'
