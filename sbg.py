import os
from datetime import datetime
from pygments import highlight
from markdown2 import markdown
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('sbg', 'templates'))

home_template = env.get_template('home.html')
post_template = env.get_template('post.html')

HTML_POSTS = {}

# store post html and metadata into a dictionary
for file_name in os.listdir('content'):
    post_path = os.path.join('content', file_name)
    with open(post_path, 'r') as post:
        HTML_POSTS[file_name] = markdown(post.read(), extras=['metadata', 'fenced-code-blocks'])

# generate invididual posts
posts_data = []
for file_name in HTML_POSTS:
    post_metadata = HTML_POSTS[file_name].metadata

    post_data = {
        'title': post_metadata['title'],
        'content': HTML_POSTS[file_name],
        'date': datetime.strptime(post_metadata['date'], '%d-%m-%y-%H-%M').strftime("%b, %d"),
        'tags': post_metadata['tags'],
        'name': file_name[:-3]
    }

    posts_data.append(post_data)
    post_html = post_template.render(post=post_data)

    with open(post_data['name'] + '.html', 'w') as post:
        post.write(post_html)

# compile index.html
posts_data.sort(key=lambda x:x['date'], reverse=True)
home_html = home_template.render(posts=posts_data)
with open('index.html', 'w') as index:
    index.write(home_html)

# TODO:
# if date is not set, set current time (file creation time?)
# if it is, keep it

# probably will have to attach a random number to every post link
# to prevent link clashing

# pseudo-philosophy, anime, and programming


