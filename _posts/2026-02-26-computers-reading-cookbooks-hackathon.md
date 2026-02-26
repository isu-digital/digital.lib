---
layout: post
title: Library Potluck and Hackathon Celebrating Newly Digitized Iowa Cookbooks
date: 2026-02-26
author: Erin
excerpt: In January, the Library Staff Association and the *Computers Reading Cookbooks* project hosted a library-wide potluck to celebrate major new additions to the Iowa Cookbook Digital Collection. 
tags: events text-analysis
image: assets/img/cookbook-banner.jpg
image-alt: 
---

In January, the Library Staff Association and the *Computers Reading Cookbooks* project hosted a library-wide potluck to celebrate major new additions to the [Cookbook Digital Collection](https://digitalcollections.lib.iastate.edu/cookbooks/). The collection of over 200 volumes features cookbooks published by Iowa communities, organizations, and individuals from the 19th through the 21st centuries curated from Special Collections and University Archives and the General Collection. This digitization effort began in summer of 2024 and was completed by a cross-departmental team from Special Collections and University Archives, Preservation, Metadata Services, and Digital Scholarship and Initiatives. 

All members of the library were invited to explore the newly digitized cookbooks and choose a recipe to prepare and share with colleagues. Attendees contributed nearly 30 dishes to the potluck spread including: Popcorn Cake from the [1984 Eddyville Oregon Trail Days Cookbook](https://digitalcollections.lib.iastate.edu/cookbooks/items/cookbooks28985.html), Scandinavian Kringla from a [1982 Friends of the Octagon cookbook](https://digitalcollections.lib.iastate.edu/cookbooks/items/cookbooks36005.html), and an intriguing noodle dish called “Zimmy Zammy” from the [1977 Ruth Circle Cookbook from Nevada, IA](https://digitalcollections.lib.iastate.edu/cookbooks/items/cookbooks32285.html).  

<div class="container my-4">
    <div class="gallery-grid my-4">
        <img src="/assets/img/news-img/20260129_120232.jpg" alt="Staff lounge full of people sitting at tables enjoying potluck food." class="short">
        <img src="/assets/img/news-img/20260129_110808.jpg" alt="Several people stand with plates at a long table of potluck dishes." class="tall">
        <img src="/assets/img/news-img/20260226_114028.jpg" alt="A recipe card for Angel Pie from the 1953 Congregational Cuisine cookbook." class="tall">
        <img src="/assets/img/news-img/20260129_105539.jpg" alt="A large glass bowl of green punch with lime slices." class="short">
    </div>
</div>

Additionally, a group of library staff participated in a hackathon to explore the Iowa community cookbooks text dataset, a corpus comprised of 200 OCR’d cookbooks published by Iowa community organizations from 1896-2009. Participants attended a kick-off workshop on January 26 for an introduction to the dataset and several suggested text analysis tools including VoyantTools, AntConc, and a guided Python Jupyter notebook. They then explored the dataset asynchronously throughout the week and discussed findings in a Teams chat. Topics explored included searching for vegetarian and vegan recipes, identifying the most popular fruits, finding and quantifying name variations for scotcheroos and taverns, and more. Check out some of the results of this exploration in the slide showcase below.
<div class="desktop-only">
  <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRYBj6h6Z95ybKpdoMJZ2gvC95iT375CkYLpncps0Ted93TLTvLglyDAFPLDC_saqX4OShEKnoZpdwA/pubembed?start=false&loop=true&delayms=10000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" title="Computers Reading Cookbooks Hackathon Showcase"></iframe>
</div>
<div class="mobile-only">
  <a href="https://docs.google.com/presentation/d/e/2PACX-1vRYBj6h6Z95ybKpdoMJZ2gvC95iT375CkYLpncps0Ted93TLTvLglyDAFPLDC_saqX4OShEKnoZpdwA/pub?start=true&loop=true&delayms=10000" target="_blank" rel="noopener">View the Hackathon Showcase Slides</a>
</div>

## About Computers Reading Cookbooks

[*Computers Reading Cookbooks*](https://emanderson811.github.io/computers-reading-cookbooks/) is a collections-as-data project examining a selection of community cookbooks from the Library’s Iowa Cookbook Collection. Using Python and natural language processing tools, this project analyzes the cookbook corpus to identify shared food traditions, trace how dishes evolve over time, and identify both common and culturally distinct recipes across Iowa communities.  

For more information contact [Erin Ridnour](mailto:emanders@iastate.edu).

<style>
.desktop-only { display: block; }
.mobile-only { display: none; }
@media (max-width: 767px) {
  .desktop-only { display: none; }
  .mobile-only { display: block; margin: 1em 0; }
}
.gallery-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 200px 200px;
  gap: 12px;
      width: 100%;
      max-width: 700px;
      margin-left: auto;
      margin-right: auto;
}
.gallery-grid img {
  width: 100%;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.gallery-grid .tall {
  grid-row: span 2;
  height: 412px;
}
.gallery-grid .short {
  height: 200px;
}
</style>
