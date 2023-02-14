---
description: A JobTask is a unit for collecting external cloud resources. The resource belongs to a specific service account.
---
# Job task

>  **Package : spaceone.api.inventory.v1**

## JobTask

{% hint style="info" %}
**JobTask Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**delete**](job-task.md#delete)|   [JobTaskRequest](job-task.md#jobtaskrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](job-task.md#get)|   [GetJobTaskRequest](job-task.md#getjobtaskrequest) |   [JobTaskInfo](job-task.md#jobtaskinfo) |
| [**list**](job-task.md#list)|   [JobTaskQuery](job-task.md#jobtaskquery) |   [JobTasksInfo](job-task.md#jobtasksinfo) |
| [**stat**](job-task.md#stat)|   [JobTaskStatQuery](job-task.md#jobtaskstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### delete
> **POST** /inventory/v1/job-task/delete
>

> Deletes a specific JobTask. You must specify the `job_task_id` of the JobTask to delete.

| Type | Message |
| :--- | :--- |
| Request | [JobTaskRequest](job-task.md#jobtaskrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "job_task_id": "job-task-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** /inventory/v1/job-task/get
>

> Gets a specific JobTask. Prints detailed information about the JobTask, including its state, updated or failure counts, and error log.

| Type | Message |
| :--- | :--- |
| Request | [GetJobTaskRequest](job-task.md#getjobtaskrequest) |
| Response |  [JobTaskInfo](job-task.md#jobtaskinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "job_task_id": "job-task-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "job_task_id": "job-task-123456789012",
    "status": "FAILURE",
    "updated_count": 199,
    "failure_count": 1,
    "errors": [
        {
            "error_code": "ERROR_PLUGIN",
            "message": "{\"tags\": [\"Could not interpret the value as a list\"]}",
            "additional": {
                "domain_id": "domain-123456789012",
                "resource_id": "eventarc-us-central1-function",
                "resource_type": "inventory.CloudService",
                "cloud_service_group": "Pub/Sub",
                "cloud_service_type": "Subscription",
                "provider": "google_cloud"
            }
        }
    ],
    "job_id": "job-123456789012",
    "secret_id": "secret-123456789012",
    "provider": "google_cloud",
    "service_account_id": "sa-123456789012",
    "project_id": "project-123456789012",
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T11:00:02.588Z",
    "started_at": "2022-01-01T11:00:02.819Z",
    "finished_at": "2022-01-01T11:00:34.398Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /inventory/v1/job-task/list
>

> Gets a list of all JobTasks in a specific Job. You can use a query to get a filtered list of JobTasks.

| Type | Message |
| :--- | :--- |
| Request | [JobTaskQuery](job-task.md#jobtaskquery) |
| Response |  [JobTasksInfo](job-task.md#jobtasksinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {}
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "job_task_id": "job_task-69b301d0fbfc",
            "status": "SUCCESS",
            "updated_count": 55,
            "job_id": "job-587a3d3b4db3",
            "secret_id": "secret-957e407bfc15",
            "provider": "aws",
            "service_account_id": "sa-a41ff4765671",
            "project_id": "project-77dffd3f7cd3",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-06-17T08:00:00.680Z",
            "started_at": "2022-06-17T08:00:00.914Z",
            "finished_at": "2022-06-17T08:05:48.933Z"
        },
        {
            "job_task_id": "job_task-c5077338cf23",
            "status": "SUCCESS",
            "updated_count": 1921,
            "job_id": "job-587a3d3b4db3",
            "secret_id": "secret-1cd7417c1889",
            "provider": "aws",
            "service_account_id": "sa-5e186fcc7c91",
            "project_id": "project-18655561c535",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-06-17T08:00:00.582Z",
            "started_at": "2022-06-17T08:00:00.814Z",
            "finished_at": "2022-06-17T08:07:31.995Z"
        }
    ],
    "total_count": 4839
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /inventory/v1/job-task/stat
>


| Type | Message |
| :--- | :--- |
| Request | [JobTaskStatQuery](job-task.md#jobtaskstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### GetJobTaskRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| job_task_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### JobTaskInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">job_task_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">status</td>
      <td style="text-align:left"><ul>
          	<li>JOB_TASK_STATE_NONE</li>
          	<li>PENDING</li>
          	<li>CANCELED</li>
          	<li>IN_PROGRESS</li>
          	<li>SUCCESS</li>
          	<li>FAILURE</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_count</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">updated_count</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">failure_count</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">deleted_count</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">disconnected_count</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">errors</td>
      <td style="text-align:left"><a href="job-task.md#errorinfo">list of ErrorInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">job_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">service_account_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">started_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">finished_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### JobTaskQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">job_task_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">status</td>
      <td style="text-align:left"><ul>
          	<li>JOB_TASK_STATE_NONE</li>
          	<li>PENDING</li>
          	<li>CANCELED</li>
          	<li>IN_PROGRESS</li>
          	<li>SUCCESS</li>
          	<li>FAILURE</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">job_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">service_account_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### JobTaskRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| job_task_id |string|✔| |
| domain_id |string|✔| |

### JobTaskStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### JobTasksInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of JobTaskInfo](job-task.md#jobtaskinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
