from project.task import Task

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def find_object(self,task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                return task

    def complete_task(self, task_name: str) -> str:
        task = self.find_object(task_name)

        if not task:
            return f"Could not find task with the name {task_name}"

        task.completed = True
        return f"Completed task {task.name}"

    def clean_section(self):

        number_of_tasks = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]

        deleted_task = number_of_tasks - len(self.tasks) if number_of_tasks != len(self.tasks) else 0
        return f"Cleared {deleted_task} tasks."

    def view_section(self):
        output = [f"Section {self.name}:"]
        for task in self.tasks:
            output.append(task.details())

        return "\n".join(output)









