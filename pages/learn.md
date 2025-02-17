---
title: Learn With Us
nav: Learn
permalink: /learn/
layout: page
nav_order: 5
---

{%- assign workshops = site.data.dsi-workshops -%}
{%- assign events = site.data.dsi-events | where_exp: 'event', 'event.type != "workshop"' -%}

Check out current and upcoming workshops and events taught or hosted by Digital Scholarship and Initiatives.
Past workshops can be viewed on our [workshop archive page](/learn/workshop-archive.html).

## Workshops
{:.pb-0}

<div class="row ps-5">
    <div class="col-md-12">
    {%- for w in workshops -%}
        <a class="fs-5 fw-bold text-primary text-decoration-underline" href="{{ w.link }}" target="_blank" rel="noopener">{{ w.name }}</a>
        <p>{{ w.date }}, {{ w.time }}
        <br>
        {{ w.location }}</p>
    {%- endfor -%}
    </div>
</div>

## Upcoming Events
{:.pb-0}

<div class="row ps-lg-5">
{%- for e in events -%}
{%- if e.past != "true" -%}
<div class="col-md-3">
    <div class="card text-center mb-4">
        <img src="{{ e.image }}" class="card-img-top" alt="{{ e.image_alt }}">
        <div class="card-body">
            <p class="card-title fs-5 fw-bold text-primary">{{ e.name }}</p>
            <p class="card-text">{{ e.date }}, {{ e.location }}</p>
            <a href="{{ e.link }}" class="btn btn-outline-primary" target="_blank" rel="noopener">More Info</a>
        </div>
    </div>
</div>
{%- endif -%}
{%- endfor -%}
</div>

## Past Events
{:.pb-0}

<div class="row ps-lg-5">
    {%- for e in events -%}
    {%- if e.past == "true" -%}
    <div class="col-md-3">
        <div class="card text-center mb-4">
            <img src="{{ e.image }}" class="card-img-top" alt="{{ e.image_alt }}">
            <div class="card-body">
                <p class="card-title fs-5 fw-bold text-primary">{{ e.name }}</p>
                <p class="card-text">{{ e.date }}, {{ e.location }}</p>
                <a href="{{ e.link }}" class="btn btn-outline-primary" target="_blank" rel="noopener">More Info</a>
            </div>
        </div>
    </div>
    {%- endif -%}
    {%- endfor -%}
</div>