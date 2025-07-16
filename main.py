import argparse
import asyncio
from flow import create_M3U_downloader_flow

def main():
    parser = argparse.ArgumentParser(description="Download files from an M3U playlist.")
    parser.add_argument("--m3u_file", help="Path to the M3U file.")
    parser.add_argument("--output_folder", help="Path to the output folder.")
    args = parser.parse_args()

    storage = {
        "m3u_file": args.m3u_file,
        "output_folder": args.output_folder
    }

    flow = create_M3U_downloader_flow()
    asyncio.run(flow.run_async(storage))

if __name__ == "__main__":
    main()
