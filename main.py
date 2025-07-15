import argparse
import asyncio
from flow import M3UDownloaderFlow

def main():
    parser = argparse.ArgumentParser(description="Download files from an M3U playlist.")
    parser.add_argument("--m3u_file", required=True, help="Path to the M3U file.")
    parser.add_argument("--output_folder", help="Path to the output folder.")
    args = parser.parse_args()

    output_folder = args.output_folder or args.m3u_file.split(".")[0]

    storage = {
        "m3u_file": args.m3u_file,
        "output_folder": output_folder
    }

    flow = M3UDownloaderFlow()
    asyncio.run(flow.run_async(storage))

if __name__ == "__main__":
    main()
