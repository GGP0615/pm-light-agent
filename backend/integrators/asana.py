import asana
import os

class AsanaIntegrator:
    def __init__(self):
        self.client = asana.Client.access_token(os.environ["ASANA_ACCESS_TOKEN"])

    def list_tasks(self, project_gid, opt_fields=None):
        return self.client.tasks.find_by_project(project_gid, opt_fields=opt_fields or [])

    def update_task(self, task_gid, fields):
        return self.client.tasks.update(task_gid, fields)
