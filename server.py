"""Server entry point.

Note:
    Using meinheld because bjoern doesn't have prebuilt manylinux wheels,
    but it would be wise to save a few processor cycles by migrating to bjoern
    once they add wheels: https://github.com/jonashaag/bjoern/issues/121.
"""
import pathlib
import tempfile
import meinheld
import pybossa.core


directory = pathlib.Path(__file__).parent
application = pybossa.core.create_app()


if __name__ == "__main__":
    # Create temporary writeable directories for the frontend assets, that
    # will be cached inside the source tree due to a design flaw in PyBossa.
    with tempfile.TemporaryDirectory(dir=directory / "cache") as cache:
        application.config["ASSETS_CACHE"] = cache

        # Start the application using Meinheld, when
        # in production, or Werkzeug for debugging.
        host = application.config["HOST"]
        port = application.config["PORT"]
        if application.config.get("DEBUG", False):
            app.run(app, host, port, debug=True)
        else:
            meinheld.server.listen((host, port))
            meinheld.server.run(application)
