# Terminal Translator 
[![Documentation Status](https://readthedocs.org/projects/terminal-translator/badge/?version=latest)](https://terminal-translator.readthedocs.io/en/latest/?badge=latest)

Terminal Translator is a translation CLI that uses the [Google Cloud API](https://cloud.google.com/translate).

## Documentation

See the [full documentation](https://terminal-translator.readthedocs.io/en/latest/)

## Installation

Installation is very simple, just run the following command in the terminal:

```bash
pip install tt-terminal-translator
```

## Basic Usage

The CLI consists of two commands, `tt` and `tt-configure`.

### tt

`tt` is the main CLI command.

**Usage**

Basically we call the command passing the text to be translated

By default the text will be translated to `en-us`

```bash
tt ola mundo
```
![tt](./docs/assets/images/tt.png)

We can also inform the target language for the translation

```bash
tt ola mundo --target es  # spanish
```
![tt-2](./docs/assets/images/tt-2.png)

There is also a parameter to translate directly into Portuguese

```bash
tt hello world -p
```
![tt-3](./docs/assets/images/tt-3.png)


In addition there is a parameter to copy the output directly to the clipboard

```bash
tt -c hola mundo
```
![tt-4](./docs/assets/images/tt-4.png)

For more information use the parameter `--help`

```bash
tt --help
```

![tt-5](./docs/assets/images/tt-5.png)



### tt-configure

`tt-configure` is only for the initial configuration of the Google Cloud API credentials, as seen in the [settings section](/#configuration).

**Usage**

Basically we call the command passing two arguments, first the project-id followed by the path of the credentials Json file.

```bash
tt-configure <project-id> <google-api-credentials>
```

For quick help use the `--help` argument.


```bash
tt-configure --help
```
![tt-configure](./docs/assets/images/tt-configure.png)

