import os
from pocketflow import AsyncNode, AsyncParallelBatchNode
from utils import download_file

class ReadM3U(AsyncNode):
    def __init__(self):
        super().__init__()

    async def prep_async(self, storage):
        return storage.get('m3u_file')

    async def exec_async(self, m3u_file):
        print(f"Reading M3U file: {m3u_file}")
        with open(m3u_file, "r") as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        print(f"Found {len(urls)} URLs to download.")
        return urls

    async def post_async(self, storage, prep_result, exec_result):
        storage["urls"] = exec_result
        return "read"

class DownloadFiles(AsyncParallelBatchNode):
    def __init__(self):
        super().__init__()

    async def prep_async(self, storage):
        self.output_folder = storage['output_folder']
        print("Starting downloads...")
        return storage.get("urls", [])

    async def exec_async(self, url):
        return await download_file(url, self.output_folder)

    async def post_async(self, storage, prep_result, proc_result):
        storage["downloaded_files"] = proc_result
        print("All downloads completed.")
        return "downloaded"
