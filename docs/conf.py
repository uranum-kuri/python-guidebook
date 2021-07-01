import sphinx_rtd_theme

project = "Python GuideBook"
copyright = "2021, uranum"
author = "uranum"

extensions = ["recommonmark", "sphinx_markdown_tables"]

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

source_suffix = [".rst", ".md"]
source_parsers = {
    ".md": "recommonmark.parser.CommonMarkParser",
}
