import datetime

import srt


class SubtitleTrack:
    def __init__(self, filepath):
        self._subtitles = []

        self._load_subtitle(filepath)

    def get_subtitle(self, position) -> str:
        time = datetime.timedelta(milliseconds=position)

        for sub in self._subtitles:
            if sub.start < time < sub.end:
                return sub.content

        return ''

    def _load_subtitle(self, filepath: str):
        try:
            with open(filepath, encoding='utf-8') as f:
                self._subtitles = list(srt.parse(f.read()))
        except UnicodeDecodeError as e:
            with open(filepath, encoding='windows-1251') as f:
                self._subtitles = list(srt.parse(f.read()))
