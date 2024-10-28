from django.apps import AppConfig


class EmpRprtConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "emp_rprt"
    
    def ready(self):
        import emp_rprt.signals