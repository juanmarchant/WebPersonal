from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name = 'Imagen', upload_to="projects")

    language_choice = (
        ('.django','.django'),
        ('.py','.py'),
        ('.js','.js'),
        ('.html','.html'),
        ('.css','.css'),
    )
    language = MultiSelectField(choices = language_choice, verbose_name="Lenguajes")

    program_choice = (
        ('.vscode','.vscode'),
        ('.figma','.figma')
    )
    program = MultiSelectField(choices = program_choice, verbose_name = 'Programas')
    url_link =  models.URLField(null=True, blank=True, verbose_name="Dirección Web")
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de actualización')

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.title

