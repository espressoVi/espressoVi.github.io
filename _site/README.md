# Personal Website

Personal website for Soumadeep Saha.


## Usage

> [!WARNING]
> Always use links that start with ```/```, e.g., ```/assets/pdf/xyz.pdf```.

* To update **publications**:
    - Add entry in ```_data/publications.yml```.
    - Choose ```status=[preprint, published, hidden, patent]```
    - Preprints (marked with ```preprint```) appear on the front page.
    - Set ```priority=``` to change order of appearance.
> [!WARNING]
> The HTML is generated from ```_includes/pub_list.html```. Modify **if** needed.

* To update **updates**:
    - Add entry in ```_data/updates.yml```.
    - Add ISO-date ```yyyy-mm-dd```, title and text.
> [!WARNING]
> The HTML is generated from ```_includes/updates_list.html```. Modify **if** needed.

* To update **about**:
    - Edit file ```index.md```.
    - Written in markdown, so nothing else to do.

* To update **experience/education**:
    - Edit file ```_pages/experience.md```, , or ```_pages/education.md```.
    - Written in markdown, so nothing else to do.

* Put relevant PDFs in ```/assets/pdf/```
