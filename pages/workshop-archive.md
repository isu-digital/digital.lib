---
title: Workshop and Event Archive
permalink: /learn/workshop-archive.html
layout: workshop-archive
---

{%- assign workshops = site.data.dsi-workshops-old | sort: "date-iso" | reverse -%}
{%- assign events = site.data.dsi-events | sort: "date-iso" | reverse -%}

Explore past workshops and events hosted, sponsored, or partnered on by Digital Scholarship and Initiatives. (Alternatively, [see current events](/learn/).)

## 2025
{:.pb-0}

{% assign workshops2025 = workshops | where_exp: 'w', 'w.date-iso contains "2025"' -%}
{% assign events2025 = events | where_exp: 'e', 'e.date-iso contains "2025"' -%}
<div class="row ps-5">
    {%- if workshops2025.size > 0 -%}
    <div class="col-md-12">
    <p class="fs-4 fw-bold text-cardinal ps-5 ps-md-0">Workshops</p>
    <ul>
        {%- for w in workshops2025 -%}
        <li><a class="fs-5 fw-bold text-primary text-decoration-underline" href="{{ w.link }}" target="_blank" rel="noopener">{{ w.name }}</a> ({{ w.date }})</li>
        {%- endfor -%}
    </ul>
    </div>
    {%- endif -%}
    {%- if events2025.size > 0 -%}
    <div class="col-md-12">
        <p class="fs-4 fw-bold text-cardinal ps-5 ps-md-0">Events</p>
        <ul>
            {%- for e in events2025 -%}{%- if e.past == "true" -%}
            <li><a class="fs-5 fw-bold text-primary text-decoration-underline" href="{{ e.link }}" target="_blank" rel="noopener">{{ e.name }}</a> ({{ e.date }})</li>
            {%- endif -%}{%- endfor -%}
        </ul>
    </div>
    {%- endif -%}
</div>

## 2024
{:.pb-0}

{% assign workshops2024 = workshops | where_exp: 'w', 'w.date-iso contains "2024"' -%}
{% assign events2024 = events | where_exp: 'e', 'e.date-iso contains "2024"' -%}
<div class="row ps-5">
    {%- if workshops2024.size >0 -%}
    <div class="col-md-12">
    <p class="fs-4 fw-bold text-cardinal ps-5 ps-md-0">Workshops</p>
    <ul>
        {%- for w in workshops2024 -%}
        <li><a class="fs-5 fw-bold text-primary text-decoration-underline" href="{{ w.link }}" target="_blank" rel="noopener">{{ w.name }}</a> ({{ w.date }})</li>
        {%- endfor -%}
    </ul>
    </div>
    {%- endif -%}
    {%- if events2024.size >0 -%}
    <div class="col-md-12">
        <p class="fs-4 fw-bold text-cardinal ps-5 ps-md-0">Events</p>
        <ul>
            {%- for e in events2024 -%}
            <li><a class="fs-5 fw-bold text-primary text-decoration-underline" href="{{ e.link }}" target="_blank" rel="noopener">{{ e.name }}</a> ({{ e.date }})</li>
            {%- endfor -%}
        </ul>
    </div>
    {%- endif -%}
</div>

## 2023
{:.pb-0}

{% assign workshops2023 = workshops | where_exp: 'w', 'w.date-iso contains "2023"' -%}
{% assign events2023 = events | where_exp: 'e', 'e.date-iso contains "2023"' -%}
<div class="row ps-5">
    {%- if workshops2023.size >0 -%}
    <div class="col-md-12">
    <p class="fs-4 fw-bold text-cardinal ps-5 ps-md-0">Workshops</p>
    <ul>
        {%- for w in workshops2023 -%}
        <li><a class="fs-5 fw-bold text-primary text-decoration-underline" href="{{ w.link }}" target="_blank" rel="noopener">{{ w.name }}</a> ({{ w.date }})</li>
        {%- endfor -%}
    </ul>
    </div>
    {%- endif -%}
    {%- if events2023.size >0 -%}
    <div class="col-md-12">
        <p class="fs-4 fw-bold text-cardinal ps-5 ps-md-0">Events</p>
        <ul>
            {%- for e in events2023 -%}
            <li><a class="fs-5 fw-bold text-primary text-decoration-underline" href="{{ e.link }}" target="_blank" rel="noopener">{{ e.name }}</a> ({{ e.date }})</li>
            {%- endfor -%}
        </ul>
    </div>
    {%- endif -%}
</div>
