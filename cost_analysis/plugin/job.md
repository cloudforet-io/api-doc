---
description:  
---
# Job

>  **Package : spaceone.api.cost_analysis.plugin**

## Job

{% hint style="info" %}
**Job Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**get_tasks**](job.md#get_tasks)|   [GetTasksRequest](job.md#gettasksrequest) |   [TasksInfo](job.md#tasksinfo) |  |TEST

<table style="border-collapse: collapse; text-align: left; line-height: 1.5;">
    <thead>
    <tr>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Method</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Request</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Response</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">get_tasks</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   GetTasksRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   TasksInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
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
