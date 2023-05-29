"""
Core utilities for handling Ryven projects and nodes packages, and
resolving paths. Deos not depend on any Qt modules.
"""

from os.path import normpath, join, dirname, abspath, expanduser
import pathlib
from typing import Union, Optional
from packaging.version import Version


def read_project(project_path: Union[str, pathlib.Path]) -> dict:
    """Read the project file and return its dictionary.

    :param project_path: The path to the project file.
    :return: The contents of the project file.
    """
    import io
    import json

    if isinstance(project_path, io.TextIOWrapper):
        project_dict = json.loads(project_path.read(), strict=False)
    else:
        with open(project_path) as f:
            import json
            # strict=False is needed to allow 'control characters' like '\n'
            # for newline when loading the json
            project_dict = json.load(f, strict=False)

    # backward compatibility: translate old project files to current version
    if Version(project_dict['ryven_version']) < Version('3.3.0'):
        print('WARNING: project was created with an older version of Ryven')
        print('INFO: attempting to translate project to current version...')
        pass  # TODO: implement project translation

    return project_dict


def find_project(project_path: Union[str, pathlib.Path]) -> Optional[pathlib.Path]:
    """Resolves a possibly *~/.ryven/saves/*-relative path to a nodes package to an absolute path.

    :param project_path: The path to the project file or the subpath to :code:`ryven_dir_path()/saves`.
        The file extension '.json' can be omitted.
    :return: The absolute and resolved path to the project file, or `None` if it could not be found.

    """
    project_path = pathlib.Path(project_path)

    if project_path.exists():
        return project_path.resolve()
    elif project_path.with_suffix('.json').exists():
        return project_path.with_suffix('.json').resolve()
    else:
        project_path = pathlib.Path(ryven_dir_path(), 'saves', project_path)
        if project_path.exists():
            return project_path.resolve()
        elif project_path.with_suffix('.json').exists():
            return project_path.with_suffix('.json').resolve()
        else:
            return None


def find_config_file(cfg_file_path: str) -> Optional[pathlib.Path]:
    """Resolves a possibly *~/.ryven/*-relative path of a config file to an absolute path.

    :param cfg_file_path: Either an absolute path, or relative to the *~/.ryven/* directory.
        The file extension '.cfg' can be omitted.
    :return: The full path to the config file or `None`, if it could not be found.
    """

    config_file_path = pathlib.Path(cfg_file_path)

    if config_file_path.exists():
        return config_file_path.resolve()
    else:
        config_file_path = pathlib.Path(ryven_dir_path(), cfg_file_path)
        if config_file_path.exists():
            return config_file_path.resolve()
        else:
            return None


def ryven_dir_path() -> str:
    """
    :return: absolute path the (OS-specific) '~/.ryven/' folder
    """
    return abspath(normpath(join(expanduser('~'), '.ryven/')))


def abs_path_from_package_dir(ryven_rel_path: str):
    """
    :param ryven_rel_path: path relative to ryven package folder (e.g. main/node_env.py)
    :return: absolute path
    """
    ryven_path = dirname(dirname(__file__))
    return abspath(join(ryven_path, ryven_rel_path))


def abs_path_from_ryven_dir(ryven_rel_path: str):
    """
    :param ryven_rel_path: path relative to '~/.ryven/' dir (e.g. saves)
    :return: absolute path
    """

    return abspath(join(ryven_dir_path(), ryven_rel_path))


def ryven_version() -> Version:
    """
    :return: the version of Ryven
    """

    # if we are in a development environment, we can't use importlib.metadata
    if (pathlib.Path(abs_path_from_package_dir('../setup.cfg'))).exists():
        # read the version from setup.cfg
        import configparser
        config = configparser.ConfigParser()
        config.read(abs_path_from_package_dir('../setup.cfg'))
        ver = Version(config['metadata']['version'])
        return ver
    else:
        # read the version from importlib.metadata
        from importlib.metadata import version
        return Version(version('ryven'))
