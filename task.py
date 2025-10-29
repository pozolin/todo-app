class Task():
    _id_counter = 1

    def __init__(self, title, priority="low"):
        self.title = title
        self.id = Task._id_counter
        Task._id_counter += 1
        self.status = "not_completed"
        self.priority = priority

    def toggle(self):
        if self.status == "not_completed":
            self.status = "completed"
        else:
            self.status = "not_completed"

    def __repr__(self):
        return f"<Task id={self.id} title='{self.title}' status={self.status}>"