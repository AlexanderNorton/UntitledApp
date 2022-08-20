# UntitledApp

A web app made using Django - create a profile and fill it with anything you want.

# Getting started
- Install Python:
- Install Git Bash: https://git-scm.com/download/win
- Open Git Bash in the project's base directory (Right click - 'git bash here').
- Use Visual Studio Code terminals for the same.
- Create a virtual environment:
`python -m venv env`
- Activate the environment:
`source env/Scripts/activate`
- Ensure pip is up to date:
`python -m pip install --upgrade pip`
- Install the dependencies:
`pip install -r requirements.txt`
- Migrate all database models:
`python manage.py migrate`
- Start up the webserver:
`python manage.py runserver`

# Contributing with Git
- Have a new idea? Create an 'issue': https://github.com/AlexanderNorton/UntitledApp/issues
- To clone the repo, use `git clone https://github.com/AlexanderNorton/UntitledApp.git`.
- Use `git status` to check what's been changed or ready to be comitted.
- Create a new branch with a name related to the issue you created: `git checkout -b front_page`.
- Make the required changes to complete the issue. For example, complete the front page code.
- Use `git add .` to mark all changed files as ready to commit.
- Use `git commit -m "some message"` to create a commit with the changed files. Include a useful message so everyone knows what the change was.
- Use `git push` to push the changes to the Github server. The changes will now be in the `front_page` branch.
- Merge with master by making a pull request. Someone will review the change and approve it for merging.
