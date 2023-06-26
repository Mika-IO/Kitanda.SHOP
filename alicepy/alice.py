class Component:
    def __init__(self, html_string):
        self.html_string = html_string
        self.components = []

    def add(self, component):
        self.components.append(component)

    def render(self):
        html = self.html_string
        for component in self.components:
            html += component.render()
        return html

    def __str__(self):
        return self.render()


class Alice:
    def register(self, url):
        return url

    def build(self, html_content, file_path):
        with open(file_path, "w") as file:
            file.write(str(html_content))
        print(f"File {file_path} created successfully!")

    def run(self, debug=False):
        """Criar as rotas e renderiza as paginas

        Args:
            debug (bool, optional): Logger debug. Defaults to False.
        """
        for url in self.urls:
            url_path = url[0]
            html_content = url[1]
            file_path = url[2]

            self.register(url_path)
            self.build(html_content, file_path)
