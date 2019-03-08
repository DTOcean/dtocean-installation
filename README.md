[![appveyor](https://ci.appveyor.com/api/projects/status/github/DTOcean/dtocean-installation?branch=master&svg=true)](https://ci.appveyor.com/project/DTOcean/dtocean-installation)
[![codecov](https://codecov.io/gh/DTOcean/dtocean-installation/branch/master/graph/badge.svg)](https://codecov.io/gh/DTOcean/dtocean-installation)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bb34506cc82f4df883178a6e64619eaf)](https://www.codacy.com/project/H0R5E/dtocean-installation/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=DTOcean/dtocean-installation&amp;utm_campaign=Badge_Grade_Dashboard&amp;branchId=8410911)
[![release](https://img.shields.io/github/release/DTOcean/dtocean-installation.svg)](https://github.com/DTOcean/dtocean-installation/releases/latest)

# DTOcean Installation Module

The DTOcean Installation Modules calculates the scheduling of installation of 
the designs created by the [dtocean-electrical]( 
https://github.com/DTOcean/dtocean-electrical) and [dtocean-moorings]( 
https://github.com/DTOcean/dtocean-moorings) modules and the OECs themselves. 
It produces a detailed time-based installation plan and associated costs. 
Installation is optimised for minimum cost. 

See [dtocean-app](https://github.com/DTOcean/dtocean-app) or [dtocean-core](
https://github.com/DTOcean/dtocean-app) to use this package within the DTOcean
ecosystem.

* For python 2.7 only.

## Installation

Installation and development of dtocean-installation uses the [Anaconda 
Distribution](https://www.anaconda.com/distribution/) (Python 2.7)

### Conda Package

To install:

```
$ conda install -c defaults -c conda-forge -c dataonlygreater dtocean-installation
```

### Source Code

Conda can be used to install dependencies into a dedicated environment from
the source code root directory:

```
conda create -n _dtocean_install python=2.7 pip
```

Activate the environment, then copy the `.condrc` file to store installation  
channels:

```
$ conda activate _dtocean_install
$ copy .condarc %CONDA_PREFIX%
```

Install [polite](https://github.com/DTOcean/polite) and [dtocean-logistics](
https://github.com/DTOcean/dtocean-logistics) into the environment. For 
example, if installing them from source:

```
$ cd \\path\\to\\polite
$ conda install --file requirements-conda-dev.txt
$ pip install -e .
```

```
$ cd \\path\\to\\dtocean-logistics
$ conda install --file requirements-conda-dev.txt
$ pip install -e .
```

Finally, install dtocean-installation and its dependencies using conda and pip:

```
$ cd \\path\\to\\dtocean-installation
$ conda install --file requirements-conda-dev.txt
$ pip install -e .
```

To deactivate the conda environment:

```
$ conda deactivate
```

### Tests

A test suite is provided with the source code that uses [pytest](
https://docs.pytest.org).

If not already active, activate the conda environment set up in the [Source 
Code](#source-code) section:

```
$ conda activate _dtocean_install
```

Install packages required for testing to the environment (one time only):

```
$ conda install -y pytest
```

Run the tests:

``` 
$ py.test tests
```

### Uninstall

To uninstall the conda package:

```
$ conda remove dtocean-installation
```

To uninstall the source code and its conda environment:

```
$ conda remove --name _dtocean_install --all
```

## Usage

Example scripts are available in the "examples" folder of the source code.

```
cd examples
python example.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to
discuss what you would like to change.

See [this blog post](
https://www.dataonlygreater.com/latest/professional/2017/03/09/dtocean-development-change-management/)
for information regarding development of the DTOcean ecosystem.

Please make sure to update tests as appropriate.

## Credits

This package was initially created as part of the [EU DTOcean project](
https://www.dtoceanplus.eu/About-DTOceanPlus/History) by:

 * Boris Teillant at [WavEC](https://www.wavec.org/)
 * Paulo Chainho at [WavEC](https://www.wavec.org/)
 * Pedro Vicente at [WavEC](https://www.wavec.org/)
 * Adam Collin at [the University of Edinburgh](https://www.ed.ac.uk/)
 * Mathew Topper at [TECNALIA](https://www.tecnalia.com)

It is now maintained by Mathew Topper at [Data Only Greater](
https://www.dataonlygreater.com/).

## License

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
