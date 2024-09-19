---
title: Digital Scholarship and Initiatives
layout: default
---

<div style="display: flex; flex-direction: column; align-items: center;">
  <div style="width: 100%; max-width: 60rem;">
    <h2>About us</h2>
    <hr style="border: none; height: 4px; background-color: #f1be48; width: 100px; margin: 7px 0;">
    <p>Digital Scholarship and Initiatives (DSI) is comprised of three units: digital scholarship, the digital repository, and digital collections. Our department supports the development of digital research projects; assists students, faculty, and staff in learning to use digital tools; and provides online access to ISU scholarship and historic materials.</p>
    <p> We can be found in The Catalyst, an events and collaboration space managed by DSI along with our partners in the Library's <a href="https://www.lib.iastate.edu/research-and-teach/data-services">Research Data Services</a> and <a href="https://www.lib.iastate.edu/collections/digital-press">ISU Digital Press</a> Units. Learn more <a href="http://127.0.0.1:4000/about.html">about DSI</a>.</p>
  </div>
  <br>
    <div class="card-container" style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
        <div class="card" style="width: 18rem; background-color: #CAC7A7">
            <img src="assets\img\blackisc_map.jpg" class="card-img-top" alt="...">
            <div class="card-body">
            <h5 class="card-title">Digital Scholarship</h5>
            <p class="card-text">Integrate digital tools and methods into research, instruction, and publication to gain new insights and teach new skills.</p>
            <a href="https://www.lib.iastate.edu/research-and-teach/digital-scholarship" class="btn bg-iastate-gold" target="_blank" rel="noopener noreferrer">Learn more</a>
            </div>
        </div>
        <div class="card" style="width: 18rem; background-color: #CAC7A7">
            <img src="assets\img\DR_Student-Research.svg" class="card-img-top" alt="...">
            <div class="card-body">
            <h5 class="card-title">Digital Repository</h5>
            <p class="card-text">Scholarly work, both unpublished and published, by current or emeritus ISU faculty, staff, and students. Includes theses and dissertations.</p>
            <a href="https://dr.lib.iastate.edu/" class="btn bg-iastate-red" target="_blank" rel="noopener noreferrer" style="color: white; margin-bottom: 10px;">Explore the Digital Repository</a>
            <a href="https://www.lib.iastate.edu/collections/digital-repository-iowa-state-university" class="btn bg-iastate-gold" target="_blank" rel="noopener noreferrer">Learn more</a>
            </div>
        </div>
        <div class="card" style="width: 18rem; background-color: #CAC7A7">
            <img src="https://digitalcollections.lib.iastate.edu/iiif/2/isu:WPA_b6f10i5~JP2~~isu_public/full/500,/0/default.jpg" class="card-img-top" alt="...">
            <div class="card-body">
            <h5 class="card-title">Digital Collections</h5>
            <p class="card-text">Digital materials representing many of the library’s rare and unique resources, which document Iowa State University, Iowa, and beyond.</p>
            <a href="https://digitalcollections.lib.iastate.edu/" class="btn bg-iastate-red" target="_blank" rel="noopener noreferrer" style="color: white; margin-bottom: 10px;">Explore our Digital Collections</a>
            <a href="https://www.lib.iastate.edu/collections/digital-collections" class="btn bg-iastate-gold" target="_blank" rel="noopener noreferrer">Learn more</a>
            </div>
        </div>
        <div class="card" style="width: 18rem; background-color: #CAC7A7">
            <img src="assets\img\The Catalyst space 2 - reduced size.jpg" class="card-img-top" alt="...">
            <div class="card-body">
            <h5 class="card-title">The Catalyst</h5>
            <p class="card-text">Our space for consultations, workshops, collaborations, and events. Shared with Research Data Services and the ISU Digital Press.</p>
            <a href="https://www.lib.iastate.edu/visit-and-study/creation-and-learning-spaces/catalyst" class="btn bg-iastate-gold" target="_blank" rel="noopener noreferrer">Learn more</a>
            </div>
        </div>
    </div>
    <br>
</div>

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