# Soccer SDK Utils

This package contains general purpose utilities to be utilized in various other Soccer related SDK products.


# Setup
- Create your virtual environment of choice
- Install Poetry globally

Install dependencies

```bash
$ pip install --upgrade pip 
$ pip install -r requirements-dev.txt
$ invoke install
```

Update dependencies

```bash
$ invoke update
```


Clean up transient files

```bash
$ invoke clean
```

Analyze syntax

```bash
$ invoke lint
```

Run tests

```bash
$ invoke test
```

Generate Coverage Report

```bash
$ invoke cover
```

Build the project

```bash
$ invoke build
```

The default task is build so by calling invoke you will build the project

```bash
$ invoke
```