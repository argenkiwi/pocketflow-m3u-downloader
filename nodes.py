import os
import inquirer
from pocketflow import AsyncNode, AsyncParallelBatchNode
from utils import download_file, resolve_khinsider_url

class KhinsiderURLResolver(AsyncParallelBatchNode):
    """
    Resolves khinsider URLs to direct MP3 links.
    """
    async def prep_async(self, storage):
        print("Resolving khinsider URLs...")
        return storage.get("urls", [])

    async def exec_async(self, url: str) -> str:
        return await resolve_khinsider_url(url)

    async def post_async(self, storage, prep_result, proc_result):
        storage["urls"] = proc_result
        print("URL resolution complete.")

class ValidateM3UPath(AsyncNode):
    async def prep_async(self, storage):
        return storage.get("m3u_file")

    async def exec_async(self, m3u_file):
        if m3u_file and os.path.exists(m3u_file):
            return "valid"

        questions = [
            inquirer.List(
                "m3u_file",
                message="M3U file not found. Select a file from the list below or abort",
                choices=os.listdir(".") + ["Abort"],
            ),
        ]

        answers = inquirer.prompt(questions)
        return answers

    async def post_async(self, storage, m3u_file, answers):
        if answers and answers["m3u_file"] != "Abort":
            storage["m3u_file"] = answers["m3u_file"]
            storage["output_folder"] = storage["output_folder"] or answers["m3u_file"].split(".")[0]
            return "valid"

        return "invalid"
    
class ReadM3U(AsyncNode):
    async def prep_async(self, storage):
        return storage.get('m3u_file')

    async def exec_async(self, m3u_file):
        print(f"Reading M3U file: {m3u_file}")
        with open(m3u_file, "r") as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        print(f"Found {len(urls)} URLs to download.")
        return urls

    async def post_async(self, storage, m3u_files, urls):
        storage["urls"] = urls

class PromptUserAction(AsyncNode):
    async def prep_async(self, storage):
        return storage.get("urls", [])

    async def exec_async(self, urls):
        choices = ["List", "Download", "Quit"]
        if any("downloads.khinsider.com/game-soundtracks" in url for url in urls):
            choices.insert(1, "Resolve")

        questions = [
            inquirer.List(
                "action",
                message="What would you like to do?",
                choices=choices,
            ),
        ]

        answers = inquirer.prompt(questions)
        return answers["action"]

    async def post_async(self, storage, _, answer):
        return answer.lower()

class ListURLs(AsyncNode):
    async def prep_async(self, storage):
        return storage.get("urls", [])

    async def exec_async(self, urls):
        if urls:
            print("Here are the URLs in the M3U file:")
            for url in urls:
                print(url)
        else:
            print("No URLs found in the M3U file.")
         

class SaveM3UFile(AsyncNode):
    async def prep_async(self, storage):
        return (storage.get("m3u_file"), storage.get("urls", []))

    async def exec_async(self, data):
        m3u_file, urls = data
        if m3u_file and urls:
            print(f"Saving URLs to {m3u_file}...")
            with open(m3u_file, "w") as f:
                for url in urls:
                    f.write(f"{url}\n")
            print("File saved successfully.")
        else:
            print("No file or URLs to save.")

class DownloadFiles(AsyncParallelBatchNode):

    async def prep_async(self, storage):
        self.output_folder = storage.get("output_folder", "./m3u_downloads")
        print("Starting downloads...")
        return storage.get("urls", [])

    async def exec_async(self, url):
        return await download_file(url, self.output_folder)

    async def post_async(self, storage, prep_result, proc_result):
        storage["downloaded_files"] = proc_result
        print("All downloads completed.")

class Greet(AsyncNode):
    async def exec_async(self, _ ):
        print("Thank you for playing!\n")
