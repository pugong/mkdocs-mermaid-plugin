# mkdocs-mermaid-plugin

A [MkDocs](https://www.mkdocs.org/) plugin that renders mermaid graphs.

## Installation

Install the package with pip:

```bash
pip install mkdocs-mermaid-plugin
```

## Usage

Enable this plugin in your `mkdocs.yml`:

```yaml
plugins:
    - search
    - markdownmermaid

extra_javascript:
    - https://unpkg.com/mermaid@7.1.2/dist/mermaid.min.js
```

> If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set.

> **Note:** Don't forget to include the mermaid.min.js (local or remotely) in your `mkdocs.yml`

More information about plugins in the [MkDocs documentation][http://www.mkdocs.org/user-guide/plugins/]
