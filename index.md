---
layout: single
title: ""
permalink: /
classes: about-justified
author_profile: true
---
## About

I am Soumadeep {% include speaker.html %} (pronounced _Show-mo-deep_), and I
completed my PhD in Computer Science at the Computer Vision and Pattern
Recognition Unit, [ISI Kolkata](https://www.isical.ac.in), under the supervision
of [Dr. Utpal Garain](https://www.isical.ac.in/~utpal/).

My doctoral research focused on integrating key symbolic AI principles&mdash;such
as domain constraint awareness and logical coherence&mdash;into deep
learning systems. Currently, I am exploring techniques to better understand and
enhance reasoning in Large Language Models (LLMs), with a focus on constraint
adherence, alignment, and reliability.

## Recent Works

{% assign published = site.data.publications | where: "status", "preprint" | sort: "year" | reverse %}
{% include pub_list.html pubs=published%}

