---
layout: single
title: ""
permalink: /
classes: about-justified
author_profile: true
---
I am a PhD candidate at the Computer Vision and Pattern Recognition Unit,
[ISI Kolkata](https://www.isical.ac.in), working under the supervision of
[Dr. Utpal Garain](https://www.isical.ac.in/~utpal/).

My PhD work has focused on trying to inculcate key features of symbolic AI
techniques&mdash;such as domain constraint awareness and logical
coherence&mdash;into deep learning-based systems. My dissertation titled
["_Domain Obedient Deep Learning_"](https://github.com/espressoVi/Dissertation/blob/5e8e0f1cf19be1c23e4e660e6882724728b70da4/thesis.pdf)
has been **accepted**.

I am currently exploring techniques to better understand large language model
(LLM) reasoning and to promote constraint adherence in LLMs, with the goal of
improving their reasoning, alignment, and overall reliability.

## Recent Works

{% assign published = site.data.publications | where: "status", "preprint" | sort: "year" | reverse %}
{% include pub_list.html pubs=published%}

