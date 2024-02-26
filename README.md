# README

## Project Overview :
This project was completed for CS091 (Social Crowd and Computing) under the guidance of Dr. Sukrit Venkatagiri in collaboration with Felicia Yi '26 and Anusha Bhatia '24. 
We implemented a chatbot for a Mastodon server that summarizes mass comment sections using natural language processing. To prepare for the implementation, we conducted research
about Mastodon APIs and social/computing issues to address. 

## Resources:
GitHub refresher: https://coderuse.com/2017/10/A-Short-Refresher-On-Git/

Flask Quick Start Guide: https://flask.palletsprojects.com/en/3.0.x/quickstart/

Intro to HTML Guide: https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started

Python refresher: https://code.tutsplus.com/series/a-smooth-refresher-to-python–cms-950

Introduction to Flask: https://pymbook.readthedocs.io/en/latest/flask.html, https://opensource.com/article/18/4/flask

## Installation:

1. Install virtualenv:

   `pip3 install virtualenv`
   
2. Create your virtual environment:

   `virtualenv venv`

3. Actrive your virtual environment:

   `source venv/bin/activate`

4. Install Mastodon, Flask and its dependencies within your virtual environment:

   `pip3 install Mastodon.py`
   `pip3 install flask`

5. Install all other packages used that are not already downloaded on your computer (some examples are below): 

   `pip3 install asyncio`
   `pip3 install openai`
   `pip3 install bs4`
   `pip3 install treelib`
   `pip3 install flask_sqlalchemy`
   `pip3 install flask_migrate`

6. Create two files 
   
   a. chatgpt_token - put our chapGPT API token
   
   b. user_token - place user token for Mastodon you want the summary to be posted from 

   Also, run `export OPENAI_API_KEY={your_key}` on terminal after activating your virtual environmnt before running the flask app. 
   

## Running the app:
`my_app` is the main directory or "application factory" for Flask and `__init__.py`` tells Python that the `my_app` directory should be treated as a package. To run your flask app:

`flask --app my_app run --debug --port 8000`

Note that if you can't access the app on that port, try a different one, like 5000 or 8080.

## Structure:
- `my_app` is the main directory or "application factory" for Flask
- `__init__.py` is the main app that handles incoming requests for your web server
- `templates` is the directory that holds all of your HTML files
- `static` is the directory that holds all of your CSS and Javascript files
- Don't forget to add a `.gitignore` file! This will prevent you from accidentally pushing your virtual environment and other files to GitHub.


## Build Part 1
### Requirements
1. Be able to detect when there is a new post that uses #summarizethis and output the comment ID
2. Given the comment ID, be able to take the ancestors and descendants of the comment and build a comment tree that will later be put into the NLP
3. Be able to post the summary on Mastodon as reply to the post that used the hashtag #summarizethis

** As per our talk earlier, these requirements are updated and different from the original writeup. 

### HTML routes
1. /posts/ - gives the ID of the post that used #summarizethis
2. /comment_tree/ - shows the comment tree that will be put into the NLP
3. /summary/ - can enter the summary which will then be posted as a reply to the original post that used the hashtag 


## Build Part 2
### Why Chatgpt
We chose ChatGPT because we wanted to use an abstractive NLP summarizer. A lot of the more commonly used summarizers like NLTK, Gensim, or SpaCy are all extractive NLPs and did not provide the kind of summaries that we were looking for. After implementing both NLTK and ChatGPT, we found ChatGPT's summaries to be much more comprehensive and we could also adjust the prompts in the future to provide different types of summaries. We also looked into Pegasus as another abstractive type of NLP with a larger character limit but it was much harder to implement and did not have as much documentation as ChatGPT. Overall, we prioritized the quality of the summaries and ease to implement over other criteria so ChatGPT was the best option for our project. 
