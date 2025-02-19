import os
import requests
import zipfile

def search_logo(sportsbook):
    # For Clearbit logo service, you can try using their API
    clearbit_api_url = f"https://logo.clearbit.com/{sportsbook.lower().replace(' ', '')}.com"
    
    print(f"Searching for logo on Clearbit: {clearbit_api_url}")
    
    response = requests.get(clearbit_api_url)

    if response.status_code == 200:
        logo_url = response.url
        print(f"Found logo for {sportsbook}: {logo_url}")
        return logo_url
    else:
        print(f"No logo found for {sportsbook} on Clearbit")
        return None

def download_logo(url, name, folder):
    if not url:
        return False
    
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        filename = os.path.join(folder, f"{name}.png")
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return filename
    return None

def zip_logos(folder, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(folder):
            for file in files:
                zipf.write(os.path.join(root, file), arcname=file)

def main():
    sportsbooks = [
        "Skybook","Bovada","BetMania","SBGGlobal","SportsBetting","BetOnline","Pinnacle","JustBet","Jazz","Heritage","BetHorizon","Public%","Catalina","Grande","Buckeye","IASports","Intertops","Mirage","Westgate","BetPhoenix","PayPerHead","EasySt","SouthPoint","William Hill","WWWager","SportsInterAction","BetUS","Peppermill","YouWager","Coasts","Stations","Caesars","Wynn","Click and Bet","Atlantis","ABC","WagerWeb","TicoSports","PerHead","Golden Nugget","PlayCR","TopBet","BetOSB","CD Sports","Odds","WagerPerHead","Lowvig","BetSTS","LinePros","BPPH","Treasure Island","Carson Valley Inn","WagerMadness","BETHK","Heritage105","Bet365","LooseLines","UCABet","VSO247","El Caribe","GTbets","Sports411","AcePPH","ActionPass","Bet33","BetWay","Consensus","Dollar","ISI Sports","Premier","ProBets","QBT","BetAnySports","SportsBetting AU","SportsBetting OL","Baldinis","BetCRIS","DELottery","William Hill NJ","William Hill MS","DraftKings","Rhode Island Lottery","PlayMGM","Moneyball","Buffalo Thunder","Circa","BetWorks","Pearl River","Chinook","RWCatskills","Beau Rivage","Monarch BH","WMHillCO","WMHillDC","WMHillIL","BetMGMDetroit","SpiritMountain","Bet105","SasquatchWildCardCO","Maverick","FireBet","BetRivers","Consensus US","ResortWorldLV","Gila River AZ","Cadillac Jacks SD","Tin Lizzie SD","Emerald Queen WA","CircaIA","ELYSDC","Boyd","FuboIA","WynnMA","MGM Natl Harbor MD","IGT","Truebookies","ParadiseWager","4CasterSports","Amapola","Shiba","Prophet Exchange NJ","3et","SundayBets","CircaCO","GANTest1","GANTest2","CircaIL","ts_lambda","ts_lambda_stage","DonBest","BettorsDen","CircaKY"
    ]  # Add more from your list
    
    folder = "logos"
    os.makedirs(folder, exist_ok=True)
    
    for sportsbook in sportsbooks:
        logo_url = search_logo(sportsbook)
        if logo_url:
            download_logo(logo_url, sportsbook, folder)
    
    zip_logos(folder, "sportsbook_logos.zip")
    print("Logos downloaded and zipped successfully!")

if __name__ == "__main__":
    main()
