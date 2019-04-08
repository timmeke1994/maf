import authomatic
from authomatic.providers import oauth2, oauth1

CONFIG = {
    'google': {
        'class_': oauth2.Google,

        'consumer_key': '354722028032-03adk6d71khebmp05otm7c83b74q9j7s.apps.googleusercontent.com',
        'consumer_secret': 'nUF_OTn1BV0VEp8vb1EcIsqi',
        'id': authomatic.provider_id(),
        'scope': oauth2.Google.user_info_scope + [
            'https://www.googleapis.com/auth/calendar',
            'https://mail.google.com/mail/feed/atom',
            'https://www.googleapis.com/auth/drive',
            'https://gdata.youtube.com'],
        '_apis': {
            'List your calendars': ('GET', 'https://www.googleapis.com/calendar/v3/users/me/calendarList'),
            'List your YouTube playlists': ('GET', 'https://gdata.youtube.com/feeds/api/users/default/playlists?alt=json'),
        }
    }
}