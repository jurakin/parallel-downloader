# Parallel Downloader

Downloads file using parallel downloading (if range header is supported otherwise downloads normally).

## How it works

The library is based on adding [range headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Range_requests) to request and downloading the file in threads simultaneously.

## Instalation

- Requirements are `threading` and `requests` (built-in)
- Install from repository `python3 -m pip install git+https://github.com/jurakin/parallel-downloader`

## Examples

```
import parallel_downloader as d

url = "https://i.imgur.com/z4d4kWk.jpg"
file = "cat.jpg"

# download url to file using 10 parts
d.ParallelDownloader(url, file, 10).wait()
```

Using `.start()` and `.wait()`:

```
import parallel_downloader as d

url = "https://i.imgur.com/z4d4kWk.jpg"
file = "cat.jpg"

# download url to file using 10 parts
p = d.ParallelDownloader(url, file, 10)

print("before downloading")

p.start()

print("downloading")

p.wait()

print("downloaded")
```

Using `.terminate()`:

```
import parallel_downloader as d

import time

url = "https://i.imgur.com/z4d4kWk.jpg"
file = "cat.jpg"

# download url to file using 10 parts
p = d.ParallelDownloader(url, file, 10).wait()

time.sleep(1)

p.terminate()
```

## Result

The result image is:

![cat](./cat.jpg?raw=true)

## License

This project is released under GNU General Public License v3.0

## Credits

This project is inspired by [ulozto-downloader](https://github.com/setnicka/ulozto-downloader)'s parallel downloader.
