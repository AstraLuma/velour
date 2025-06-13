set windows-powershell := true

SPHINXOPTS := ""
SOURCEDIR  := "src"
BUILDDIR   := "build"


# Show this help
@help:
  just --list


# Show sphinx help
@sphinx-help:
  just build help


# Set up dev environments
install:
  python3 -m venv .venv
  .venv/bin/pip install --disable-pip-version-check -r requirements.txt sphinx-autobuild


# Reverse install
uninstall:
  rm -r .venv


# Run sphinx autobuild against the docs.
serve:
  .venv/bin/sphinx-autobuild --nitpicky --port 0 --open-browser "{{SOURCEDIR}}" "{{BUILDDIR}}/html"


# Do a sphinx build
build KIND="html":
  .venv/bin/sphinx-build -M {{KIND}} "{{SOURCEDIR}}" "{{BUILDDIR}}" {{SPHINXOPTS}}


# Run sphinx linkcheck
@linkcheck:
  just build linkcheck


# Clean up built files
@clean:
  just build clean


# Show the couch inventory
inv-couch:
  .venv/bin/python -m sphinx.ext.intersphinx https://docs.couchdb.org/en/stable/objects.inv