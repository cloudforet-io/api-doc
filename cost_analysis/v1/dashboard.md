---
description:  
---
# Dashboard

>  **Package : spaceone.api.cost_analysis.v1**

## Dashboard

{% hint style="info" %}
**Dashboard Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](dashboard.md#create)|   [CreateDashboardRequest](dashboard.md#createdashboardrequest) |   [DashboardInfo](dashboard.md#dashboardinfo) |  |
| 2 | [**update**](dashboard.md#update)|   [UpdateDashboardRequest](dashboard.md#updatedashboardrequest) |   [DashboardInfo](dashboard.md#dashboardinfo) |  |
| 3 | [**change_scope**](dashboard.md#change_scope)|   [ChangeDashboardScopeRequest](dashboard.md#changedashboardscoperequest) |   [DashboardInfo](dashboard.md#dashboardinfo) |  |
| 4 | [**delete**](dashboard.md#delete)|   [DashboardRequest](dashboard.md#dashboardrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**get**](dashboard.md#get)|   [GetDashboardRequest](dashboard.md#getdashboardrequest) |   [DashboardInfo](dashboard.md#dashboardinfo) |  |
| 6 | [**list**](dashboard.md#list)|   [DashboardQuery](dashboard.md#dashboardquery) |   [DashboardsInfo](dashboard.md#dashboardsinfo) |  |
| 7 | [**stat**](dashboard.md#stat)|   [DashboardStatQuery](dashboard.md#dashboardstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /cost-analysis/v1/dashboards
>


| Type | Message |
| :--- | :--- |
| Request | [CreateDashboardRequest](dashboard.md#createdashboardrequest) |
| Response |  [DashboardInfo](dashboard.md#dashboardinfo)  |
 
 

 
### update
> **PUT** /cost-analysis/v1/dashboard/{dashboard_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateDashboardRequest](dashboard.md#updatedashboardrequest) |
| Response |  [DashboardInfo](dashboard.md#dashboardinfo)  |
 
 

 
### change_scope
> **PUT** /cost-analysis/v1/dashboard/{dashboard_id}/scope
>


| Type | Message |
| :--- | :--- |
| Request | [ChangeDashboardScopeRequest](dashboard.md#changedashboardscoperequest) |
| Response |  [DashboardInfo](dashboard.md#dashboardinfo)  |
 
 

 
### delete
> **DELETE** /cost-analysis/v1/dashboard/{dashboard_id}
>


| Type | Message |
| :--- | :--- |
| Request | [DashboardRequest](dashboard.md#dashboardrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /cost-analysis/v1/dashboard/{dashboard_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetDashboardRequest](dashboard.md#getdashboardrequest) |
| Response |  [DashboardInfo](dashboard.md#dashboardinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v1/dashboards
>
> **POST** /cost-analysis/v1/dashboards/search



| Type | Message |
| :--- | :--- |
| Request | [DashboardQuery](dashboard.md#dashboardquery) |
| Response |  [DashboardsInfo](dashboard.md#dashboardsinfo)  |
 
 

 
### stat
> **POST** /cost-analysis/v1/dashboards/stat
>


| Type | Message |
| :--- | :--- |
| Request | [DashboardStatQuery](dashboard.md#dashboardstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### ChangeDashboardScopeRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">dashboard_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">scope</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>PUBLIC</li>
          	<li>PRIVATE</li>
        </ul></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### CreateDashboardRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | name |string|✅| |
| 2 | default_layout_id |string|❌| |
| 3 | custom_layouts |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| 4 | default_filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 6 | domain_id |string|✅| |

### DashboardInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">dashboard_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">scope</td>
      <td style="text-align:left"><ul>
          	<li>SCOPE_NONE</li>
          	<li>PUBLIC</li>
          	<li>PRIVATE</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">default_layout_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">custom_layouts</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">default_filter</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### DashboardQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">dashboard_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">scope</td>
      <td style="text-align:left"><ul>
          	<li>SCOPE_NONE</li>
          	<li>PUBLIC</li>
          	<li>PRIVATE</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### DashboardRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | dashboard_id |string|✅| |
| 2 | domain_id |string|✅| |

### DashboardStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### DashboardsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of DashboardInfo](dashboard.md#dashboardinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetDashboardRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | dashboard_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### UpdateDashboardRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | dashboard_id |string|✅| |
| 2 | name |string|❌| |
| 3 | default_layout_id |string|❌| |
| 4 | custom_layouts |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| 5 | default_filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 7 | domain_id |string|✅| |
