# autogrem

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
### Install Python
Check out Python's [Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide/Download) for instructions on downloading python for your particular system.

### Create virtual environment
Once you've cloned the repository, navigate to it in a terminal or PowerShell window:
```bash
# navigate to the cloned repository
cd /path/to/autogrem

# Unix/macOS
python3 -m venv "venv"

# Windows
py -m venv venv
```

### Activate your virtual environment
```bash
# Unix/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

To confirm the virtual environment is activated, check the location of your Python interpreter:

```bash
# Unix/macOS
which python

# Windows
where python
```
While the virtual environment is active, the above command will output a filepath that includes the `venv` directory and ends with something like the following:

```bash
# Unix/macOS
venv/bin/python

# Windows
venv\Scripts\python
```

For example, on my system (Debian), I see:
```
/home/emmett/git-projects/autogrem/venv/bin/python
```

While a virtual environment is activated, pip will install packages into that specific environment. This enables you to import and use packages in your Python application.

### Deactivate your virtual environment
At any time you can deactivate your virtual environment with the `deactivate` command. This command is the same on Unix/macOS and Windows.

### Install required packages
```bash
# navigate to the cloned repository
cd /path/to/autogrem

# ensure your virtual environment is activated
# Unix/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

# Install dependencies (to your virtual environment)
# on Unix/macOS
python3 -m pip install -r requirements.txt

# on Windows
py -m pip install -r requirements.txt
```

## Usage
Make sure your prerequisites are satisfied:
- [ ] [Install python](#install-python)
- [ ] [Create and activate your virtual environment](#create-virtual-environment)
- [ ] [Install required packages](#install-required-packages)

### Running the app locally
Open a new terminal and navigate to the django project directory:
```bash
cd /path/to/autogrem/autogrem
```

> **Example usage:**
> ```
> cd /home/emmett/git-projects/autogrem/autogrem
> ```

You'll notice that the directory structure seems a bit redundant. Below is a summary of the important parts of the basic structure:
```plaintext
autogrem/                   <-- top level directory
 |-- autogrem/              <-- django project directory
 |    |-- autogrem/         <-- autogrem app directory
 |    |    |-- __init__.py
 |    |    |-- settings.py  <-- settings for entire project
 |    |    +-- urls.py      <-- project URL routing
 |    |-- finance/          <-- one of many possible "apps" within the project 
 |    +-- manage.py         <-- script to run development server, tests, and more
 +-- venv/                  <-- virtual environment (can be deleted and recreated anytime)
```

In this document and within the entire project, we will always refer to these main
directories in the following way to avoid confusion:
```plaintext
autogrem/                   <-- top level directory
 |-- autogrem/              <-- django project directory
 |    |-- autogrem/         <-- autogrem app directory
 |    |-- foo/              <-- "foo" app directory
 |    |-- bar/              <-- "bar" app directory
 |    |-- ...
 +-- venv/                  <-- virtual environment
```

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
