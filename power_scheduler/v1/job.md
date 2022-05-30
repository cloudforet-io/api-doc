---
description:  
---
# Job

>  **Package : spaceone.api.power_scheduler.v1**

## Job

{% hint style="info" %}
**Job Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](job.md#list)|   [JobsQuery](job.md#jobsquery) |   [JobsInfo](job.md#jobsinfo) |
| [**stat**](job.md#stat)|   [JobStatQuery](job.md#jobstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### list
> **GET** /power-scheduler/v1/jobs
>
> **POST** /power-scheduler/v1/jobs/search



| Type | Message |
| :--- | :--- |
| Request | [JobsQuery](job.md#jobsquery) |
| Response |  [JobsInfo](job.md#jobsinfo)  |
 
 

 
### stat
> **POST** /power-scheduler/v1/jobs/stat
>


| Type | Message |
| :--- | :--- |
| Request | [JobStatQuery](job.md#jobstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### ErrorInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| error_code |string | |
| message |string | |
| additional |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

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
          	<li>NONE</li>
          	<li>CREATED</li>
          	<li>CANCELED</li>
          	<li>IN_PROGRESS</li>
          	<li>SUCCESS</li>
          	<li>ERROR</li>
          	<li>TIMEOUT</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">filter</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
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
      <td style="text-align:left; width:100px;">errors</td>
      <td style="text-align:left"><a href="job.md#errorinfo">list of ErrorInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">schedule_info</td>
      <td style="text-align:left"><a href="job.md#scheduleinfo">ScheduleInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">control_action</td>
      <td style="text-align:left"><ul>
          	<li>CONTROL_ACTION_NONE</li>
          	<li>RUNNING</li>
          	<li>STOPPED</li>
        </ul></td>
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
      <td style="text-align:left; width:100px;">job_type</td>
      <td style="text-align:left"><ul>
          	<li>JOB_TYPE_NONE</li>
          	<li>APPLY</li>
          	<li>MAINTAIN</li>
        </ul></td>
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
  </tbody>
</table>



### JobStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

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
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">job_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">status</td>
      <td style="text-align:left"><ul>
          	<li>JOB_STATUS_NONE</li>
          	<li>CREATED</li>
          	<li>CANCELED</li>
          	<li>IN_PROGRESS</li>
          	<li>SUCCESS</li>
          	<li>ERROR</li>
          	<li>TIMEOUT</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">schedule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">control_action</td>
      <td style="text-align:left"><ul>
          	<li>CONTROL_ACTION_NONE</li>
          	<li>RUNNING</li>
          	<li>STOPPED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">job_type</td>
      <td style="text-align:left"><ul>
          	<li>JOB_TYPE_NONE</li>
          	<li>APPLY</li>
          	<li>MAINTAIN</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>


