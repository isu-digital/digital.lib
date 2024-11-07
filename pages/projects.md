---
title: Projects
nav: Projects
layout: page
nav_order: 2
---


Digital Scholarship and Initiatives conducts research and provides project support and collaboration with students, faculty, and staff from across campus. Check out some of our work.

## Current Projects
{% assign projects = site.data.dsi-research-projects %}
<div class="row">
    {% for p in projects %}
    {% if p.status == "in-progress" or p.status == "ongoing" %}
    <div class="col-md-3">
        <div class="card text-center mb-4">
            <img src="{{ p.image }}" class="card-img-top" alt="{{ p.image_alt }}">
            <div class="card-body">
                <p class="card-title">{{ p.title }}</p>
                {% if p.link contains "http" %}
                <a href="{{ p.link }}" class="btn btn-outline-primary" target="_blank">View Project</a>
                {% else %}
                <a href="{{ p.link }}" class="btn btn-outline-primary">View Project</a>
                {% endif %}
            </div>
        </div>
    </div>
    {% endif %}
    {% endfor %}
</div>

## Browse All Projects

{% assign statuses = site.data.dsi-research-projects | map: 'status' | uniq %}
{% assign types = site.data.dsi-research-projects | map: 'type' | uniq %}

#### Filter by Status and Type
<div class="filter-container">
    <div class="btn-group mb-4" role="group" aria-label="Filter by Status">
        <button type="button" class="btn btn-outline-primary" onclick="filterProjects('all', 'status', this)">All</button>
        {% for status in statuses %}
        <button type="button" class="btn btn-outline-primary" onclick="filterProjects('{{ status }}', 'status', this)">{{ status | capitalize }}</button>
        {% endfor %}
    </div>

    <div class="btn-group mb-4" role="group" aria-label="Filter by Type">
        <button type="button" class="btn btn-outline-primary" onclick="filterProjects('all', 'type', this)">All</button>
        {% for type in types %}
        <button type="button" class="btn btn-outline-primary" onclick="filterProjects('{{ type }}', 'type', this)">{{ type | capitalize }}</button>
        {% endfor %}
    </div>
</div>

<div class="row" id="projects-container">
    {% assign projects = site.data.dsi-research-projects %}
    {% for p in projects %}
    <div class="col-md-3 project-card" data-status="{{ p.status }}" data-type="{{ p.type }}">
        <div class="card text-center mb-4">
            <img src="{{ p.image }}" class="card-img-top" alt="{{ p.image_alt }}">
            <div class="card-body">
                <p class="card-title">{{ p.title }}</p>
                <a href="{{ p.link }}" class="btn btn-outline-primary" target="_blank" rel="noopener">View Project</a>
            </div>
        </div>
    </div>
    {% endfor %}
</div>

<script>
let currentStatusFilter = 'all';
let currentTypeFilter = 'all';

function filterProjects(value, filterType, button) {
    if (filterType === 'status') {
        currentStatusFilter = value;
        setActiveButton(button, 'status');
    } else if (filterType === 'type') {
        currentTypeFilter = value;
        setActiveButton(button, 'type');
    }

    var cards = document.querySelectorAll('.project-card');
    cards.forEach(function(card) {
        var statusMatch = (currentStatusFilter === 'all' || card.getAttribute('data-status') === currentStatusFilter);
        var typeMatch = (currentTypeFilter === 'all' || card.getAttribute('data-type') === currentTypeFilter);

        if (statusMatch && typeMatch) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

function setActiveButton(button, filterType) {
    var buttonGroup = button.parentElement;
    var buttons = buttonGroup.querySelectorAll('.btn');
    buttons.forEach(function(btn) {
        btn.classList.remove('active');
    });
    button.classList.add('active');
}
</script>
