---
description: A JobTask is a task unit subdividing a Job. The division criteria are specified in each DataSource plugin.
---
# Job task

>  **Package : spaceone.api.cost_analysis.v1**

## JobTask

{% hint style="info" %}
**JobTask Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**get**](job-task.md#get)|   [GetJobTaskRequest](job-task.md#getjobtaskrequest) |   [JobTaskInfo](job-task.md#jobtaskinfo) |
| [**list**](job-task.md#list)|   [JobTaskQuery](job-task.md#jobtaskquery) |   [JobTasksInfo](job-task.md#jobtasksinfo) |
| [**stat**](job-task.md#stat)|   [JobTaskStatQuery](job-task.md#jobtaskstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### get
> **GET** /cost-analysis/v1/job-task/{job_task_id}
>

> Gets a specific JobTask. Prints detailed information about the JobTask, including the relevant resources: DataSource and Job. The criteria used for dividing a Job into JobTasks can be found in the DataSource used, but the total count of divided JobTasks can be found by this method.

| Type | Message |
| :--- | :--- |
| Request | [GetJobTaskRequest](job-task.md#getjobtaskrequest) |
| Response |  [JobTaskInfo](job-task.md#jobtaskinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "job_task_id": "job-task-3622d860a776"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "job_task_id": "job-task-3622d860a776",
    "status": "SUCCESS",
    "options": {
        "month": "202207",
        "platform": "gcp"
    },
    "created_count": 1,
    "job_id": "job-85cf2c385252",
    "data_source_id": "ds-c96609f5afeb",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-17T16:00:08.266Z",
    "started_at": "2022-07-17T16:01:28.243Z",
    "updated_at": "2022-07-17T16:01:28.939Z",
    "finished_at": "2022-07-17T16:01:28.939Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /cost-analysis/v1/job-tasks
>
> **POST** /cost-analysis/v1/job-tasks/search


> Gets a list of all JobTasks. You can use a query to get a filtered list of JobTasks.

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
            "job_task_id": "job-task-3622d860a776",
            "status": "SUCCESS",
            "options": {
                "platform": "gcp",
                "month": "202207"
            },
            "created_count": 1,
            "job_id": "job-85cf2c385252",
            "data_source_id": "ds-c96609f5afeb",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-07-17T16:00:08.266Z",
            "started_at": "2022-07-17T16:01:28.243Z",
            "updated_at": "2022-07-17T16:01:28.939Z",
            "finished_at": "2022-07-17T16:01:28.939Z"
        },
        {
            "job_task_id": "job-task-038c0b076ec5",
            "status": "SUCCESS",
            "options": {
                "account": "257706363616",
                "start": "2022-07-01"
            },
            "created_count": 5756,
            "job_id": "job-6b6765f757a9",
            "data_source_id": "ds-fcba92ca73b1",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-07-17T16:00:05.099Z",
            "started_at": "2022-07-17T16:00:47.356Z",
            "updated_at": "2022-07-17T16:01:20.856Z",
            "finished_at": "2022-07-17T16:01:20.856Z"
        }
    ],
    "total_count": 720
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /cost-analysis/v1/job-tasks/stat
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
| job_task_id |string|???| |
| domain_id |string|???| |
| only |list of string|???| |

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
          	<li>SCOPE_NONE</li>
          	<li>PENDING</li>
          	<li>IN_PROGRESS</li>
          	<li>SUCCESS</li>
          	<li>FAILURE</li>
          	<li>TIMEOUT</li>
          	<li>CANCELED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_count</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">error_code</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">error_message</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">job_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data_source_id</td>
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
      <td style="text-align:left; width:100px;">updated_at</td>
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
<td style="text-align:center">???</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">job_task_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">???</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">status</td>
      <td style="text-align:left"><ul>
          	<li>SCOPE_NONE</li>
          	<li>PENDING</li>
          	<li>IN_PROGRESS</li>
          	<li>SUCCESS</li>
          	<li>FAILURE</li>
          	<li>TIMEOUT</li>
          	<li>CANCELED</li>
        </ul></td>
<td style="text-align:center">???</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">job_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">???</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data_source_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">???</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">???</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### JobTaskStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|???| |
| domain_id |string|???| |

### JobTasksInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of JobTaskInfo](job-task.md#jobtaskinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
