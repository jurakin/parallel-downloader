from .downloader import ParalellDownloader
import argparse

parser = argparse.ArgumentParser(prog="paralell-downloader", description="Downloads file using paralell downloading.")
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
    

ParalellDownloader(args.url, args.file, args.parts, pbar=pbar).wait()