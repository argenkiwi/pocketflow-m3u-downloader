from pocketflow import AsyncFlow
from nodes import ValidateM3UPath, ReadM3U, DownloadFiles

def create_M3U_downloader_flow():
    validate_m3u_path = ValidateM3UPath()
    read_m3u = ReadM3U()
    download_files = DownloadFiles()
        
    validate_m3u_path - "valid" >> read_m3u
    read_m3u - "read" >> download_files

    return AsyncFlow(validate_m3u_path)
