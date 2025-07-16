from pocketflow import AsyncFlow
from nodes import (
    ValidateM3UPath,
    ReadM3U,
    PromptUserAction,
    ListURLs,
    DownloadFiles,
)

def create_M3U_downloader_flow():
    validate_m3u_path = ValidateM3UPath()
    read_m3u = ReadM3U()
    prompt_user_action = PromptUserAction()
    list_urls = ListURLs()
    download_files = DownloadFiles()

    validate_m3u_path - "valid" >> read_m3u
    read_m3u - "read" >> prompt_user_action
    prompt_user_action - "download" >> download_files
    prompt_user_action - "list" >> list_urls

    return AsyncFlow(validate_m3u_path)
