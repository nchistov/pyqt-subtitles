from PyQt6 import QtMultimedia

from .subtitle_track import SubtitleTrack


class PyQtSubtitles:
    def __init__(self, media_player: QtMultimedia.QMediaPlayer, subtitle_files: list[str]):
        self._media_player = media_player

        self._tracks = [SubtitleTrack(filepath) for filepath in subtitle_files]
        self._current_track: SubtitleTrack | None = None

        self._media_player.positionChanged.connect(self._position_changed)

    def _position_changed(self, position):
        if self._current_track is not None:
            self._media_player.videoSink().setSubtitleText(self._current_track.get_subtitle(position))

    def set_current_track(self, index: int):
        """Set current track index, if index is -1 or less, current track will be None"""
        if index < 0:
            self._current_track = None
        else:
            if index >= len(self._tracks):
                ...
            else:
                self._media_player.setActiveSubtitleTrack(-1)  # Disable video built-in subtitles
                self._current_track = self._tracks[index]

    def get_current_track(self) -> int:
        if self._current_track is None:
            return -1
        else:
            return self._tracks.index(self._current_track)
