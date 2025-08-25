---
layout: single
title: ""
permalink: /
classes: about-justified
author_profile: true
---
I completed my PhD at the Computer Vision and Pattern Recognition Unit,
[ISI Kolkata](https://www.isical.ac.in), working under the supervision of
[Dr. Utpal Garain](https://www.isical.ac.in/~utpal/). My PhD work has focused on
trying to inculcate key features of symbolic AI techniques&mdash;such as domain
constraint awareness and logical coherence&mdash;into deep learning-based systems.

I am currently exploring techniques to better understand large language model
(LLM) reasoning and to promote constraint adherence in LLMs, with the goal of
improving their reasoning, alignment, and overall reliability.

> Dissertation: ["_Domain Obedient Deep Learning_"](/assets/pdf/dissertation.pdf).

## Recent Works

{% assign published = site.data.publications | where: "status", "preprint" | sort: "year" | reverse %}
{% include pub_list.html pubs=published%}

