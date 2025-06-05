import shutil
import os
import random

os.chdir("/home/mateuszs/Project/VSC_Project/python_code/organization_of_files")
if os.path.isdir("examples") is False:
    os.mkdir("examples")
shutil.copy("example2.txt", os.path.join(os.getcwd(), "examples"))
shutil.copy("example.txt", os.path.join(os.getcwd(), "examples/example3.txt"))
try:
    shutil.copytree(
        os.path.join(os.getcwd(), "examples"),
        os.path.join("new_direction/" + str(random.randint(0, 100))),
    )
except FileExistsError or FileNotFoundError as e:
    print(e)
try:
    shutil.move(
        os.path.join(
            os.getcwd(),
            "new_direction",
            os.listdir(os.path.join(os.getcwd(), "examples"))[0],
        ),
        os.path.join(os.getcwd(), "new_direction"),
    )
except FileExistsError or FileNotFoundError as e:
    print(e)
