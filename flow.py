from pocketflow import AsyncFlow
from pocketflow import AsyncFlow
from nodes import ReadM3U, DownloadFiles

class M3UDownloaderFlow(AsyncFlow):
    def __init__(self):
        read_m3u = ReadM3U()
        download_files = DownloadFiles()

        read_m3u - "read" >> download_files

        super().__init__(read_m3u)
