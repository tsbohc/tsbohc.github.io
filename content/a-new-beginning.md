---
title: a new beginning
date: 2020-06-27 21:25
tags: code, blog
---
It dawned on me that I have a tumblr blog which I've been neglecting for a while. And instead of pulling up vim and writing something profound, I thought to myself, "fuck tumblr, I'm gonna move to github pages."

That turned out to be simple enough, but of course I didn't stop there. I thought, "so they have that static website generator, and it looks pretty neat."

But it still wasn't autistic enough for me. And there I was, thinking, "Python's fun to iterate on, I should use that to code my own generator."

The funny thing is, the script itself is < 40 lines of code. Making things pretty and figuring out the templates did take some time, though. Speaking of pretty things and code:

```python
def main():
  print("hello, world!")

if __name__ == "__main__":
    main()
```

Pure stylesheet magic.

Each time I make an edit, the pages are recompiled and served to a local http server with live reload. Whenever I want to update the website, I make a commit and push files to github.

Everything is modular and easily extendable.
