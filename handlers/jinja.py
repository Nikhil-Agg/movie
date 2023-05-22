from jinja2 import Environment, FileSystemLoader


class JinjaManager:

    jinja_environment = None

    @staticmethod
    def _get_jinja_environment():
        """Function to set jinja environment"""
        file_loader = FileSystemLoader("templates")
        env = Environment(loader=file_loader)
        return env
    
    @classmethod
    def set_jinja_environment(cls):
        if cls.jinja_environment is None:
            cls.jinja_environment = cls._get_jinja_environment()

    @classmethod
    def render_text(cls, template, data):
        template = cls.jinja_environment.get_template(template)
        return template.render(data)
