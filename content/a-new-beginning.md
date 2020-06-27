---
title: A New Beginning
date: 27-06-20-21-25
tags: code
---

It dawned on me that I have that tumblr blog and that I haven't posted anything in a while. And instead of pulling up vim and writing something profound, I thought to myself, "fuck tumblr, I'm gonna move to github."

That turned out simple enough, but of course I didn't stop there. I thought, "so they have that static website generator, and it looks pretty neat".

But it wasn't autistic enough for me. And there I was, thinking, "python's pretty fun to iterate on. I should use that to make my own generator."

And here we are.

The funny thing is, at the time of writing the generator itself is < 40 lines of code. Making things pretty and figuring out the templates did take a long time, though.

Speaking of pretty things and code, check out the snippet below:

```python
def main():
    answer = "the answer to the ultimate question of life, the universe, and everything there is {}".format(deep_thought())
    print(answer)
```

Pure stylesheet magic. For the record, the actual post looks like this:

```markdown
```python
def deep_thought():
  time.wait(75000000 * 31556952)
```

The formatting is done fully automatically, I just have to provide a hint at the language in the block.
