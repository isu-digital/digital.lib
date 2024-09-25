---
title: Digital Scholarship and Initiatives
layout: default
---

<link rel="stylesheet" href="assets/css/styles.css">
<script src="assets\js\indexcards.js"></script>


<div style="width: 100%; max-width: 60rem; margin: 0 auto;">
  <h1>About us</h1>
  <hr style="border: none; height: 4px; background-color: #f1be48; width: 100px; margin: 7px 0;">
  <p>Digital Scholarship and Initiatives (DSI) supports the development of digital research projects; assists students, faculty, and staff in learning to use digital tools; and provides online access to ISU scholarship and historic materials.</p>
  <p> We can be found in The Catalyst, an events and collaboration space managed by DSI along with our partners in the Library's <a href="https://www.lib.iastate.edu/research-and-teach/data-services" target="_blank" rel="noopener noreferrer">Research Data Services</a> and <a href="https://www.lib.iastate.edu/collections/digital-press" target="_blank" rel="noopener noreferrer">ISU Digital Press</a> units. Learn more <a href="http://127.0.0.1:4000/pages/about.html" target="_blank" rel="noopener noreferrer">about DSI</a>.</p>
</div>

<br>

<div class="card-container">
  <div class="card about-us-card">
    <img src="assets/img/blackisc_map.jpg" class="card-img-top" alt="...">
    <div class="card-body">
      <h4 class="card-title">Digital Scholarship</h4>
      <p class="card-text">Integrate digital tools and methods into research, instruction, and publication to gain new insights and teach new skills.</p>
      <a href="http://127.0.0.1:4000/pages/collaborate.html" class="btn btn-cards" target="_blank" rel="noopener noreferrer">Collaborate with us</a>
    </div>
  </div>
  <div class="card about-us-card">
    <img src="assets/img/dr_dissertation.jpg" class="card-img-top" alt="...">
    <div class="card-body">
      <h4 class="card-title">Digital Repository</h4>
      <p class="card-text">Scholarly work, both unpublished and published, by current or emeritus ISU faculty, staff, and students. Includes theses and dissertations.</p>
      <a href="https://dr.lib.iastate.edu/" class="btn btn-cards" target="_blank" rel="noopener noreferrer">Explore the Digital Repository</a>
    </div>
  </div>
  <div class="card about-us-card">
    <img src="https://digitalcollections.lib.iastate.edu/iiif/2/isu:WPA_b6f10i5~JP2~~isu_public/1200,900,3000,2250/500,/0/default.jpg" class="card-img-top" alt="...">
    <div class="card-body">
      <h4 class="card-title">Digital Collections</h4>
      <p class="card-text">Digital materials representing many of the library’s rare and unique resources, which document Iowa State University, Iowa, and beyond.</p>
      <a href="https://digitalcollections.lib.iastate.edu/" class="btn btn-cards" target="_blank" rel="noopener noreferrer">Explore our Digital Collections</a>
    </div>
  </div>
  <div class="card about-us-card">
    <img src="assets/img/catalyst4.jpg" class="card-img-top" alt="...">
    <div class="card-body">
      <h4 class="card-title">The Catalyst</h4>
      <p class="card-text">Our space for consultations, workshops, and events. Shared with our partners in Research Data Services and the ISU Digital Press.</p>
      <a href="https://www.lib.iastate.edu/visit-and-study/creation-and-learning-spaces/catalyst" class="btn btn-cards" target="_blank" rel="noopener noreferrer">Visit The Catalyst</a>
    </div>
  </div>
</div>

# Featured Projects

{% assign projects = site.data.dsi-research-projects %}
<div class="row">
    {% for p in projects %}
        {% if p.featured == "true" %}
        <div class="col-md-3">
            <div class="card text-center mb-4">
                <img src="{{ p.image }}" class="card-img-top" alt="{{ p.image_alt }}">
                <div class="card-body">
                    <p class="card-title">{{ p.title }}</p>
                    <a href="{{ p.link }}" class="btn btn-outline-primary" target="_blank" rel="noopener">View Project</a>
                </div>
            </div>
        </div>
        {% endif %}
    {% endfor %}
</div>