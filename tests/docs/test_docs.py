from sphinx.application import Sphinx

source_dir = "."
config_dir = "."
output_dir = "./_build"
doctree_dir = "./_build/doctrees"
all_files = 1


def test_html_documentation():
    app = Sphinx(
        source_dir,
        config_dir,
        output_dir,
        doctree_dir,
        buildername="html",
        warningiserror=True,
    )
    app.build(force_all=all_files)
