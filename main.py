import argparse
import asyncio
from flow import create_M3U_downloader_flow

def main():
    parser = argparse.ArgumentParser(description="Download files from an M3U playlist.")
    parser.add_argument("--m3u_file", help="Path to the M3U file.")
    parser.add_argument("--output_folder", help="Path to the output folder.")
    args = parser.parse_args()

    output_folder = args.output_folder or (args.m3u_file.split(".")[0] if args.m3u_file else None)

    storage = {
        "m3u_file": args.m3u_file,
        "output_folder": output_folder
    }

    flow = create_M3U_downloader_flow()
    asyncio.run(flow.run_async(storage))

if __name__ == "__main__":
    main()
