---
title: Projects
nav: Projects
permalink: /projects.html
layout: page
nav_order: 2
---


Digital Scholarship and Initiatives conducts research and provides project support and collaboration with students, faculty, and staff from across campus. Check out some of our work.

<div id="documentList">
    <div class="input-group mb-3">
        <input type="text" id="listSearch" class="form-control form-control-lg search" aria-label="Text input to filter list" placeholder="Filter...">
        <button class="btn btn-lg btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="collapse" data-bs-target="#collapseListOptions" aria-expanded="false" aria-controls="collapseListOptions">options</button>
        <div class="collapse w-100" id="collapseListOptions">
            <div class="card card-body">
                <p>Sort by:</p>
                <p>
                    <input type="radio" class="btn-check" name="sort_list" id="list_shuffle" autocomplete="off" checked>
                    <label class="btn btn-outline-info m-1" for="list_shuffle">Random</label>
                    <input type="radio" class="btn-check sort" name="sort_list" id="list_title" autocomplete="off" data-sort="listTitle">
                    <label class="btn btn-outline-info m-1" for="list_title">Title</label>
                    <input type="radio" class="btn-check sort" name="sort_list" id="list_type" autocomplete="off" data-sort="listType">
                    <label class="btn btn-outline-info m-1" for="list_type">Type</label>
                </p>
                <p>View item types:</p>
                <p>
                    <input type="radio" class="btn-check" name="filterRadio" id="filter-all" autocomplete="off" value="show-all" checked>
                    <label class="btn btn-outline-primary m-1" for="filter-all">All</label>
                    {% assign types = site.dsi-research-projects | where_exp: 'i','i.ignore != true' | map: 'type' | compact | uniq %}
                    {% for t in types %}
                    <input type="radio" class="btn-check" name="filterRadio" id="filter-{{ t | slugify }}" autocomplete="off" value="{{ t }}">
                    <label class="btn btn-outline-primary m-1" for="filter-{{ t | slugify }}">{{ t }}</label>
                    {% endfor %}
                </p>
            </div>
        </div>
    </div>
    <div class="mt-5 list row row-cols-1 row-cols-md-2"></div>
</div>

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
