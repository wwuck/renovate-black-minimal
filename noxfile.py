# Copyright 2021 Eskatos
"""noxfile.py."""
from __future__ import annotations

import nox


@nox.session
def gitlint(session: nox.Session) -> None:
    """
    Gitlint.

    :param session: nox session
    """
    args: list[str] = []

    if session.posargs:
        args.append(*session.posargs)

    deps = [
        'gitlint==0.16.0',
    ]

    session.install(*deps)
    session.run('gitlint', *args)


@nox.session
def yamllint(session: nox.Session) -> None:
    """
    yamllint.

    :param session: nox session
    """
    args = ['-f', 'parsable']

    if session.posargs:
        args.extend(session.posargs)

    session.install('yamllint==1.26.3')
    session.run('yamllint', *args)
