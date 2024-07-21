import requests
from bs4 import BeautifulSoup
import pandas
import gspread
import numpy as np
import datetime
import json
import urllib.parse

# Set up time of running script 600 = 10 mins
seconds = 3000 

class flicks:
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
        'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    creds = {
        "type": "service_account",
        "project_id": "crypto-messari",
        "private_key_id": "9cd2f9d784c4baaba89c4f5f8a565ac47d2b33ab",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCwQ2KpOgPnA7wv\nuBjzFYbkL8vmfuFlQ1e3j8IqG0Ikale7bWfc24E21cK4ZX1zeCbN5R4Rcb560q4L\nLTiLLvsfcZYyh+WCtdih//Jdg7LelwejNP8FemVy5eXvtaWJVLIVw7XDDLxA34dQ\nXrtTECiiT4cZ4S+m/Pt7m6h8e1f3ddrKbAjr91vq6gWlY0x5bIJwvjoc8jkcKzpj\ndQ6VBa6SHjQ2X4qUUEzxflpDh+qbgXm208VBr/sMfwtzueL+F9NmvJ3jSkF/Ahjl\nSNPuKXY6TbwqS+oaPf7mFQRsvXTJ0o7skVLqsoOEsAYd1DDV12usKZaQV35CUh/p\nmSvG9+k5AgMBAAECggEALQO4kaFIV9ojWEh6zrHDtkjimOX0aCkPoMhs/NXjSWuD\nJlGlgcjpMfjbdr4skK2xs0l9KVVUIQfm/OG6nAkOhxQ6GIOOQJhyT8UOv4UfzCrj\n/3FMY7jDadl+pH5OXUktBdPqenqpJSQw6XyX+Hma9wC6bwiMY+gdzY6OM+RILeEV\nc58YvulFxSHAwmb5voh5SEalnnC4G3dO3qOwBaMRzNmEpSs9OIDWQ4/BKCrvViyI\ntcpHgCt/d9AtiU61k1GxJzFiiJt/Pu5abmfnvQhZcLrhG9rkoO4dZ1zvbKKYUzgk\nZkw3Yt1Xk3y34S5rl42XsVOmNAeaRkIy/ZoqDTLZ9QKBgQDm5mWV3Awb5iJjj3C5\n/jigoxLWuBiHkBEQg7krjnStBaAOms1fIWBUP6mw5cBH+BM17uij8c1eqRT3HVwZ\n0j+qQKbd65erMtlmOYucUJSbWcX/kEXIfXEYP+hAmSTAuir8Eqgtu0V7jgpa5ffH\npweCn9Pf1lzckKwqhCT709IrxwKBgQDDbIdamsk85GgZcvaXuEYptg3sVTKsksuV\n7+hymV7sC2zDgegvdde3aFX1VwxlXPdvqJvdWPSWran2lI3Mz6eTPWMSlBPt+tLq\nXYNWSKzQ06WE+eVUmE61WDVw0x8+Jr5aubg8OA6DhdLI6IDqvFp7v4QNB0EvVPsu\nWCT6OgNC/wKBgAFfwZ8ArjnERtQc2Gji8GdUURpiAhNcch2NCx8NO/iDng44MZyt\nUCtwLYxV8az79vFNOKkxGS3FB9DopdGphKN4uwV7D23/YXfQQ9psSFYcVKdOrnug\n83lXeARaZPOYqATT/5g2ExXHJJyh3bWcctj+Jn6ggfD2E3A1VRsCia+lAoGACmUV\ndg5Rsfl8SA5Da6KTqNhUOUP25BMS3TDbrmzWDbw11thsH0onZUwZdmlg8WtWhgvz\n7nwy1mj6Z3FTcZeCFGTphi12Oexjl6/NsqM+/gSkA0S/nBZV6XN9tDimqsmoym6i\njCF3NCvEIIetg87tCTQQtBi0sO3WRorNvLmlPsUCgYAtSEFVqcTe6D6c6mNjyfhX\nrMJ2tR3l9q37C2k4GtXdx1LFeoNusEOyMU7GMTUL5gd7q571IW92mow5U04GmsXp\n2DfA41nVUT7sqnkVCoFt6LQDS+s/5v5KnxNZ23ZEul5Qbygfx9PQaZ/TuyaxZ6+S\nhJrcuKgiWaFyED4Lni/XsQ==\n-----END PRIVATE KEY-----\n",
        "client_email": "pythoncryptomessariaccount@crypto-messari.iam.gserviceaccount.com",
        "client_id": "112559430258363988070",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/pythoncryptomessariaccount%40crypto-messari.iam.gserviceaccount.com"
    }
    
    save = []
    set_list = []
    
    def read_sheets(self):
        gc = gspread.service_account_from_dict(self.creds)
        spreed_sheet_id = '1fMD-Ld9LOn8LctXuaFYywv3mY_LugjS1syd-bCizer0'
        sheet = gc.open_by_key(spreed_sheet_id)
        worksheet = sheet.worksheet('List of movies')
        movies = worksheet.col_values(1)[1:]
        for movie in movies:
            self.movie_name = movie
            href = self.get_movies(movie_name=movie)
            if href == None:continue
            self.get_movies_location(href=href)
        
    def get_movies(self,movie_name:str):
        
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            # 'cookie': '_gcl_au=1.1.487198694.1720539998; _ga=GA1.1.1019235755.1720539999; _fbp=fb.2.1720539998969.15664020545363344; _tt_enable_cookie=1; _ttp=8tfR2sVlSUOBkFecf3yWP4qH3Tf; _sharedID=6edb98e2-b8ac-4e21-b756-f4f5f052d29d; _sharedID_cst=VyxHLMwsHQ%3D%3D; pbjs-unifiedid=%7B%22TDID%22%3A%22955b0faf-81d7-41d4-ba87-8c0a8aac2d28%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222024-06-09T15%3A46%3A41%22%7D; pbjs-unifiedid_cst=VyxHLMwsHQ%3D%3D; listview=list; geo={%22gps%22:{%22lat%22:14.611%2C%22lng%22:120.9962}%2C%22region%22:%22brisbane-central%22%2C%22choice%22:%22gps%22%2C%22ip_detect%22:false}; connect.sid=s%3A-ScRKZdfuwLbjQIkeqs0TaQuRGAWl_nH.2hFozEPnI%2FTof%2FfbDf2h6e%2FiL9qkqWfd1DijfhWrKJM; _ga_70KED4KQBQ=GS1.1.1721483174.2.0.1721483174.60.0.873514818; _ga_6R8P3B2ZGZ=GS1.1.1721483174.2.0.1721483174.60.0.0; __gads=ID=c118cf97361465b4:T=1720539998:RT=1721483176:S=ALNI_MaTsM3YHLZaq-01Fv6u41Yvaztx0g; __eoi=ID=1cc5b7b3e72d6280:T=1720539998:RT=1721483176:S=AA-AfjYyxWQ1k_XwtsBM4pyvRfPZ',
            'is-ajax-call': 'yes',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.flicks.com.au/',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        }

        params = {
            'q': movie_name,
        }

        response = requests.get('https://www.flicks.com.au/search/live/', params=params, headers=headers)
        soup = BeautifulSoup(response.text,'html.parser')
        try:
            href = soup.select_one('.search-nav__content__inner').select('li')[0].a.get('href')
            href = 'https://www.flicks.com.au' + href
        except:
            href = None
        
        return href
    
    def get_cookies(self,city:str):
        data = {
            "gps": None,
            "region": city,
            "choice": "region"
        }
        json_str = json.dumps(data)
        encoded_str = urllib.parse.quote(json_str)
        cookies = {

            'geo': encoded_str,

        }
        return cookies
    
    def get_movies_location(self,href:str):
        href = href.replace('movie','movie/times')
        main_curl = href.split('times/')[1].split('/')[0]
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            # 'cookie': '_gcl_au=1.1.487198694.1720539998; _ga=GA1.1.1019235755.1720539999; _fbp=fb.2.1720539998969.15664020545363344; _tt_enable_cookie=1; _ttp=8tfR2sVlSUOBkFecf3yWP4qH3Tf; _sharedID=6edb98e2-b8ac-4e21-b756-f4f5f052d29d; _sharedID_cst=VyxHLMwsHQ%3D%3D; pbjs-unifiedid=%7B%22TDID%22%3A%22955b0faf-81d7-41d4-ba87-8c0a8aac2d28%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222024-06-09T15%3A46%3A41%22%7D; pbjs-unifiedid_cst=VyxHLMwsHQ%3D%3D; listview=list; connect.sid=s%3A-ScRKZdfuwLbjQIkeqs0TaQuRGAWl_nH.2hFozEPnI%2FTof%2FfbDf2h6e%2FiL9qkqWfd1DijfhWrKJM; _ga_70KED4KQBQ=GS1.1.1721483174.2.1.1721484202.60.0.873514818; __gads=ID=c118cf97361465b4:T=1720539998:RT=1721484203:S=ALNI_MaTsM3YHLZaq-01Fv6u41Yvaztx0g; __eoi=ID=1cc5b7b3e72d6280:T=1720539998:RT=1721484203:S=AA-AfjYyxWQ1k_XwtsBM4pyvRfPZ; _ga_6R8P3B2ZGZ=GS1.1.1721483174.2.1.1721484308.60.0.0; geo={%22gps%22:null%2C%22region%22:%22sydney-city-inner-and-east%22%2C%22choice%22:%22region%22%2C%22ip_detect%22:false}',
            'is-ajax-call': 'yes',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.flicks.com.au/movie/kalki-2898-ad/',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        }
        
        cities = ['sydney-city-inner-and-east','sydney-north','sydney-south','sydney-west',
                  'melbourne-city-inner','melbourne-east','melbourne-north-and-west','melbourne-south-and-frankston']
        
        for city in cities:
            city_url = f'{href}{city}'
            print(city_url)
            response = requests.get(city_url,headers=headers)
            #print(response.text)
            soup = BeautifulSoup(response.text,'html.parser')
            divs = soup.find_all('div',attrs={'data-date':True})
            if divs == []:
                print('No found! on city : ',city)
            for div in divs:
                date = div['data-date']
                region = div['data-geotype']
                region_url = f'https://www.flicks.com.au/movie/sessions/{main_curl}/{date}/{region}/'
                cookies = self.get_cookies(city=city)
                response = requests.get(region_url,headers=headers,cookies=cookies)
                soup = BeautifulSoup(response.text,'html.parser')
                articles = soup.select('article')
                for article in articles:
                    dic = {}
                    if 'sydney' in city:
                        dic['City'] = 'Sydney'
                    if 'melbourne' in city:
                        dic['City'] = 'Melbourne'
                    dic['Movie name'] = self.movie_name
                    dic['Date'] = date
                    dic['Theatre'] = article.h4.text
                    times = article.select('.times-calendar-times__el__time')
                    time_dates = []
                    for time_ in times:
                        time_dates.append(time_.text.strip())
                    time_dates = ' | '.join(time_dates) 
                    dic['Times'] = time_dates
                    try:
                        dic['Ticket link'] = article.select_one('[data-category="Bookings"]')['href']
                    except:
                        dic['Ticket link'] = ''
                    print(dic)
                    self.save.append(dic)
    
    def saving(self):
        df = pandas.DataFrame(self.save)
        df = df.replace(np.NAN,'')
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        gc = gspread.service_account_from_dict(self.creds)
     
        spreed_sheet_id = '1fMD-Ld9LOn8LctXuaFYywv3mY_LugjS1syd-bCizer0'
        sheet = gc.open_by_key(spreed_sheet_id)
        worksheet = sheet.worksheet('Session times')
        worksheet.batch_clear(["A1:EZ"])
        columns = df.columns.values.tolist()
        body = df.values.tolist()
        save = []
        save.append(columns)
        for item in body:
            save.append(item)
        worksheet.update(values=save,range_name='A1',)
        print('exit - 0 finish | date: ',datetime.datetime.now() , ' | total: ' + str(len(self.save)))

if __name__ == '__main__':
    flicks_obj = flicks()
    flicks_obj.read_sheets()
    flicks_obj.saving()
