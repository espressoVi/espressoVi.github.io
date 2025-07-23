import os
import re
import toml
import markdown

config = toml.load("config.toml")


class HTMLGenerator:
    def __init__(self, content):
        self.content = content

    def generate_page(self):
        header_file = os.path.join(
                config['html']['root'],
                config['html']['header']
        )
        Page = self._get_file(header_file)
        while match := re.search(r"(\{% include.+%\})", Page):
            find_filename = re.search(r'"([^"]+)"', str(match))
            if find_filename: filename = find_filename.group(1)
            else: continue
            if filename == "CONTENT":
                page = self._get_content(self.content)
            else:
                page = self._get_file(
                    os.path.join(config['html']['root'], filename)
                )
            Page = (Page[:match.start()].rstrip() 
                         + f"\n{page}" 
                         + Page[match.end():].lstrip()
            )
        return Page

    def _get_file(self, filename):
        with open(filename, "r") as f:
            page = f.read()
        return page

    def _get_content(self, content):
        content_file = os.path.join(config["pages"]["content"], f"{content}.md")
        with open(content_file, "r") as f:
            page = f.read()
        return markdown.markdown(page)

    def get(self):
        return self.generate_page()

def main():
    page = HTMLGenerator("head.html")
    page._generate_page()

if __name__ == "__main__":
    main()
