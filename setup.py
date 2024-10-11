[metadata]
name = pre_commit_hooks
version = 1.0.0
description = Pre-commits library for custom projects
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/Guudox/pre-commit
author = Michael Kiernan
author_email = dev@mkiernan.com
license = MIT
license_files = LICENSE
classifiers =
    License :: OSI Approved :: MIT License
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: Implementation :: CPython
    Programming Language :: Python :: Implementation :: PyPy

[options]
packages = find:
install_requires =
    ruamel.yaml>=0.15
    tomli>=1.1.0;python_version<"3.12"
python_requires = >=3.12

[options.packages.find]
exclude =

[options.entry_points]
console_scripts =
    check_private_guild_sync = pre_commit_hooks.check_private_guild_sync:main

[bdist_wheel]
universal = True

[coverage:run]
plugins = covdefaults

[mypy]
check_untyped_defs = true
disallow_any_generics = true
disallow_incomplete_defs = true
disallow_untyped_defs = true
warn_redundant_casts = true
warn_unused_ignores = true

[mypy-testing.*]
disallow_untyped_defs = false

[mypy-tests.*]
disallow_untyped_defs = false
