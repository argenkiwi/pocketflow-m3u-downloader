import os
import aiohttp
import aiofiles

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
