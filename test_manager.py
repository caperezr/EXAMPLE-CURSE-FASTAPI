import pytest
import sys
import os
import typer
from _pytest._io import TerminalWriter

app = typer.Typer()


@app.command()
def test(tests_type: str = "integration", token: str = ""):  # Literal["unit", "integration"]
    tw = TerminalWriter(sys.stderr)
    tw.sep("=", f"executing: {tests_type} tests", None, blue=True, bold=True)

    directories = {
        "integration": "src/tests/integration",
    }
    os.environ["TEMP_TOKEN"] = token

    directory = directories[tests_type]

    pytest.main(["-vv", "-s", "-x", "--color=yes", directory])
    # "-x" stops the test run on the first error or failure.
    # "-s" disables all capturing of stdout/stderr during test execution so that you can see print() output.
    # "-vv" increases verbosity.
    # "--color=yes" enables color output.
    # "--tb=short" shows less information on errors.
    # "--tb=long" shows more information on errors.
    # "--tb=line" shows only one line of output on errors.


if __name__ == "__main__":
    app()