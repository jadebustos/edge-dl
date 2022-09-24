# Python virtual environments

Python virtual environments allow us to have installed different python environments using different python versions.

## Installing virtualenv

To install *virtualenv*:

```bash
jadebustos@reypastor:~$ python3.7 -m pip install --upgrade pip
Collecting pip
  Using cached pip-22.2.2-py3-none-any.whl (2.0 MB)
Installing collected packages: pip
Successfully installed pip-22.2.2
jadebustos@reypastor:~$ pip3 install virtualenv
Defaulting to user installation because normal site-packages is not writeable
Collecting virtualenv
  Downloading virtualenv-20.16.5-py3-none-any.whl (8.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.8/8.8 MB 11.8 MB/s eta 0:00:00
Collecting filelock<4,>=3.4.1
  Using cached filelock-3.8.0-py3-none-any.whl (10 kB)
Collecting importlib-metadata>=4.8.3
  Using cached importlib_metadata-4.12.0-py3-none-any.whl (21 kB)
Collecting distlib<1,>=0.3.5
  Downloading distlib-0.3.6-py2.py3-none-any.whl (468 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 468.5/468.5 kB 12.3 MB/s eta 0:00:00
Collecting platformdirs<3,>=2.4
  Using cached platformdirs-2.5.2-py3-none-any.whl (14 kB)
Collecting zipp>=0.5
  Using cached zipp-3.8.1-py3-none-any.whl (5.6 kB)
Collecting typing-extensions>=3.6.4
  Downloading typing_extensions-4.3.0-py3-none-any.whl (25 kB)
Installing collected packages: distlib, zipp, typing-extensions, platformdirs, filelock, importlib-metadata, virtualenv
Successfully installed distlib-0.3.6 filelock-3.8.0 importlib-metadata-4.12.0 platformdirs-2.5.2 typing-extensions-4.3.0 virtualenv-20.16.5 zipp-3.8.1
jadebustos@reypastor:~$ 
```

## Creating virtual environments using virtualenv

We can create virtual environments for the python versions installed:

```bash
jadebustos@reypastor:~$ ls -lh /usr/bin/python3*
lrwxrwxrwx 1 root root    9 jul  5 22:30 /usr/bin/python3 -> python3.8
-rwxr-xr-x 2 root root 4,9M abr 24 03:05 /usr/bin/python3.7
-rwxr-xr-x 2 root root 4,9M abr 24 03:05 /usr/bin/python3.7m
-rwxr-xr-x 1 root root 5,3M mar 15  2022 /usr/bin/python3.8
lrwxrwxrwx 1 root root   33 mar 15  2022 /usr/bin/python3.8-config -> x86_64-linux-gnu-python3.8-config
lrwxrwxrwx 1 root root   16 mar 13  2020 /usr/bin/python3-config -> python3.8-config
-rwxr-xr-x 1 root root  384 mar 28  2020 /usr/bin/python3-futurize
-rwxr-xr-x 1 root root  388 mar 28  2020 /usr/bin/python3-pasteurize
jadebustos@reypastor:~$ 
```
So, we can create python virtual environments for python 3.7 and 3.8. 

To create a virtual environment named **tensorflow** using python 3.7:

```bash
jadebustos@reypastor:~$ virtualenv -p /usr/bin/python3.7 tensorflow
created virtual environment CPython3.7.13.final.0-64 in 147ms
  creator CPython3Posix(dest=/home/jadebustos/tensorflow, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/jadebustos/.local/share/virtualenv)
    added seed packages: pip==22.1.2, setuptools==63.1.0, wheel==0.37.1
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
jadebustos@reypastor:~$ 
```

A directory named *tensorflow** will be created at the user's home directory.

## Using the virtual environment

To activate the virtual environment:

```bash
jadebustos@reypastor:~$ source tensorflow/bin/activate
(tensorflow) jadebustos@reypastor:~$ 
```

Now we will using the python virtual environment we have just installed. We will need to install python modules:

```bash
(tensorflow) jadebustos@reypastor:~$ pip install tensorflow-gpu==2.5.3
...
(tensorflow) jadebustos@reypastor:~$ 
```

Install all the modules you need and run any python script.