---
title: Digital Scholarship and Initiatives
layout: default
---
# Featured Projects

{% assign projects = site.data.dsi-research-projects %}
<div class="row">
    {% for p in projects %}
        {%if p.featured == "true" %}
        <div class="col-md-3">
            <div class="card text-center mb-4">
                <img src="{{ p.image }}" class="card-img-top" alt="{{ p.image_alt }}">
                <div class="card-body">
                    <p class="card-title">{{ p.title }}</p>
                    <a href="{{ p.link }}" class="btn btn-outline-primary" target="_blank"      rel="noopener">View Project</a>
                </div>
            </div>
        </div>
        {% endif %}
    {% endfor %}
</div>