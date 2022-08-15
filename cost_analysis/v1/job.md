---
description: A Job is an act of collecting external cost data through plugins. The data to collect is defined in a plugin.
---
# Job

>  **Package : spaceone.api.cost_analysis.v1**

## Job

{% hint style="info" %}
**Job Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**cancel**](job.md#cancel)|   [JobRequest](job.md#jobrequest) |   [JobInfo](job.md#jobinfo) |
| [**get**](job.md#get)|   [GetJobRequest](job.md#getjobrequest) |   [JobInfo](job.md#jobinfo) |
| [**list**](job.md#list)|   [JobQuery](job.md#jobquery) |   [JobsInfo](job.md#jobsinfo) |
| [**stat**](job.md#stat)|   [JobStatQuery](job.md#jobstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### cancel
> **POST** /cost-analysis/v1/job/{job_id}/cancel
>

> Cancels a specific Job. You can manually cease a Job in run with this method.

| Type | Message |
| :--- | :--- |
| Request | [JobRequest](job.md#jobrequest) |
| Response |  [JobInfo](job.md#jobinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "job_id": "job-07994c7c9021"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "job_id": "job-07994c7c9021",
    "status": "CANCELED",
    "options": {
        "no_preload_cache": false,
        "start": "2021-01-01T00:00:00Z"
    },
    "total_tasks": 2,
    "remained_tasks": 2,
    "data_source_id": "ds-fcba92ca73b1",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-04-02T09:17:44.031Z",
    "updated_at": "2022-04-02T09:19:47.715Z",
    "finished_at": "2022-04-02T09:19:47.715Z",
    "changed": [
        {
            "start": "2021-01-01T00:00:00.000Z"
        }
    ]
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /cost-analysis/v1/job/{job_id}
>

> Gets a specific Job. Prints detailed information about the Job, including the plugin used, operation time, and `status`.

| Type | Message |
| :--- | :--- |
| Request | [GetJobRequest](job.md#getjobrequest) |
| Response |  [JobInfo](job.md#jobinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "job_id": "job-85cf2c385252"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "job_id": "job-85cf2c385252",
    "status": "SUCCESS",
    "options": {
        "no_preload_cache": false,
        "start": null
    },
    "total_tasks": 1,
    "data_source_id": "ds-c96609f5afeb",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-17T16:00:08.254Z",
    "updated_at": "2022-07-17T16:01:30.637Z",
    "finished_at": "2022-07-17T16:01:30.637Z",
    "changed": [
        {
            "start": "2022-07-01T00:00:00.000Z"
        }
    ]
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /cost-analysis/v1/jobs
>
> **POST** /cost-analysis/v1/jobs/search


> Gets a list of all Jobs. You can use a query to get a filtered list of Jobs.

| Type | Message |
| :--- | :--- |
| Request | [JobQuery](job.md#jobquery) |
| Response |  [JobsInfo](job.md#jobsinfo)  |
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
            "job_id": "job-85cf2c385252",
            "status": "SUCCESS",
            "options": {
                "start": null,
                "no_preload_cache": false
            },
            "total_tasks": 1,
            "data_source_id": "ds-c96609f5afeb",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-07-17T16:00:08.254Z",
            "updated_at": "2022-07-17T16:01:30.637Z",
            "finished_at": "2022-07-17T16:01:30.637Z",
            "changed": [
                {
                    "start": "2022-07-01T00:00:00.000Z"
                }
            ]
        },
        {
            "job_id": "job-6b6765f757a9",
            "status": "SUCCESS",
            "options": {
                "start": null,
                "no_preload_cache": false
            },
            "total_tasks": 2,
            "data_source_id": "ds-fcba92ca73b1",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-07-17T16:00:05.077Z",
            "updated_at": "2022-07-17T16:01:28.206Z",
            "finished_at": "2022-07-17T16:01:28.206Z",
            "changed": [
                {
                    "start": "2022-07-01T00:00:00.000Z"
                }
            ]
        }
    ],
    "total_count": 372
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /cost-analysis/v1/jobs/stat
>


| Type | Message |
| :--- | :--- |
| Request | [JobStatQuery](job.md#jobstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### ChangedInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| start |string | |
| end |string | |

### GetJobRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| job_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### JobInfo
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
      <td style="text-align:left; width:100px;">job_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">status</td>
      <td style="text-align:left"><ul>
          	<li>SCOPE_NONE</li>
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
      <td style="text-align:left; width:100px;">total_tasks</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">remained_tasks</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
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
      <td style="text-align:left; width:100px;">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">finished_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">changed</td>
      <td style="text-align:left"><a href="job.md#changedinfo">list of ChangedInfo</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### JobQuery
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
      <td style="text-align:left; width:100px;">job_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">status</td>
      <td style="text-align:left"><ul>
          	<li>SCOPE_NONE</li>
          	<li>IN_PROGRESS</li>
          	<li>SUCCESS</li>
          	<li>FAILURE</li>
          	<li>TIMEOUT</li>
          	<li>CANCELED</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data_source_id</td>
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



### JobRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| job_id |string|✔| |
| domain_id |string|✔| |

### JobStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### JobsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of JobInfo](job.md#jobinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
