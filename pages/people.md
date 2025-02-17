---
title: People
nav: People
permalink: /people/
layout: page
nav_order: 1
---

{%- assign staff = site.data.dsi-people | where_exp: 's', 's.title != "Student"' -%}
{%- assign students = site.data.dsi-people | where_exp: 'p', 'p.title == "Student"' -%}

## Staff
{:.pt-3 .pb-0}

<div class="row">
    {%- for s in staff -%}
        <div class="col-md-6">
            <div class="row pt-3 pb-5 align-items-center">
                <div class="col-md-5 text-center">
                    <img class="img-fluid rounded-circle lazyload w-75" alt="image of {{ s.name }}" src="{{ s.image }}">
                </div>
                <div class="col-md-7">
                    <p>
                        <strong><a href="{{ s.name | slugify | append: '.html' | prepend: '/people/' | relative_url }}">{{ s.name }}</a></strong>, {{ s.title }}   
                        <br>
                        <a href="mailto:{{ s.email }}" class="text-decoration-underline">{{ s.email }}</a>
                        <br>
                        {% if s.phone %}<strong>{{ s.phone }}</strong>{% endif %}
                    </p>
                </div>
            </div>
        </div> 
    {%- endfor -%}
</div>

## Students
{:.pb-0}

<div class="row pb-3">
    <div class="col-md-12">
        <ul>
            {%- for p in students -%}
            <li>{{ p.name }}</li>
            {%- endfor -%}
        </ul>
    </div>
</div>
