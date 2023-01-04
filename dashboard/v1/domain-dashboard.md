---
description: description of dashboard
---
# Domain dashboard

>  **Package : spaceone.api.dashboard.v1**

## DomainDashboard

{% hint style="info" %}
**DomainDashboard Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](domain-dashboard.md#create)|   [CreateDomainDashboardRequest](domain-dashboard.md#createdomaindashboardrequest) |   [DomainDashboardInfo](domain-dashboard.md#domaindashboardinfo) |
| [**update**](domain-dashboard.md#update)|   [UpdateDomainDashboardRequest](domain-dashboard.md#updatedomaindashboardrequest) |   [DomainDashboardInfo](domain-dashboard.md#domaindashboardinfo) |
| [**delete**](domain-dashboard.md#delete)|   [DomainDashboardRequest](domain-dashboard.md#domaindashboardrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](domain-dashboard.md#get)|   [GetDomainDashboardRequest](domain-dashboard.md#getdomaindashboardrequest) |   [DomainDashboardInfo](domain-dashboard.md#domaindashboardinfo) |
| [**delete_version**](domain-dashboard.md#delete_version)|   [DomainDashboardVersionRequest](domain-dashboard.md#domaindashboardversionrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**revert_version**](domain-dashboard.md#revert_version)|   [DomainDashboardVersionRequest](domain-dashboard.md#domaindashboardversionrequest) |   [DomainDashboardInfo](domain-dashboard.md#domaindashboardinfo) |
| [**get_version**](domain-dashboard.md#get_version)|   [GetDomainDashboardVersionRequest](domain-dashboard.md#getdomaindashboardversionrequest) |   [DomainDashboardVersionInfo](domain-dashboard.md#domaindashboardversioninfo) |
| [**list_versions**](domain-dashboard.md#list_versions)|   [DomainDashboardVersionQuery](domain-dashboard.md#domaindashboardversionquery) |   [DomainDashboardVersionsInfo](domain-dashboard.md#domaindashboardversionsinfo) |
| [**list**](domain-dashboard.md#list)|   [DomainDashboardQuery](domain-dashboard.md#domaindashboardquery) |   [DomainDashboardsInfo](domain-dashboard.md#domaindashboardsinfo) |
| [**stat**](domain-dashboard.md#stat)|   [DomainDashboardStatQuery](domain-dashboard.md#domaindashboardstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /dashboard/v1/domain-dashboards
>


| Type | Message |
| :--- | :--- |
| Request | [CreateDomainDashboardRequest](domain-dashboard.md#createdomaindashboardrequest) |
| Response |  [DomainDashboardInfo](domain-dashboard.md#domaindashboardinfo)  |
 
 

 
### update
> **PUT** /dashboard/v1/domain-dashboard/{domain_dashboard_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateDomainDashboardRequest](domain-dashboard.md#updatedomaindashboardrequest) |
| Response |  [DomainDashboardInfo](domain-dashboard.md#domaindashboardinfo)  |
 
 

 
### delete
> **DELETE** /dashboard/v1/domain-dashboard/{domain_dashboard_id}
>


| Type | Message |
| :--- | :--- |
| Request | [DomainDashboardRequest](domain-dashboard.md#domaindashboardrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /dashboard/v1/domain-dashboard/{domain_dashboard_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetDomainDashboardRequest](domain-dashboard.md#getdomaindashboardrequest) |
| Response |  [DomainDashboardInfo](domain-dashboard.md#domaindashboardinfo)  |
 
 

 
### delete_version
> **DELETE** /dashboard/v1/domain-dashboard/{domain_dashboard_id}/version/{version}
>


| Type | Message |
| :--- | :--- |
| Request | [DomainDashboardVersionRequest](domain-dashboard.md#domaindashboardversionrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### revert_version
> **POST** /dashboard/v1/domain-dashboard/{domain_dashboard_id}/version/{version}/revert
>


| Type | Message |
| :--- | :--- |
| Request | [DomainDashboardVersionRequest](domain-dashboard.md#domaindashboardversionrequest) |
| Response |  [DomainDashboardInfo](domain-dashboard.md#domaindashboardinfo)  |
 
 

 
### get_version
> **GET** /dashboard/v1/domain-dashboard/{domain_dashboard_id}/version/{version}
>


| Type | Message |
| :--- | :--- |
| Request | [GetDomainDashboardVersionRequest](domain-dashboard.md#getdomaindashboardversionrequest) |
| Response |  [DomainDashboardVersionInfo](domain-dashboard.md#domaindashboardversioninfo)  |
 
 

 
### list_versions
> **GET** /dashboard/v1/domain-dashboard/{domain_dashboard_id}/versions
>
> **POST** /dashboard/v1/domain-dashboard/{domain_dashboard_id}/versions/search



| Type | Message |
| :--- | :--- |
| Request | [DomainDashboardVersionQuery](domain-dashboard.md#domaindashboardversionquery) |
| Response |  [DomainDashboardVersionsInfo](domain-dashboard.md#domaindashboardversionsinfo)  |
 
 

 
### list
> **GET** /dashboard/v1/domain-dashboards
>
> **POST** /dashboard/v1/domain-dashboards/search



| Type | Message |
| :--- | :--- |
| Request | [DomainDashboardQuery](domain-dashboard.md#domaindashboardquery) |
| Response |  [DomainDashboardsInfo](domain-dashboard.md#domaindashboardsinfo)  |
 
 

 
### stat
> **POST** /dashboard/v1/domain-dashboards/stat
>


| Type | Message |
| :--- | :--- |
| Request | [DomainDashboardStatQuery](domain-dashboard.md#domaindashboardstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateDomainDashboardRequest
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



### DomainDashboardInfo
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
      <td style="text-align:left; width:100px;">domain_dashboard_id</td>
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



### DomainDashboardQuery
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
      <td style="text-align:left; width:100px;">domain_dashboard_id</td>
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



### DomainDashboardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_dashboard_id |string|✔| |
| domain_id |string|✔| |

### DomainDashboardStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### DomainDashboardVersionInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| domain_dashboard_id |string | |
| version |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| latest |bool | |
| layouts |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| variables |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| settings |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| variables_schema |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
| created_at |string | |

### DomainDashboardVersionQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| domain_dashboard_id |string|✔| |
| version |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✘| |
| domain_id |string|✔| |

### DomainDashboardVersionRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_dashboard_id |string|✔| |
| version |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✔| |
| domain_id |string|✔| |

### DomainDashboardVersionsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of DomainDashboardVersionInfo](domain-dashboard.md#domaindashboardversioninfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### DomainDashboardsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of DomainDashboardInfo](domain-dashboard.md#domaindashboardinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetDomainDashboardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_dashboard_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### GetDomainDashboardVersionRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_dashboard_id |string|✔| |
| version |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### UpdateDomainDashboardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_dashboard_id |string|✔| |
| name |string|✘| |
| layouts |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| variables |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| settings |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| variables_schema |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
