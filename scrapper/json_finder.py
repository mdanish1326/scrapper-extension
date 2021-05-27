# json file finder in the system
import json,time
import pathlib
import scrapper

def json_finder():
    
    loop = True
    while loop:
        try:
            json_path = str(pathlib.Path.home()) + "\\codes\\pycode\\scrapper-extension\\scrapper\\ab.json"
            with open(json_path,"r", encoding="utf-8") as f:
                data = json.load(f)
                for user in data["user_details"]:

                    link = user.get("url")
                    user_price = user.get("price")
                    user_email = user.get("user_email")
                    
                    if link != None and user_price != None:
                        scrapper.get_details(link, user_price, user_email)
                
                loop = False

        except FileNotFoundError:
            print('File Not Found...')
            time.sleep(3600)
            
        finally:
            pass
