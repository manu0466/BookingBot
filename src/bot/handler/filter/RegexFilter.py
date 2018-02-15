from typing import List
import re

from bot import Message
from . import HandlerFilter


class RegexFilter(HandlerFilter):

    def __init__(self, keywords: List[str],
                 case_sensitive: bool = True,
                 exact_match: bool = True,
                 handle_command: bool = False):
        self._handle_command = handle_command
        regex = ""
        for i in range(len(keywords)):
            regex += ("(^" + keywords[i] + (".*$)" if not exact_match else "$)"))
            if i < len(keywords) - 1:
                regex += "|"
        if not case_sensitive:
            self._text_regex = re.compile(regex, re.IGNORECASE)
        else:
            self._text_regex = re.compile(regex)

    def filter(self, message: Message) -> bool:
        text = message.get_escaped_text() if self._handle_command else message.get_text()
        return self._text_regex.search(text) is not None
