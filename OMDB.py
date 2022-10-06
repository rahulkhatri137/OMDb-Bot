#sheriyenna

import requests
from info import API_KEY

user = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57"}

def get_movie_info(query):    
    try:
       url = f'http://www.omdbapi.com/?apikey={API_KEY}&t={query}'
       resp = requests.get(url, headers=user).json()
       poster=resp['Poster']
       id=resp['imdbID']
       text=f"""📀 <b>𝖳𝗂𝗍𝗅𝖾: <u>{resp['Title']}</u></b>\n
⭐ <b>𝖱𝖺𝗍𝗂𝗇𝗀</b>: {resp['imdbRating']}/10
📆 <b>𝖱𝖾𝗅𝖾𝖺𝗌𝖾</b>: {resp['Released']}
🎭 <b>𝖦𝖾𝗇𝗋𝖾</b>: {resp['Genre']}
🎙 <b>𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾</b>: {resp['Language']}
🌐 <b>𝖢𝗈𝗎𝗇𝗍𝗋𝗒</b>: {resp['Country']}
🎥 <b>𝖣𝗂𝗋𝖾𝖼𝗍𝗈𝗋𝗌</b>: {resp['Director']}
📝 <b>𝖶𝗋𝗂𝗍𝖾𝗋𝗌</b>: {resp['Writer']}
🌟 <b>𝖲𝗍𝖺𝗋𝗌</b>: {resp['Actors']}
🗒 <b>StoryLine</b>: <code>{resp['Plot']}</code>

🔹<b>Request</b>- @Anything_On_Demand 
♨️<b>Updates</b>- @Everyth1ng_On_Demand
🔹<b>Main Channel</b>: @Mov1es_On_Demand"""

    except Exception as error:
        print(error)
    return poster, id, text
         
