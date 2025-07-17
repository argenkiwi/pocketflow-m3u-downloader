import os
import aiohttp
import aiofiles
from bs4 import BeautifulSoup

async def resolve_khinsider_url(url: str) -> str:
    if "downloads.khinsider.com" in url:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
        }
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        soup = BeautifulSoup(await response.text(), "html.parser")
                        
                        # Try to find the direct link in the audio player
                        audio_source = soup.find("audio", id="audioPlayer")
                        if audio_source and audio_source.has_attr("src"):
                            mp3_url = audio_source["src"]
                            print(f"Resolved {url} to {mp3_url}")
                            return mp3_url
                        
                        # If not found, search for a link with 'href'
                        for link in soup.find_all('a', href=True):
                            if link['href'].endswith('.mp3'):
                                mp3_url = link['href']
                                print(f"Resolved {url} to {mp3_url}")
                                return mp3_url

        except Exception as e:
            print(f"Could not resolve {url}: {e}")
    return url

async def download_file(url, output_folder):
    """Downloads a file from a URL to a specified folder asynchronously."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_name = url.split("/")[-1]
    output_path = os.path.join(output_folder, file_name)

    print(f"Downloading {url}...")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            async with aiofiles.open(output_path, "wb") as f:
                while True:
                    chunk = await response.content.read(8192)
                    if not chunk:
                        break
                    await f.write(chunk)
    print(f"Finished downloading {url}")
    return output_path
