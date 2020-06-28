---
title: creating a static blog
date: 2020-06-28 19:11
tags: code, blog
---
Code is like a relationship. It's all about the concept of inputs and outputs. You put something in, you get something out. Despite the boring name, a static website is kinda like that.

It accepts raw human readable text files, and produces machine readable data. Which in turn, by some unknown magic of your browser, turns into the page you're reading right now.

So, we're making a blog, and our input looks something like this:

```markdown
title: my favourite quote from cat's cradle
date: 2020-06-28 19:11
---
"Peculiar travel suggestions are dancing lessons from god."
- Kurt Vonnegut
```

Markdown is an in-line formatting language that translates well to html and has a bunch of stuff to quickly create lists, tables, code blocks like the one above, and etc. This marks the first step, parsing the input.

Our second step is to take the parsed data, define how and where it should belong, and push it through some templates, producing freshly baked html. After that's done, we get this:

```html
<article>
  <h2>
    <a href="my-favourite-quote-from-cats-cradle.html">
      my favourite quote from cat's cradle
    </a>
  </h2>
  <p>"Peculiar travel suggestions are dancing lessons from god."</p>
  <p>- Kurt Vonnegut</p>
</article>
<div class="date">Jun, 28</div>
```

The last step is to take advantage of inheritance and nested templates to produce coherent web pages. And of course tell things where they should be and how they should look with CSS.

The rest is usability, maybe I'll add a tiny ecosystem with drafts and a database, but for now this should be enough.
