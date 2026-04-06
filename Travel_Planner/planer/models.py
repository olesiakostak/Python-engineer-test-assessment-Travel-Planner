from django.db import models


class TravelProject(models.Model):
    name = models.CharField(max_length=256)
    start_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Travel project '{self.name}'"


class Place(models.Model):
    external_id = models.CharField(max_length=256)
    project = models.ForeignKey(TravelProject, on_delete=models.CASCADE, related_name='places')
    visited = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('external_id', 'project')

    def __str__(self):
        return f"Place id: {self.external_id}. Project: {self.project.name}'"
    