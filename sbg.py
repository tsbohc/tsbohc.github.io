import inflect
import os
import sys
import argparse
import math
from datetime import datetime, date
from pygments import highlight
from markdown2 import markdown
from jinja2 import Environment, PackageLoader
from livereload import Server, shell

_inflect = inflect.engine()

def recompile():
    env = Environment(loader=PackageLoader('sbg', 'templates'))

    error_template = env.get_template('error.html')
    archive_template = env.get_template('archive.html')
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

        raw_date = datetime.strptime(post_metadata['date'], '%Y-%m-%d %H:%M')

        post_data = {
            'title': post_metadata['title'],
            'content': HTML_POSTS[file_name],
            'date': raw_date.strftime("%b, %d"),
            'raw_date': post_metadata['date'],
            'date_month': raw_date.strftime('%B'),
            'date_year': raw_date.strftime('%Y'),
            'date_year_words': _inflect.number_to_words(raw_date.strftime('%Y'), group=2).replace(',', ''),
            'tags': post_metadata['tags'].split(', '),
            'name': file_name[:-3]
        }

        posts_data.append(post_data)
        post_html = post_template.render(post=post_data)

        print(post_data['name'] + '.html')
        with open(post_data['name'] + '.html', 'w') as post:
            post.write(post_html)

    # sort by date in reverse
    posts_data.sort(key=lambda x:x['raw_date'], reverse=True)

    # generate index-0.html, index-1.html, and etc
    split_after = 5
    post_n = 0
    split_n = 0
    temp_data = []
    for index, post_data in enumerate(posts_data):
        print(index)
        temp_data.append(post_data)
        post_n += 1
        if post_n == split_after or index + 1 == len(posts_data):
            if split_n == 0:
                split = ''
            else:
                split = '-' + str(split_n)

            past_n = split_n + 1
            if past_n >= math.ceil(len(posts_data) / split_after):
                past_n = -1
            else:
                past_n = '-' + str(past_n)

            future_n = split_n - 1
            if future_n == 0:
                future_n = ''
            elif future_n < 0:
                future_n = -1
            else:
                future_n = '-' + str(future_n)


            temp_html = home_template.render(posts=temp_data, past=past_n, future=future_n)
            print('index' + split + '.html')
            with open('index' + split + '.html', 'w') as index:
                index.write(temp_html)

            temp_data = []
            post_n = 0
            split_n += 1

#    home_html = home_template.render(posts=posts_data)
#    print('index.html')
#    with open('index.html', 'w') as index:
#        index.write(home_html)

    archive_html = archive_template.render(posts=posts_data)
    print('archive.html')
    with open('archive.html', 'w') as archive:
        archive.write(archive_html)

    error_html = error_template.render()
    print('404.html')
    with open('404.html', 'w') as error:
        error.write(error_html)

def start_server():
    server = Server()
    server.watch('content/*.md', shell('python sbg.py -r'), delay=2)
    server.watch('templates/*.html', shell('python sbg.py -r'), delay=5)
    server.watch('static/*.css')
    server.serve()

def new_post():
    print('title:')
    new_title = input()
    new_name = new_title.lower().replace(' ', '-')
    new_name = new_name.replace(':', '')
    new_date = datetime.now().strftime('%Y-%m-%d %H:%M')

    # add %y%m- to the file names

    new_template = "---\ntitle: " + new_title + "\ndate: " + new_date + "\ntags: \n---\n\n"

    with open('content/' + new_name + '.md', 'w') as new_post:
        new_post.write(new_template)
    os.system('nvim content/' + new_name + '.md')

# --- main ---

if __name__ == "__main__":
    def getOptions(args=sys.argv[1:]):
        parser = argparse.ArgumentParser(description="Parses command.")
        parser.add_argument("-n", "--new", dest='new', action='store_true', help="new post")
        parser.add_argument("-r", "--recompile", dest='recompile', action='store_true', help="recompile html")
        parser.add_argument("-s", "--server", dest='server', action='store_true', help="localhost debug live server")
        options = parser.parse_args(args)
        return options

    options = getOptions(sys.argv[1:])

    if options.recompile:
        recompile()
    elif options.server:
        start_server()
    elif options.new:
        new_post()
