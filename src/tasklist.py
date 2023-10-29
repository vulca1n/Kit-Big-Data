from task import Task


class TaskList:
    def __init__(self):
        pass

    def add_task(
        self, name: str, due_date: str, description: str = "", completion: int = 0
    ):
        """
        Add a new task to the task list.

        :param name: The name of the task.
        :type name: str

        :param due_date: The due date of the task (in string format).
        :type due_date: str

        :param description: Additional description of the task (default is an empty string).
        :type description: str

        :param completion: The completion status of the task (default is 0).
        :type completion: int
        """
        Task(name, due_date, description, completion)

    def remove_task_by_name(self, name: str):
        """
        Remove a task by its name from the task list.

        :param name: The name of the task to remove.
        :type name: str
        """
        task_to_remove = Task.get_task_by_name(name)
        Task.remove(task_to_remove)

    def remove_task_by_id(self, id: int):
        """
        Remove a task by its unique identifier from the task list.

        :param id: The unique identifier of the task to remove.
        :type id: int
        """
        task_to_remove = Task.get_task_by_id(id)
        Task.remove(task_to_remove)

    def complete_task_by_name(self, name: str):
        """
        Mark a task as completed by its name.

        :param name: The name of the task to mark as completed.
        :type name: str
        """
        Task.get_task_by_name(name).set_completion(100)

    def complete_task_by_id(self, id: int):
        """
        Mark a task as completed by its unique identifier.

        :param id: The unique identifier of the task to mark as completed.
        :type id: int
        """
        Task.get_task_by_id(id).set_completion(100)

    def start_of_display(self):
        print()
        print("=====================")
        print("------- TASKS -------")
        print("=====================")
        print()

    def end_of_display(self):
        print("=====================")
        print("-------- END --------")
        print("=====================")

    def display_tasks(self):
        self.start_of_display()
        for task in Task.get_all_tasks():
            print(task, "\n")
        self.end_of_display()
