## Installation

Right now, installation is pretty manual, but I'll be working on this.  The easiest way to install would be to make your own utilities directory

```bash
mkdir ~/util
cd ~/util
```

and clone the repo into it

```bash
git clone https://github.com/alexhagen/jdc
```

and then add that directory into your ``PYTHONPATH``

```bash
sudo echo "export PYTHONPATH=${PYTHONPATH}:~/util" >> ~/.bashrc
```

Then you can

```python
import jdc.jdc as jdc
```
in any Jupyter notebook.
