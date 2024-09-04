---
layout: page
title: Erin Ridnour
---

{% assign author_name = "Erin" %} 

<h1>Posts by {{ author_name }}</h1>

<ul>
  {% for post in site.posts %}
    {% if post.author == author_name %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <p>{{ post.date | date: "%B %d, %Y" }}</p>
      </li>
    {% endif %}
  {% endfor %}
</ul>
