---
title: Workshop Archive
permalink: /learn/workshop-archive.html
layout: workshop-archive
---

{%- assign workshops = site.data.dsi-events | where_exp: 'event', 'event.type == "workshop"' -%}

Explore past workshops hosted, sponsored, or partnered on by Digital Scholarship and Initiatives. (Alternatively, [see current events](/learn/).)

## 2024
{:.pb-0}

<div class="row ps-5">
    <div class="col-md-12">
    <ul>
        {%- for w in workshops -%}
        <li><a class="fs-5 fw-bold text-primary text-decoration-underline" href="{{ w.link }}" target="_blank" rel="noopener">{{ w.name }}</a> ({{ w.date }})</li>
        {%- endfor -%}
    </ul>
    </div>
</div>
