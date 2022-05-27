---
description:  
---
# Job

>  **Package : spaceone.api.cost_analysis.v1**

## Job

{% hint style="info" %}
**Job Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :--- | :--- | :--- | :--- |
| [**cancel**](job.md#cancel)|   [JobRequest](job.md#jobrequest) |   [JobInfo](job.md#jobinfo) |  |
| [**get**](job.md#get)|   [GetJobRequest](job.md#getjobrequest) |   [JobInfo](job.md#jobinfo) |  |
| [**list**](job.md#list)|   [JobQuery](job.md#jobquery) |   [JobsInfo](job.md#jobsinfo) |  |
| [**stat**](job.md#stat)|   [JobStatQuery](job.md#jobstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### cancel
> **POST** /cost-analysis/v1/job/{job_id}/cancel
>


| Type | Message |
| :--- | :--- |
| Request | [JobRequest](job.md#jobrequest) |
| Response |  [JobInfo](job.md#jobinfo)  |
 
 

 
### get
> **GET** /cost-analysis/v1/job/{job_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetJobRequest](job.md#getjobrequest) |
| Response |  [JobInfo](job.md#jobinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v1/jobs
>
> **POST** /cost-analysis/v1/jobs/search



| Type | Message |
| :--- | :--- |
| Request | [JobQuery](job.md#jobquery) |
| Response |  [JobsInfo](job.md#jobsinfo)  |
 
 

 
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
| job_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### JobInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">job_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">status</td>
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
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">error_code</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">error_message</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">total_tasks</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">remained_tasks</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">data_source_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">finished_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">changed</td>
      <td style="text-align:left"><a href="job.md#changedinfo">list of ChangedInfo</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### JobQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">job_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">status</td>
      <td style="text-align:left"><ul>
          	<li>SCOPE_NONE</li>
          	<li>IN_PROGRESS</li>
          	<li>SUCCESS</li>
          	<li>FAILURE</li>
          	<li>TIMEOUT</li>
          	<li>CANCELED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">data_source_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### JobRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| job_id |string|✅| |
| domain_id |string|✅| |

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
