---
layout: manual
title: About
permalink: /about/
---

# Key Dates

 <!-- Key Dates -->
    <section id="about">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <h2 class="section-heading text-uppercase">Key Dates</h2>
            <h3 class="section-subheading text-muted">Dates to Know.</h3>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-12">
            <ul class="timeline">
	    {% for deadline in site.data.deadlines %}
              <li>
                  <a href="{{ deadline.url | prepend: site.baseurl }}"><div
                                  class="timeline-image"><img
                                  class="rounded-circle img-fluid" src="{{
                                  deadline.img }}" alt="">
                                  <h3>{{ deadline.date | date: "%b %-d" }}<br/>
                                  {{ deadline.date | date: "%Y" }}</h3>
                          </div></a>
                <div class="timeline-panel">
                  <div class="timeline-heading">
                          <br/><br/><h3 class="subheading">{{ deadline.title }}</h3>
                  </div>
                </div>
              </li>
	      {% endfor %}
            </ul>
          </div>
        </div>
      </div>
    </section>


# Code of Conduct

# History

# Organizers

# Participants
