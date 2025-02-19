# Logo Downloader

## Overview
This script searches for sportsbook logos using Clearbit's logo service, downloads them, and compresses them into a ZIP file. It automates the retrieval of logos for a predefined list of sportsbooks (but can be used for any logos).

## Features
- Fetches logos from **Clearbit** based on names.
- Downloads logos and saves them in a local folder.
- Zips all downloaded logos into a single archive for easy access.

## Prerequisites
- Python 3.x installed
- `requests` library installed

### Install Dependencies
Run the following command to install the required library:
```sh
pip install requests
```

## How to Use
1. **Run the script**:
   ```sh
   python download_logos.py
   ```
2. The script will:
   - Search for each sportsbook's logo on Clearbit.
   - Download the logo if available.
   - Save the logos in a folder named `logos`.
   - Compress all logos into `sportsbook_logos.zip`.
3. Once completed, you will find the downloaded logos in the `logos` folder and the zip file in the script directory.

## File Structure
```
.
├── download_logos.py  # The main script
├── logos/             # Folder where logos are saved
└── sportsbook_logos.zip  # Zipped archive of logos
```

## Notes
- Clearbit provides logos for many websites, but not all sportsbooks may be available.
- If no logo is found, the script will skip that sportsbook and continue.
- Ensure you have an active internet connection while running the script.

## License
This project is open-source and free to use.

## Author
Developed by [Your Name]

