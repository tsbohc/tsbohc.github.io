---
title: creating a static blog
date: 2020-06-28 19:11
tags: code, blog
---
Code is like a relationship. It's all about the concept of inputs and outputs. You put something in, you get something out. A static website is a little like that.

We're making a blog, so what's our input? I chose Markdown because I'm used to it and because it translates well to html. It looks something like this:

```markdown
title: my favourite quote from cat's cradle
date: 2020-06-28 19:11
---
"Peculiar travel suggestions are dancing lessons from god."
- Kurt Vonnegut
```

It's an in-line formatting language that has a bunch of stuff to quickly create lists, tables, code blocks like the one above, and etc. So, this marks our first step, parsing the input.

The second step is to take the parsed data, define how and where it should belong, and push it through some templates, producing freshly baked html. After that's done, we get this:

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

The last step to write some logic while taking advantage of inheritance and nested templates. That's how we end up with customized, yet coheret pages.

We should also tell things where they should be and how they should look with CSS.

The rest is usability, maybe I'll add a tiny ecosystem with drafts and a database, but for now this should be enough.
