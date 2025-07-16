from pocketflow import AsyncFlow
from nodes import ReadM3U, DownloadFiles

def create_M3U_downloader_flow():
    read_m3u = ReadM3U()
    download_files = DownloadFiles()
        
    read_m3u - "read" >> download_files

    return AsyncFlow(read_m3u)
