---
layout: single
title: "Publications"
permalink: /publications/
author_profile: true
---

{% assign published = site.data.publications | where: "status", "published" | sort: "year" | reverse %}
{% include pub_list.html pubs=published%}

## Patents
{% assign published = site.data.publications | where: "status", "patent" %}
{% include pub_list.html pubs=published%}
