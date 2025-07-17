from pocketflow import AsyncFlow
from nodes import (
    ValidateM3UPath,
    ReadM3U,
    KhinsiderURLResolver,
    PromptUserAction,
    ListURLs,
    DownloadFiles,
    SaveM3UFile,
    Greet,
)

def create_M3U_downloader_flow():
    validate_m3u_path = ValidateM3UPath()
    read_m3u = ReadM3U()
    khinsider_url_resolver = KhinsiderURLResolver()
    prompt_user_action = PromptUserAction()
    list_urls = ListURLs()
    download_files = DownloadFiles()
    save_m3u_file = SaveM3UFile()
    greet = Greet()

    validate_m3u_path - "valid" >> read_m3u
    validate_m3u_path - "invalid" >> greet 
    read_m3u >> prompt_user_action
    prompt_user_action - "resolve" >> khinsider_url_resolver
    prompt_user_action - "download" >> download_files
    prompt_user_action - "list" >> list_urls
    prompt_user_action - "resolve" >> khinsider_url_resolver
    prompt_user_action - "quit" >> greet
    khinsider_url_resolver >> save_m3u_file
    
    list_urls >> prompt_user_action
    download_files >> prompt_user_action
    save_m3u_file >> prompt_user_action

    return AsyncFlow(validate_m3u_path)
