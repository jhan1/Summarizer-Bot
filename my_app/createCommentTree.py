from mastodon import Mastodon
from treelib import Tree
from bs4 import BeautifulSoup
from my_app.database import Post, db
from my_app.main import app  
from my_app.main import app

# read in token
f = open("./user_token",'r')
token = f.readlines()[0] 

# initiate Mastodon 
mastodon = Mastodon( api_base_url= "https://social.cs.swarthmore.edu",
                    access_token= token )

# based on given post ID, create a tree of all the comments
def create_tree(info):
   original_id = str(info[0]) #status id of the post that used the hashtag
   status = mastodon.status(original_id)

   conversation = mastodon.status_context(original_id) #gets context of post

   if len(conversation["ancestors"]) > 0 :
      status = conversation["ancestors"][0]
      root = status["id"]
      status_id = status["id"]
      conversation = mastodon.status_context(status_id)
   
   with app.app_context():
      if db.session.get(Post,int(original_id)) is None: # query the db to make sure post doesn't already exist
         post = Post(
                  id=int(original_id),\
                  created_at = info[2],\
                  account_id = str(info[1]),\
                  root_id = str(root)
               )
         db.session.add(post)
         db.session.commit()

         #  Create a new tree
         tree = Tree()
      
         #  Add the "root"
         try :
            tree.create_node(BeautifulSoup(status["content"], features="html.parser").get_text() , status["id"])
         except :
            print("Problem adding node to the tree")

         #  Add any subsequent replies
         for status in conversation["descendants"] :
            content = BeautifulSoup(status["content"], features="html.parser").get_text() #Get text content of post
            #If the post is not from summarizerbot and content does not contain #summarizerbot, then include it in the tree
            if status["account"]["id"] != 111484794568214719 and "#summarizethis" not in content: 
               try :
                  if status["id"] != int(original_id):
                     tree.create_node(BeautifulSoup(status["content"], features="html.parser").get_text(), status["id"], parent=status["in_reply_to_id"])
               except :
                  #  If a parent node is missing
                  print("Problem adding parent node to the tree")
         return tree
      else:
         return 0
