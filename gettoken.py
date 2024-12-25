import requests
import json

_banner_ = '''
\033[1;91m ooooooooo.                                o8o  
\033[1;92m`888   `Y88.                              `"'  
\033[1;97m 888   .d88'  .ooooo.  ooo. .oo.  .oo.   oooo  
\033[1;98m 888ooo88P'  d88' `88b `888P"Y88bP"Y88b  `888  
\033[1;99m 888`88b.    888   888  888   888   888   888  
\033[1;93m 888  `88b.  888   888  888   888   888   888  
\033[1;97mo888o  o888o `Y8bod8P' o888o o888o o888o o888o 
                                               
                                               
                                                   
                                       
                                       
   +=+=+=+=+=+=+=+=+=+=+=+=+=+=+
  +++=== GET TOKEN FACEBOOK ===+++   
 ++== Tools Get Token Facebook ==++
+= No Spam Dettect Server Facebook =+
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

# author : Romi
# contact: 0327*******
'''
user=raw_input('username/email: ')
passw=raw_input('password: ')
get = requests.get('https://b-api.facebook.com/dialog/oauth?scope=user_about_me,user_actions.books,user_actions.fitness,user_actions.music,user_actions.news,user_actions.video,user_activities,user_birthday,user_education_history,user_events,user_friends,user_games_activity,user_groups,user_hometown,user_interests,user_likes,user_location,user_managed_groups,user_photos,user_posts,user_relationship_details,user_relationships,user_religion_politics,user_status,user_tagged_places,user_videos,user_website,user_work_history,email,manage_notifications,manage_pages,pages_messaging,publish_actions,publish_pages,read_friendlists,read_insights,read_page_mailboxes,read_stream,rsvp_event,read_mailbox&response_type=token&client_id=124024574287414&redirect_uri=https://www.instagram.com/')

up = get.content
pu = json.loads(up)
if "session_key" in up:
    print
    print _banner_
    print 'username:' + pu['identifier']
    print 'token:' + pu["access_token"]
    open(user+'-token.txt', 'a').write(pu["access_token"])
    print
    print 'saved file to '+user+'-token.txt'
else:
    print 'maaf username/password salah'
