---
title: About Us
nav: About Us
layout: people
nav_order: 2
---

{% assign people = site.data.dsi-people %}

{% for p in people %}

{% if p.position contains "Digital Scholarship" %}
**{{ p.name }}**, {{ p.position }}
- {{ p.description }}
{% endif %}

{% endfor %}


Write pages in Markdown.

## Heading Two 

### Heading Three

Any text with no empty lines between will become a paragraph.
Leave an blank line between headings and paragraphs.
Font can be *Italic* or **Bold**. ***Both***
Code can be highlighted with `backticks`.

Hyperlinks look like this [GitHub Help](https://help.github.com/).

<https://help.github.com/>

### Lists 

A bullet list is created using `*`, `+`, or `-`, like:

- dog
- cat
- muffin

A numbered list is created using a number + `.`, like:

1. one
2. two
6. three
2. four

Horizontal rule:

--------------

{% include figure.html img="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/VAN_CAT.png/480px-VAN_CAT.png" alt="white cat" caption="I found this [Cat image on Wikimedia](https://commons.wikimedia.org/wiki/File:VAN_CAT.png)." %}

> A block quote.
> Is like this.
{:.blockquote}

### A Table

| header | column a | column b |
| --- | --- | --- |
| dogs | 3 | 6 |
| cats | 3 | 6 |
| muffins | 15 | 30 |
{:.table .table-striped}
