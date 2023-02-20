from setuptools import setup, find_packages

from src.parallel_downloader import __version__

setup(
    name="parallel-downloader",
    description="Downloads file using parallel downloading.",
    version=__version__,
    license="GNU General Public License v3.0",
    author_email="jurakin.dev@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/jurakin/parallel-downloader",
    keywords="parallel downloader",
    python_requires=">=3.7",
    install_requires=[
          "requests",
          "argparse"
    ],
    entry_points={
        "console_scripts": [
            "parallel-downloader = parallel_downloader.main:main",
        ]
    }
)