---
description: description of dashboard
---
# Project dashboard

>  **Package : spaceone.api.dashboard.v1**

## ProjectDashboard

{% hint style="info" %}
**ProjectDashboard Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](project-dashboard.md#create)|   [CreateProjectDashboardRequest](project-dashboard.md#createprojectdashboardrequest) |   [ProjectDashboardInfo](project-dashboard.md#projectdashboardinfo) |
| [**update**](project-dashboard.md#update)|   [UpdateProjectDashboardRequest](project-dashboard.md#updateprojectdashboardrequest) |   [ProjectDashboardInfo](project-dashboard.md#projectdashboardinfo) |
| [**delete**](project-dashboard.md#delete)|   [ProjectDashboardRequest](project-dashboard.md#projectdashboardrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](project-dashboard.md#get)|   [GetProjectDashboardRequest](project-dashboard.md#getprojectdashboardrequest) |   [ProjectDashboardInfo](project-dashboard.md#projectdashboardinfo) |
| [**delete_version**](project-dashboard.md#delete_version)|   [ProjectDashboardVersionRequest](project-dashboard.md#projectdashboardversionrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**revert_version**](project-dashboard.md#revert_version)|   [ProjectDashboardVersionRequest](project-dashboard.md#projectdashboardversionrequest) |   [ProjectDashboardInfo](project-dashboard.md#projectdashboardinfo) |
| [**get_version**](project-dashboard.md#get_version)|   [GetProjectDashboardVersionRequest](project-dashboard.md#getprojectdashboardversionrequest) |   [ProjectDashboardVersionInfo](project-dashboard.md#projectdashboardversioninfo) |
| [**list_versions**](project-dashboard.md#list_versions)|   [ProjectDashboardVersionQuery](project-dashboard.md#projectdashboardversionquery) |   [ProjectDashboardVersionsInfo](project-dashboard.md#projectdashboardversionsinfo) |
| [**list**](project-dashboard.md#list)|   [ProjectDashboardQuery](project-dashboard.md#projectdashboardquery) |   [ProjectDashboardsInfo](project-dashboard.md#projectdashboardsinfo) |
| [**stat**](project-dashboard.md#stat)|   [ProjectDashboardStatQuery](project-dashboard.md#projectdashboardstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /dashboard/v1/project-dashboard/create
>


| Type | Message |
| :--- | :--- |
| Request | [CreateProjectDashboardRequest](project-dashboard.md#createprojectdashboardrequest) |
| Response |  [ProjectDashboardInfo](project-dashboard.md#projectdashboardinfo)  |
 
 

 
### update
> **POST** /dashboard/v1/project-dashboard/update
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateProjectDashboardRequest](project-dashboard.md#updateprojectdashboardrequest) |
| Response |  [ProjectDashboardInfo](project-dashboard.md#projectdashboardinfo)  |
 
 

 
### delete
> **POST** /dashboard/v1/project-dashboard/delete
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectDashboardRequest](project-dashboard.md#projectdashboardrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **POST** /dashboard/v1/project-dashboard/get
>


| Type | Message |
| :--- | :--- |
| Request | [GetProjectDashboardRequest](project-dashboard.md#getprojectdashboardrequest) |
| Response |  [ProjectDashboardInfo](project-dashboard.md#projectdashboardinfo)  |
 
 

 
### delete_version
> **POST** /dashboard/v1/project-dashboard/delete-version
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectDashboardVersionRequest](project-dashboard.md#projectdashboardversionrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### revert_version
> **POST** /dashboard/v1/project-dashboard/revert-version
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectDashboardVersionRequest](project-dashboard.md#projectdashboardversionrequest) |
| Response |  [ProjectDashboardInfo](project-dashboard.md#projectdashboardinfo)  |
 
 

 
### get_version
> **POST** /dashboard/v1/project-dashboard/get-version
>


| Type | Message |
| :--- | :--- |
| Request | [GetProjectDashboardVersionRequest](project-dashboard.md#getprojectdashboardversionrequest) |
| Response |  [ProjectDashboardVersionInfo](project-dashboard.md#projectdashboardversioninfo)  |
 
 

 
### list_versions
> **POST** /dashboard/v1/project-dashboard/list-versions
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectDashboardVersionQuery](project-dashboard.md#projectdashboardversionquery) |
| Response |  [ProjectDashboardVersionsInfo](project-dashboard.md#projectdashboardversionsinfo)  |
 
 

 
### list
> **POST** /dashboard/v1/project-dashboard/list
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectDashboardQuery](project-dashboard.md#projectdashboardquery) |
| Response |  [ProjectDashboardsInfo](project-dashboard.md#projectdashboardsinfo)  |
 
 

 
### stat
> **POST** /dashboard/v1/project-dashboard/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectDashboardStatQuery](project-dashboard.md#projectdashboardstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateProjectDashboardRequest
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
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">viewers</td>
      <td style="text-align:left"><ul>
          	<li>VIEWERS_NONE</li>
          	<li>PUBLIC</li>
          	<li>PRIVATE</li>
        </ul></td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">layouts</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">variables</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">settings</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">variables_schema</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">labels</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
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



### GetProjectDashboardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_dashboard_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### GetProjectDashboardVersionRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_dashboard_id |string|✔| |
| version |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### ProjectDashboardInfo
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
      <td style="text-align:left; width:100px;">project_dashboard_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">viewers</td>
      <td style="text-align:left"><ul>
          	<li>VIEWERS_NONE</li>
          	<li>PUBLIC</li>
          	<li>PRIVATE</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">version</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">layouts</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">variables</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">settings</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">variables_schema</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">labels</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
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
  </tbody>
</table>



### ProjectDashboardQuery
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
      <td style="text-align:left; width:100px;">project_dashboard_id</td>
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
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">viewers</td>
      <td style="text-align:left"><ul>
          	<li>VIEWERS_NONE</li>
          	<li>PUBLIC</li>
          	<li>PRIVATE</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
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



### ProjectDashboardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_dashboard_id |string|✔| |
| domain_id |string|✔| |

### ProjectDashboardStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### ProjectDashboardVersionInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| project_dashboard_id |string | |
| version |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| latest |bool | |
| layouts |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| variables |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| settings |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| variables_schema |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
| created_at |string | |

### ProjectDashboardVersionQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| project_dashboard_id |string|✔| |
| version |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✘| |
| domain_id |string|✔| |

### ProjectDashboardVersionRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_dashboard_id |string|✔| |
| version |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✔| |
| domain_id |string|✔| |

### ProjectDashboardVersionsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ProjectDashboardVersionInfo](project-dashboard.md#projectdashboardversioninfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### ProjectDashboardsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ProjectDashboardInfo](project-dashboard.md#projectdashboardinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateProjectDashboardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_dashboard_id |string|✔| |
| name |string|✘| |
| layouts |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| variables |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| settings |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| variables_schema |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
