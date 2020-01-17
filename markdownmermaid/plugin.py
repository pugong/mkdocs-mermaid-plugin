from mkdocs.plugins import BasePlugin
from bs4 import BeautifulSoup

try:
    unicode
except NameError:
    # Python 3 doesn't have `unicode` as `str`s are all Unicode.
    unicode = str


class MarkdownMermaidPlugin(BasePlugin):
    def on_post_page(self, output_content, config, **kwargs):
        soup = BeautifulSoup(output_content, 'html.parser')
        mermaids = soup.find_all("code", class_="language-mermaid")
        for mermaid in mermaids:
            # replace code with div
            mermaid.name = "div"
            mermaid['class'] = "mermaid"
            # replace <pre>
            mermaid.parent.replace_with(mermaid)

        if mermaids:
            new_tag = soup.new_tag("script")
            new_tag.string = "mermaid.initialize();"
            soup.body.append(new_tag)

        return unicode(soup)
