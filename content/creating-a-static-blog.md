---
title: code is a relationship
date: 2020-06-28 19:11
tags: code, blog
---
It's all about the concept of inputs and outputs. You put something in, you get something out. A static website is a little like that.

What makes it static, is that data lives apart from the html. To accommodate for changes in the data, we have to recompile the whole thing. Thankfully, that's quick and easy to automate.

So, what's our input? It looks something like this:

```markdown
title: my favourite quote from cat's cradle
---
"Peculiar travel suggestions are dancing lessons from god."
- Kurt Vonnegut
```

Markdown is an in-line formatting language that can be used to quickly create lists, tables, code blocks like the one above, and etc. But, the biggest advantage is that it translates well to html.

So, this marks our first step, parsing and converting the input.

To do that, we have to do two things. First, we'll create templates which will tell the data where to go:

```jinja
{ % block content % }
  <article>
    <h2> {{ post.title }} </h2>
    {{ post.content }}
  </article>
{ % endblock % }
```

And, of course, write some logic. Python is a good choice, because we don't care about speed and it's highly semantic. I've always liked that trade off.

```python
for post_name in posts:
    post_metadata = posts[post_name].metadata

    post_data = {
        'title': post_metadata['title'],
        'content': posts[post_name]
    }

    post_html = post_template.render(post=post_data)

    with open(post_name + '.html', 'w') as post:
        post.write(post_html)
```

Here we're going through the posts one by one, parsing their data, converting it, and pushing it through the template.

This produces freshly baked html:

```html
<article>
  <h2>my favourite quote from cat's cradle</h2>
  <p>"Peculiar travel suggestions are dancing lessons from god."</p>
  <p>- Kurt Vonnegut</p>
</article>
```

We've got the structure down, but we're still missing styling. Let's fix that and make things pretty with CSS:

```css
article {
  font: 12pt/1.8 Body, serif;
  color: #404040;
}

h2 {
  font-size: 19pt;
}

```

The last step is to write some composition logic which will manage the chunks of data we got above. Inheritance and nested templates are great for this.

The rest is usability, later I might add a tiny ecosystem with drafts and a database, but for now this should be enough.
