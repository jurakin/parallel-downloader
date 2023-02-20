from . import ParallelDownloader
import argparse

def main():
    parser = argparse.ArgumentParser(prog="parallel-downloader", description="Downloads file using parallel downloading.")
    parser.add_argument("url", help="url of file")
    parser.add_argument("file", help="path to file")
    parser.add_argument("--parts", "-p", default=10, type=int, help="number of parts (default 10)")
    parser.add_argument("--no-bar", "-n", default=False, action="store_true", help="do not show progress bar")

    args = parser.parse_args()

    pbar = None
    if not args.no_bar:
        try:
            from tqdm import tqdm
            
            pbar = tqdm(unit='iB', unit_scale=True, unit_divisor=1024)
        except ImportError:
            print("you must have tqdm installed to use progress bar or use --no-bar option")
        

    ParallelDownloader(args.url, args.file, args.parts, pbar=pbar).wait()

if __name__ == "__main__":
    main()