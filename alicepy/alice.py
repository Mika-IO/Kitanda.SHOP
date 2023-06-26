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
    def __init__(
        self,
    ):
        self.components = []
        self.html_content = self.render()

    def add(self, component):
        self.components.append(component)

    def render(self):
        html = ""
        for component in self.components:
            html += str(component) + "\n"
        return html

    def build(self, file_path, debug=None):
        html_content = self.render()
        with open(file_path, "w") as file:
            file.write(html_content)
        print(f"File {file_path} created successfully!")


"""
class Component:
    def __init__(self, html_content: str, states={}, style=None):
        self.html_content = html_content
        self.container = f"<div>{self.html}</div>"
        self.states = states
        self.style = style

        self.render()

    def render(self):
        return self.container

    def set_state(self, key, value):
        self.states[key] = value
        element = self.container.querySelector(f"#{key}")
        element.textContent = f"{self.states[key]}"

    def reactive(self, element_id, event="click"):
        def decorator(func):
            def wrapper(self, event):
                return func(self, event)

            element = self.container.querySelector(f"#{element_id}")
            element.addEventListener(event, wrapper)
            return wrapper

        return decorator


def convert_camel_to_snake(name: str) -> str:
    snake_case = ""
    for char in name:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    if snake_case.startswith("_"):
        snake_case = snake_case[1:]
    return snake_case


def html(html: str) -> str:
    tags = html.split("\n")
    tags = [tag.strip() for tag in tags]
    for i in range(len(tags)):
        if tags[i].startswith("<") and tags[i].endswith("/>"):
            component = tags[i][1:-3].strip()
            if component[0].isupper():
                component_name = convert_camel_to_snake(component)
                try:
                    tags[i] = exec(
                        f"from components.{component_name} import {component_name}\n{component_name}()"
                    )
                except ImportError:
                    raise ImportError(f"Component '{component_name}' is not defined.")
    result = f"\n".join(tags).strip()
    return result

"""
