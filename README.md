# what_to_watch
Helping you pick something to watch


## Running

From Terminal
```python
python -m what_to_watch.suggestion_cli
```

## Setup

Setup virtualenv using pipenv

All Packages
```python
pipenv install --dev
```

Only Run packages
```
pipenv install
```

Remove a package
```
pipenv uninstall NAME
```


## Testing

Run tests like so

```python
python -m pytest test
```

## Linting

Linting as run by CI can be run locally as below, where $DIR is the directory to be linted


```python
pylint -d fixme $DIR
```
