from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)
        name = data["tool"]["poetry"]["name"]
        description = data["tool"]["poetry"]["description"]
        license = data["tool"]["poetry"]["license"]
        authors = '\n'.join(f"- {author}" for author in data["tool"]["poetry"]["authors"])
        dependencies = '\n'.join(f"- {dep}" for dep in data["tool"]["poetry"]["dependencies"].keys())
        dev_dependencies = '\n'.join(f"- {dev_dep}" for dev_dep in data["tool"]["poetry"]["group"]["dev"]["dependencies"].keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return (f"Name: {name}\n"
                f"Description: {description}\n"
                f"License: {license}\n\n"
                f"Authors:\n{authors}\n\n"
                f"Dependencies:\n{dependencies}\n\n"
                f"Development dependencies:\n{dev_dependencies}")
