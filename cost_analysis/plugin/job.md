---
description:  
---
# Job

>  **Package : spaceone.api.cost_analysis.plugin**

## Job

{% hint style="info" %}
**Job Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**get_tasks**](job.md#get_tasks)|   [GetTasksRequest](job.md#gettasksrequest) |   [TasksInfo](job.md#tasksinfo) | 
 

 
### get_tasks


| Type | Message |
| :--- | :--- |
| Request | [GetTasksRequest](job.md#gettasksrequest) |
| Response |  [TasksInfo](job.md#tasksinfo)  |


## 

## Message

### ChangedInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| start |string | |
| end |string | |

### GetTasksRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| schema |string|❌| |
| start |string|❌| |
| last_synchronized_at |string|❌| |

### TaskInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| task_options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### TasksInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| tasks |[list of TaskInfo](job.md#taskinfo) | |
| changed |[list of ChangedInfo](job.md#changedinfo) | |
