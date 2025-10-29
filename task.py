class Task():
    _id_counter = 1
    PRIORITY_LEVELS = ['low', 'medium', 'high']

    def __init__(self, title, priority="low"):
        self.title = title
        self.id = Task._id_counter
        Task._id_counter += 1
        self.status = "not_completed"
        self.set_priority(priority)

    def toggle(self):
        if self.status == "not_completed":
            self.status = "completed"
        else:
            self.status = "not_completed"

    def set_priority(self, priority):
        if priority in self.PRIORITY_LEVELS:
            self.priority = priority

    def __repr__(self):
        return f"<Task id={self.id} title='{self.title}' status={self.status}>"