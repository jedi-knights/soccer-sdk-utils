from invoke import task

FILES_TO_REMOVE = [
    "*.png",
    ".coverage",
    "coverage.xml",
]

DIRECTORIES_TO_REMOVE = [
    "coverage",
    "dist",
    "htmlcov",
    "tests/htmlcov",
    "tests/.pytest_cache",
    "./.pytest_cache",
    "tests/coverage.xml",
]

@task(aliases=["i"])
def install(c):
    print("Installing dependencies...")
    c.run("pip install -e '.[dev]'")


@task(aliases=["u"])
def update_pip(c):
    print("Updating dependencies...")
    c.run("pip install --upgrade pip")


@task(aliases=["c"])
def clean(c):
    """
    Cleans up the project.

    :param c: Invoke context
    :return: None
    :raises: None
    """
    print("Cleaning up...")

    print(f"Removing files: {FILES_TO_REMOVE}")
    c.run(f"rm -f {' '.join(FILES_TO_REMOVE)}")

    print(f"Removing directories: {DIRECTORIES_TO_REMOVE}")
    c.run(f"rm -rf {' '.join(DIRECTORIES_TO_REMOVE)}")


@task(aliases=["t"])
def test(c):
    """Runs PyTest unit tests."""
    c.run("pytest tests")


@task(aliases=["v"])
def coverage(c):
    """Runs PyTest unit and integration tests with coverage."""
    c.run("coverage run -m pytest")
    c.run("coverage lcov -o ./coverage/lcov.info")


@task(aliases=["l"])
def lint(c):
    print("Linting...")
    c.run(
        "flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics"
    )
    c.run(
        "flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics"
    )


@task(aliases=["b"], pre=[clean, install, lint, coverage], default=True)
def build(c):
    print("Building the project")
    c.run("python3 -m pip install --upgrade build")
    c.run("python -m build")
