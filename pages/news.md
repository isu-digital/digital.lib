---
layout: page
title: News and Updates
nav: News
permalink: /news.html
nav_order: 4
---

{% assign posts = site.posts %}

{%- if posts.size > 0 -%}
  {%- if page.list_title -%}
    <h2 class="post-list-heading">{{ page.list_title }}</h2>
  {%- endif -%}
  <ul class="post-list">
    {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
    {%- for post in posts -%}
    <li>
      {% if post.image %}
      <img src="{{ post.image | relative_url }}" class="blog-roll-image" alt="{{ post.image-alt }}"> 
      {% endif %}
      <h2>
        <a class="post-link" href="{{ post.url | relative_url }}">
          {{ post.title | escape }}
        </a>
      </h2>
      <span class="post-meta">{{ post.date | date: date_format }}</span>
      {%- if site.show_excerpts -%}
        <p>{{ post.excerpt }}</p>
      {%- endif -%}
      {%- if post.tags -%}
        <p class="post-tags">Tags: {% for tag in post.tags %}<a href="{{ '/tags/' | append: tag | relative_url }}" class="post-tag" class="text-decoration-underline">{{ tag }}</a>{% if forloop.last == false %}, {% endif %}{% endfor %}
        </p>
      {%- endif -%}
    </li>
    {%- endfor -%}
  </ul>
{%- endif -%}

----------

{% for p in posts %}
<div class="card mb-3">
    <div class="card-body">
        <h3 id="{{ u.title | slugify }}" class="card-title">{{ page.list_title }}</h3>
        <div class="card-text">
        <p><small>Updated: {{ post.date | date_to_string: "ordinal", "US" }}</small></p>
        {{ post.content }}
        </div>
    </div>
</div>
{% endfor %}
