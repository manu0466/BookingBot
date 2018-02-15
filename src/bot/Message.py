

class Message:

    def __init__(self, text: str, user_id):
        self._text = text
        self._user_id = user_id

    def get_text(self) -> str:
        return self._text

    def get_sender_id(self):
        return self._user_id

    def get_escaped_text(self) -> str:
        escaped = self._text
        if escaped.startswith('/'):
            escaped = escaped[1:]
        return escaped
