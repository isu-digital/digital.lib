---
title: Digital Scholarship and Initiatives
layout: default
---
<style>
  .about-us-card {
    width: 18rem;
    background-color: #CAC7A7;
    transition: background-color 0.3s ease;
    cursor: pointer; /* Change cursor to pointer to indicate it's clickable */
  }
  .about-us-card:hover {
    background-color: #9B945F; /* Replace with your desired highlight color */
  }
  .btn-spacing {
    margin-bottom: 10px;
  }
</style>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.about-us-card').forEach(function(card) {
      card.addEventListener('click', function() {
        const link = card.getAttribute('data-link');
        if (link) {
          window.open(link, '_blank');
        }
      });
    });

    document.querySelectorAll('.about-us-card .btn').forEach(function(button) {
      button.addEventListener('click', function(event) {
        event.stopPropagation(); // Prevent the card click event from firing
      });
    });
  });
</script>

<div style="display: flex; flex-direction: column; align-items: center;">
  <div style="width: 100%; max-width: 60rem;">
    <h2>About us</h2>
    <hr style="border: none; height: 4px; background-color: #f1be48; width: 100px; margin: 7px 0;">
    <p>Digital Scholarship and Initiatives (DSI) is comprised of three units: digital scholarship, the digital repository, and digital collections. Our department supports the development of digital research projects; assists students, faculty, and staff in learning to use digital tools; and provides online access to ISU scholarship and historic materials.</p>
    <p> We can be found in The Catalyst, an events and collaboration space managed by DSI along with our partners in the Library's <a href="https://www.lib.iastate.edu/research-and-teach/data-services" target="_blank" rel="noopener noreferrer">Research Data Services</a> and <a href="https://www.lib.iastate.edu/collections/digital-press" target="_blank" rel="noopener noreferrer">ISU Digital Press</a> units. Learn more <a href="http://127.0.0.1:4000/pages/about.html" target="_blank" rel="noopener noreferrer">about DSI</a>.</p>
  </div>
  <br>
  <div class="card-container" style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
    <div class="card about-us-card" data-link="https://www.lib.iastate.edu/research-and-teach/digital-scholarship">
      <img src="assets\img\blackisc_map.jpg" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Digital Scholarship</h5>
        <p class="card-text">Integrate digital tools and methods into research, instruction, and publication to gain new insights and teach new skills.</p>
      </div>
    </div>
    <div class="card about-us-card" data-link="https://www.lib.iastate.edu/collections/digital-repository-iowa-state-university">
      <img src="assets\img\dr_dissertation.jpg" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Digital Repository</h5>
        <p class="card-text">Scholarly work, both unpublished and published, by current or emeritus ISU faculty, staff, and students. Includes theses and dissertations.</p>
        <a href="https://dr.lib.iastate.edu/" class="btn bg-iastate-red btn-spacing" target="_blank" rel="noopener noreferrer" style="color: white;">Explore the Digital Repository</a>
      </div>
    </div>
    <div class="card about-us-card" data-link="https://www.lib.iastate.edu/collections/digital-collections">
      <img src="https://digitalcollections.lib.iastate.edu/iiif/2/isu:WPA_b6f10i5~JP2~~isu_public/1200,900,3000,2250/500,/0/default.jpg" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Digital Collections</h5>
        <p class="card-text">Digital materials representing many of the library’s rare and unique resources, which document Iowa State University, Iowa, and beyond.</p>
        <a href="https://digitalcollections.lib.iastate.edu/" class="btn bg-iastate-red btn-spacing" target="_blank" rel="noopener noreferrer" style="color: white;">Explore our Digital Collections</a>
      </div>
    </div>
    <div class="card about-us-card" data-link="https://www.lib.iastate.edu/visit-and-study/creation-and-learning-spaces/catalyst">
      <img src="assets\img\catalyst4.jpg" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">The Catalyst</h5>
        <p class="card-text">Our space for consultations, workshops, and events. Shared with our partners in Research Data Services and the ISU Digital Press.</p>
      </div>
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