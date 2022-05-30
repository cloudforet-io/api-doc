---
description:  
---
# User dashboard

>  **Package : spaceone.api.cost_analysis.v1**

## UserDashboard

{% hint style="info" %}
**UserDashboard Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](user-dashboard.md#create)|   [CreateUserDashboardRequest](user-dashboard.md#createuserdashboardrequest) |   [UserDashboardInfo](user-dashboard.md#userdashboardinfo) |  |
| [**update**](user-dashboard.md#update)|   [UpdateUserDashboardRequest](user-dashboard.md#updateuserdashboardrequest) |   [UserDashboardInfo](user-dashboard.md#userdashboardinfo) |  |
| [**delete**](user-dashboard.md#delete)|   [UserDashboardRequest](user-dashboard.md#userdashboardrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](user-dashboard.md#get)|   [GetUserDashboardRequest](user-dashboard.md#getuserdashboardrequest) |   [UserDashboardInfo](user-dashboard.md#userdashboardinfo) |  |
| [**list**](user-dashboard.md#list)|   [UserDashboardQuery](user-dashboard.md#userdashboardquery) |   [UserDashboardsInfo](user-dashboard.md#userdashboardsinfo) |  |
| [**stat**](user-dashboard.md#stat)|   [UserDashboardStatQuery](user-dashboard.md#userdashboardstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](user-dashboard.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateUserDashboardRequest](user-dashboard.md#createuserdashboardrequest)  </div> | <div style="width:200px; text-align:center;">   [UserDashboardInfo](user-dashboard.md#userdashboardinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](user-dashboard.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateUserDashboardRequest](user-dashboard.md#updateuserdashboardrequest)  </div> | <div style="width:200px; text-align:center;">   [UserDashboardInfo](user-dashboard.md#userdashboardinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](user-dashboard.md#delete) </div> | <div style="width:200px; text-align:center;">    [UserDashboardRequest](user-dashboard.md#userdashboardrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](user-dashboard.md#get) </div> | <div style="width:200px; text-align:center;">    [GetUserDashboardRequest](user-dashboard.md#getuserdashboardrequest)  </div> | <div style="width:200px; text-align:center;">   [UserDashboardInfo](user-dashboard.md#userdashboardinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](user-dashboard.md#list) </div> | <div style="width:200px; text-align:center;">    [UserDashboardQuery](user-dashboard.md#userdashboardquery)  </div> | <div style="width:200px; text-align:center;">   [UserDashboardsInfo](user-dashboard.md#userdashboardsinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](user-dashboard.md#stat) </div> | <div style="width:200px; text-align:center;">    [UserDashboardStatQuery](user-dashboard.md#userdashboardstatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
### create
> **POST** /cost-analysis/v1/user-dashboards
>


| Type | Message |
| :--- | :--- |
| Request | [CreateUserDashboardRequest](user-dashboard.md#createuserdashboardrequest) |
| Response |  [UserDashboardInfo](user-dashboard.md#userdashboardinfo)  |
 
 

 
### update
> **PUT** /cost-analysis/v1/user-dashboard/{user_dashboard_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateUserDashboardRequest](user-dashboard.md#updateuserdashboardrequest) |
| Response |  [UserDashboardInfo](user-dashboard.md#userdashboardinfo)  |
 
 

 
### delete
> **DELETE** /cost-analysis/v1/user-dashboard/{user_dashboard_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UserDashboardRequest](user-dashboard.md#userdashboardrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /cost-analysis/v1/user-dashboard/{user_dashboard_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetUserDashboardRequest](user-dashboard.md#getuserdashboardrequest) |
| Response |  [UserDashboardInfo](user-dashboard.md#userdashboardinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v1/user-dashboards
>
> **POST** /cost-analysis/v1/user-dashboards/search



| Type | Message |
| :--- | :--- |
| Request | [UserDashboardQuery](user-dashboard.md#userdashboardquery) |
| Response |  [UserDashboardsInfo](user-dashboard.md#userdashboardsinfo)  |
 
 

 
### stat
> **POST** /cost-analysis/v1/user-dashboards/stat
>


| Type | Message |
| :--- | :--- |
| Request | [UserDashboardStatQuery](user-dashboard.md#userdashboardstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateUserDashboardRequest
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
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">default_layout_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">custom_layouts</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">default_filter</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">period_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>AUTO</li>
          	<li>FIXED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">period</td>
      <td style="text-align:left"><a href="user-dashboard.md#userdashboardperiod">UserDashboardPeriod</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
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



### GetUserDashboardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_dashboard_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### UpdateUserDashboardRequest
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
      <td style="text-align:left">user_dashboard_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">default_layout_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">custom_layouts</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">default_filter</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">period_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>AUTO</li>
          	<li>FIXED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">period</td>
      <td style="text-align:left"><a href="user-dashboard.md#userdashboardperiod">UserDashboardPeriod</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
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



### UserDashboardInfo
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
      <td style="text-align:left">user_dashboard_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">default_layout_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">custom_layouts</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">default_filter</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">period_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>AUTO</li>
          	<li>FIXED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">period</td>
      <td style="text-align:left"><a href="user-dashboard.md#userdashboardperiod">UserDashboardPeriod</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">user_id</td>
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
  </tbody>
</table>



### UserDashboardPeriod
| Field | Type |  Description |
| :--- | :--- | :--- |
| start |string | |
| end |string | |

### UserDashboardQuery
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
      <td style="text-align:left">user_dashboard_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">period_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>AUTO</li>
          	<li>FIXED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">user_id</td>
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



### UserDashboardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_dashboard_id |string|✅| |
| domain_id |string|✅| |

### UserDashboardStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### UserDashboardsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of UserDashboardInfo](user-dashboard.md#userdashboardinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
