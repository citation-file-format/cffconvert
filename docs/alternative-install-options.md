# Alternative install options for using `cffconvert`

## Install in virtual environment

```shell
# use venv to make a virtual environment named env
python3 -m venv env

# activate the environment
source env/bin/activate

# install cffconvert in it
pip install cffconvert
```

## Install globally

Note: this option needs sudo rights.

```shell
sudo -H python3 -m pip install cffconvert
```

## Install with conda

Make an environment definition file `environment.yml` with the following contents:

```yaml
name: env
channels:
  - conda-forge
  - defaults
dependencies:
  - pip
  - pip:
    - cffconvert
```

Then run:

```shell
conda env create --file environment.yml
conda activate env
```

## No-install options

### Using `cffconvert` as a Google Cloud Function

`cffconvert` comes with [an interface](/cffconvert/gcloud.py) for
running as a Google Cloud Function. We set it up here
<https://bit.ly/cffconvert> for the time being / as long as we have
enough credits on the Google Cloud Function platform.

Really, all the Google Cloud interface does is get any supplied URL
parameters, and use them as if they had been entered as command line
arguments. For more detailed explanation and examples, see
<https://bit.ly/cffconvert>.

On Google Cloud Function, set `requirements.txt` to:

```text
Flask
cffconvert
```

and use the following as `main.py`:

```python
from cffconvert.gcloud import cffconvert

def main(request):
   return cffconvert(request)
```

### Docker

Build the Docker container 

```shell
cd <project root>
docker build --tag cffconvert:2.0.0-alpha.0 .
docker build --tag cffconvert:latest .
```

Build the Docker container 

```shell
cd <where your CITATION.cff is>
docker run --rm -ti -v ${PWD}:/app cffconvert
```

