<!--
name: blagsh
peek: Portmanteaus and why I'm not allowed to make websites anymore.
tags: blog bash
date: 1629741133
-->

What tools would satisfy my minimalist heart? I sneered at python. I let jinja go. I pondered for a while. The next night, the fated words *parameter expansion in bash* came to me in my sleep.

```bash
t:post() {
  local name ; name="$(f:meta "$1" name)"
  t:body "$name" "
    <main>
      <article>
        <h1>$name</h1>
        $(render "$(<"p/$1/raw.md")")
        <div id='meta'>$(t:date "$1") $(t:tags "$1")</div>
      </article>
    </main>"
}
```

Here's a short bash poem, depicting you, the reader:

```bash
:|| echo "if i could speak i'd grumble"
```

## design

Visually, I wanted the blog to feel distinctly text-centric. CSS-wise, that entailed creating a monochrome pallette and abusing pseudo-elements to capture that raw markdown vibe.

Despite the templating code being the bastard child of bash and JSX, I quite like it. Having direct access to system commands is nice.

```
t:date() {
  echo -n "
    <time datetime='$(date '+%Y-%m-%d %H:%M' -d "@$1")'>
      $(date '+%d%m%y' -d "@$1")
    </time>"
}
```

Around the back, I ended up embedding metadata into markdown files as comments and parsing it with regex. As far as frugal solutions go, I think it's the best one.

```
├── 1633785019
│   ├── index.html
│   └── raw.md
└── 1633890762
    ├── index.html
    └── raw.md
```

The UNIX timestamp makes for a good permalink, and I don't mind being a little cryptic. To make finding the right post easier, I'm extracting the metadata and feeding it into fzf.

```
f:edit() { # select post in fzf to nvim
  raw="$(for p in "p/"*; do
    f:meta "${p##*/}" date name peek tags
  done | awk -F "^I" '{ print $1" "$2" "$3" ("$4")" }' | fzf)"
  [[ -n "$raw" ]] && nvim "$(awk -F " " '{ print "p/"$1"/raw.md" }' <<< "$raw")"
}
```

There is a subcommand in the script that launches *http-server* and recompiles the html on change via *entr*.

With something like this, there really isn't much to talk about. If you're curious, I'll let the [code](https://github.com/tsbohc/tsbohc.github.io/blob/master/honeycake) speak for itself.
