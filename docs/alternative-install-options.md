# Alternative install options for using `cffconvert`

## Install in virtual environment

``` {.sourceCode .bash}
virtualenv -p /usr/bin/python3.5 myvenv3
source myvenv3/bin/activate
pip3 install cffconvert
```

## Install globally

Note: this option needs sudo rights.

``` {.sourceCode .bash}
sudo -H pip3 install cffconvert
```

## Install with conda

See
<https://stackoverflow.com/questions/41060382/using-pip-to-install-packages-to-anaconda-environment>

``` {.sourceCode .bash}
conda install pip
pip install cffconvert
```

**Option 6 (not preferred): install with setup.py in the user
environment**

``` {.sourceCode .bash}
python setup.py install --user
```

## No-install option: use `cffconvert` as a Google Cloud Function

`cffconvert` comes with [an interface](/cffconvert/gcloud.py) for
running as a Google Cloud Function. We set it up here
<https://bit.ly/cffconvert> for the time being / as long as we have
enough credits on the Google Cloud Function platform.

Really, all the Google Cloud interface does is get any supplied URL
parameters, and use them as if they had been entered as command line
arguments. For more detailed explanation and examples, see
<https://bit.ly/cffconvert>.

On Google Cloud Function, set `requirements.txt` to:

``` {.sourceCode .}
Flask
cffconvert
```

and use the following as `main.py`:

``` {.sourceCode .python}
from cffconvert.gcloud import cffconvert

def main(request):
   return cffconvert(request)
```
