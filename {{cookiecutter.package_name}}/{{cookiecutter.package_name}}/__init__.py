
import json
import os.path as osp

from ._version import __version__

HERE = osp.abspath(osp.dirname(__file__))

with open(osp.join(HERE, 'static', 'package.orig.json')) as fid:
    data = json.load(fid)

def _jupyter_labextension_paths():
    return [{
        'src': 'static',
        'dest': data['name']
    }]


{% if cookiecutter.has_server_extension.lower().startswith('y') %}
from .handlers import setup_handlers


def _jupyter_server_extension_paths():
    return [{
        "module": "{{ cookiecutter.python_name }}"
    }]


def load_jupyter_server_extension(lab_app):
    """Registers the API handler to receive HTTP requests from the frontend extension.

    Parameters
    ----------
    lab_app: jupyterlab.labapp.LabApp
        JupyterLab application instance
    """
    setup_handlers(lab_app.web_app)
    lab_app.log.info("Registered HelloWorld extension at URL path /{{ cookiecutter.python_name }}")
{% endif %}
