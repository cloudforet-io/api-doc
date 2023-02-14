---
description: A Job is an act of collecting external cloud resources through plugins.
---
# Job

>  **Package : spaceone.api.inventory.v1**

## Job

{% hint style="info" %}
**Job Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**delete**](job.md#delete)|   [JobRequest](job.md#jobrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](job.md#get)|   [GetJobRequest](job.md#getjobrequest) |  JobInfo|
| [**list**](job.md#list)|   [JobsQuery](job.md#jobsquery) |   [JobsInfo](job.md#jobsinfo) |
| [**stat**](job.md#stat)|   [JobStatQuery](job.md#jobstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### delete
> **POST** /inventory/v1/job/delete
>

> Deletes a specific Job. You must specify the `job_id` of the Job to delete.

| Type | Message |
| :--- | :--- |
| Request | [JobRequest](job.md#jobrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "job_id": "job-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** /inventory/v1/job/get
>

> Gets a specific Job. Prints detailed information about the Job, including its state, total tasks, and collector info.

| Type | Message |
| :--- | :--- |
| Request | [GetJobRequest](job.md#getjobrequest) |
| Response | JobInfo |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "job_id": "job-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "job_id": "job-123456789012",
    "status": "ERROR",
    "filter": {},
    "total_tasks": 2,
    "collector_info": {
        "collector_id": "collector-123456789012",
        "name": "Jenkins Collector",
        "state": "ENABLED",
        "plugin_info": {
            "plugin_id": "plugin-jenkins-inven-collector",
            "version": "0.1.1"
        },
        "provider": "jenkins",
        "capability": {},
        "is_public": true
    },
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T10:00:01.389Z",
    "updated_at": "2022-01-01T10:00:01.389Z",
    "finished_at": "2022-01-01T10:02:11.270Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /inventory/v1/job/list
>

> Gets a list of all Jobs. You can use a query to get a filtered list of Jobs.

| Type | Message |
| :--- | :--- |
| Request | [JobsQuery](job.md#jobsquery) |
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
            "job_id": "job-3b124006c2d2",
            "status": "SUCCESS",
            "filter": {},
            "total_tasks": 2,
            "collector_info": {
                "collector_id": "collector-accd02663b3d",
                "name": "openstack-collector",
                "state": "ENABLED",
                "plugin_info": {
                    "plugin_id": "plugin-openstack-inven-collector",
                    "version": "0.4.2.20220616.134758"
                },
                "provider": "openstack",
                "capability": {
                    "supported_schema": [
                        "openstack_credentials"
                    ]
                },
                "is_public": true
            },
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-06-17T08:00:01.225Z",
            "updated_at": "2022-06-17T08:00:01.225Z",
            "finished_at": "2022-06-17T08:00:15.197Z"
        },
        {
            "job_id": "job-587a3d3b4db3",
            "status": "SUCCESS",
            "filter": {},
            "total_tasks": 3,
            "collector_info": {
                "collector_id": "collector-2c0847644f39",
                "name": "AWS stat-kwon Collector",
                "state": "ENABLED",
                "plugin_info": {
                    "plugin_id": "plugin-30d21ef75a5d",
                    "version": "1.13.13.20220610.143142"
                },
                "provider": "aws",
                "capability": {
                    "supported_schema": [
                        "aws_access_key"
                    ]
                },
                "is_public": true
            },
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-06-17T08:00:00.407Z",
            "updated_at": "2022-06-17T08:00:00.407Z",
            "finished_at": "2022-06-17T08:07:32.023Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /inventory/v1/job/stat
>


| Type | Message |
| :--- | :--- |
| Request | [JobStatQuery](job.md#jobstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### GetJobRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| job_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

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

### JobsQuery
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
          	<li>JOB_STATE_NONE</li>
          	<li>CREATED</li>
          	<li>CANCELED</li>
          	<li>IN_PROGRESS</li>
          	<li>SUCCESS</li>
          	<li>ERROR</li>
          	<li>TIMEOUT</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">collector_id</td>
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


