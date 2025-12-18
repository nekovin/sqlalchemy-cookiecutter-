import os
import shutil

use_alembic = "{{ cookiecutter.use_alembic }}" == "yes"
include_example_model = "{{ cookiecutter.include_example_model }}" == "yes"

if not use_alembic:
    shutil.rmtree("alembic", ignore_errors=True)
    if os.path.exists("alembic.ini"):
        os.remove("alembic.ini")

if not include_example_model:
    user_model = os.path.join("src", "{{ cookiecutter.project_slug }}", "models", "user.py")
    if os.path.exists(user_model):
        os.remove(user_model)
