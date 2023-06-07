import json
from enum import Enum
from todocli.utils.datetime_util import api_timestamp_to_datetime
import hashlib
import base64


class TaskStatus(str, Enum):
    COMPLETED = "completed"
    NOT_STARTED = "notStarted"
    IN_PROGRESS = "inProgress"
    WAITING_ON_OTHERS = "waitingOnOthers"
    DEFERRED = "deferred"


class TaskImportance(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"


class Task:
    def __init__(self, query_result):
        self.title = query_result["title"]
        self.id = query_result["id"]
        self.short_id = self.shorten_uid(self.id, 5)
        self.importance = TaskImportance(query_result["importance"])
        self.status = TaskStatus(query_result["status"])
        self.created_datetime = api_timestamp_to_datetime(
            query_result["createdDateTime"]
        )

        if "completedDateTime" in query_result:
            self.completed_datetime = api_timestamp_to_datetime(
                query_result["completedDateTime"]
            )
        else:
            self.completed_datetime = None

        self.is_reminder_on: bool = bool(query_result["isReminderOn"])

        if "reminderDateTime" in query_result:
            self.reminder_datetime = api_timestamp_to_datetime(
                query_result["reminderDateTime"]
            )
        else:
            self.reminder_datetime = None

        self.last_modified_datetime = api_timestamp_to_datetime(
            query_result["lastModifiedDateTime"]
        )

        if "dueDateTime" in query_result:
            self.due_date_datetime = api_timestamp_to_datetime(
                query_result["dueDateTime"]
            )
        else:
            self.due_date_datetime = None

        if "bodyLastModifiedDateTime" in query_result:
            self.body_last_modified_datetime = api_timestamp_to_datetime(
                query_result["bodyLastModifiedDateTime"]
            )
        else:
            self.body_last_modified_datetime = None

    def shorten_uid(self, uid, length):
        # Hash the UID using SHA-256
        hash_object = hashlib.sha256(uid.encode())
        hash_value = hash_object.digest()

        # Convert the first bytes of the hash value to a string
        bytes_to_encode = hash_value[:length*2]
        encoded_bytes = base64.b64encode(bytes_to_encode)
        encoded_string = encoded_bytes.decode()[:length]

        return encoded_string

class TaskJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        return {
            "title": obj.title,
            "id": obj.id,
            "sid": obj.short_id,
            "status": obj.status,
            "created_at": obj.created_datetime,
            "completed_at": obj.completed_datetime,
            "reminder_at": obj.reminder_datetime,
            "due_at": obj.due_date_datetime
        }
