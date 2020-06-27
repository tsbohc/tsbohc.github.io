import os
from datetime import datetime
from markdown2 import markdown
from jinja2 import Environment, PackageLoader

STATIC_PREFIX = '/'

env = Environment(loader=PackageLoader('sbg', 'templates'))
post_template = env.get_template('post.html')

HTML_POSTS = {}

# store post html into a dictionary
for file_name in os.listdir('content'):
    post_path = os.path.join('content', file_name)

    with open(post_path, 'r') as post:
        HTML_POSTS[file_name] = markdown(post.read(), extras=['metadata'])

# generate invididual posts
for file_name in HTML_POSTS:
    post_metadata = HTML_POSTS[file_name].metadata

    post_data = {
        'title': post_metadata['title'],
        #'date': post_metadata['date'],
        'content': HTML_POSTS[file_name],
        'tags': post_metadata['tags']
    }

    post_html = post_template.render(post=post_data)

    with open('posts/' + file_name[:-2] + 'html', 'w') as post:
        post.write(post_html)

# TODO:
# if date is not set, set current time (file creation time?)
# if it is, keep it

# probably will have to attach a random number to every post link
# to prevent link clashing

# pseudo-philosophy, anime, and programming
