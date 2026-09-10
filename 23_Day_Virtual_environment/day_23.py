# Exercises - Day 23

from pathlib import Path
import venv

# Create a project directory with a virtual environment based on the example given above
def create_virtual_environment(project_name='day_23_project'):
    project = Path(project_name)
    project.mkdir(exist_ok=True)
    venv.create(project / '.venv', with_pip=True)
    return project.resolve()

# print(create_virtual_environment())
