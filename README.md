# SlashFramework
Official Website https://slash.readthedocs.io/en/master/

Basic tests script for slash framework written in python and running on Windows OS.
You can use Git Bash or command prompt(cmd) on Windows to run the tests.

### Activate virtualenv
```
$ source myenv/Scripts/activate  # Git Bash
> myenv\Scripts\activate.bat     # cmd
```

### Install requirments
```
pip install -r requirements.txt
```

### How to run any test?
```
slash run path/to/file/filename.py
```
Output for pass and fail scenario

![pass-fail](https://user-images.githubusercontent.com/22471567/216791577-c01b091b-b628-403a-8645-ca9d97225998.jpg)

### How to list available Fixtures or Testcases?
```
slash list tests
```
![list](https://user-images.githubusercontent.com/22471567/216791603-00dcadcf-43ec-4262-b8a8-8fd4f24f9c05.jpg)
