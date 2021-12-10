---
description:  
---
# Job

>  **Package : spaceone.api.cost_analysis.plugin**

## Job

{% hint style="info" %}
**Job Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**get_tasks**](job.md#get_tasks)|   [GetTasksRequest](job.md#gettasksrequest) |   [TasksInfo](job.md#tasksinfo) |  | 
 

 
### get_tasks


| Type | Message |
| :--- | :--- |
| Request | [GetTasksRequest](job.md#gettasksrequest) |
| Response |  [TasksInfo](job.md#tasksinfo)  |


## 

## Message

### GetTasksRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 2 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 3 | schema |string|❌| |
| 4 | start |string|❌| |
| 5 | end |string|❌| |
| 6 | last_synchronized_at |string|❌| |

### TaskInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | task_options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### TasksInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of TaskInfo](job.md#taskinfo) | |
