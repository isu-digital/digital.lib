---
title: Learn With Us
nav: Learn
permalink: /learn.html
layout: page
nav_order: 5
---
## Workshops


## Upcoming Events
{% assign events = site.data.dsi-events %}
<div class="row">
    {% for e in events %}
    {% if e.past != "true" %}

    <div class="col-md-3">
        <div class="card text-center mb-4">
            <img src="{{ e.image }}" class="card-img-top" alt="{{ e.image_alt }}">
            <div class="card-body">
                <h5 class="card-title">{{ e.name }}</h5>
                <p class="card-text">{{ e.date }}, {{ e.location }}</p>
                <a href="{{ e.link }}" class="btn btn-outline-primary" target="_blank" rel="noopener">More Info</a>
            </div>
        </div>
    </div>
    {% endif %}
    {% endfor %}
</div>

## Past Events

<div class="row">
    {% for e in events %}
    {% if e.past == "true" %}
    <div class="col-md-3">
        <div class="card text-center mb-4">
            <img src="{{ e.image }}" class="card-img-top" alt="{{ e.image_alt }}">
            <div class="card-body">
                <h5 class="card-title">{{ e.name }}</h5>
                <p class="card-text">{{ e.date }} {{ e.location }}</p>
                <a href="{{ e.link }}" class="btn btn-outline-primary" target="_blank" rel="noopener">More Info</a>
            </div>
        </div>
    </div>
    {% endif %}
    {% endfor %}
</div>