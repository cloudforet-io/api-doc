---
description:  
---
# Public dashboard

>  **Package : spaceone.api.cost_analysis.v1**

## PublicDashboard

{% hint style="info" %}
**PublicDashboard Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](public-dashboard.md#create)|   [CreatePublicDashboardRequest](public-dashboard.md#createpublicdashboardrequest) |   [PublicDashboardInfo](public-dashboard.md#publicdashboardinfo) |  |
| [**update**](public-dashboard.md#update)|   [UpdatePublicDashboardRequest](public-dashboard.md#updatepublicdashboardrequest) |   [PublicDashboardInfo](public-dashboard.md#publicdashboardinfo) |  |
| [**delete**](public-dashboard.md#delete)|   [PublicDashboardRequest](public-dashboard.md#publicdashboardrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](public-dashboard.md#get)|   [GetPublicDashboardRequest](public-dashboard.md#getpublicdashboardrequest) |   [PublicDashboardInfo](public-dashboard.md#publicdashboardinfo) |  |
| [**list**](public-dashboard.md#list)|   [PublicDashboardQuery](public-dashboard.md#publicdashboardquery) |   [PublicDashboardsInfo](public-dashboard.md#publicdashboardsinfo) |  |
| [**stat**](public-dashboard.md#stat)|   [PublicDashboardStatQuery](public-dashboard.md#publicdashboardstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](public-dashboard.md#create) </div> | <div style="width:200px; text-align:center;">    [CreatePublicDashboardRequest](public-dashboard.md#createpublicdashboardrequest)  </div> | <div style="width:200px; text-align:center;">   [PublicDashboardInfo](public-dashboard.md#publicdashboardinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](public-dashboard.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdatePublicDashboardRequest](public-dashboard.md#updatepublicdashboardrequest)  </div> | <div style="width:200px; text-align:center;">   [PublicDashboardInfo](public-dashboard.md#publicdashboardinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](public-dashboard.md#delete) </div> | <div style="width:200px; text-align:center;">    [PublicDashboardRequest](public-dashboard.md#publicdashboardrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](public-dashboard.md#get) </div> | <div style="width:200px; text-align:center;">    [GetPublicDashboardRequest](public-dashboard.md#getpublicdashboardrequest)  </div> | <div style="width:200px; text-align:center;">   [PublicDashboardInfo](public-dashboard.md#publicdashboardinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](public-dashboard.md#list) </div> | <div style="width:200px; text-align:center;">    [PublicDashboardQuery](public-dashboard.md#publicdashboardquery)  </div> | <div style="width:200px; text-align:center;">   [PublicDashboardsInfo](public-dashboard.md#publicdashboardsinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](public-dashboard.md#stat) </div> | <div style="width:200px; text-align:center;">    [PublicDashboardStatQuery](public-dashboard.md#publicdashboardstatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
### create
> **POST** /cost-analysis/v1/public-dashboards
>


| Type | Message |
| :--- | :--- |
| Request | [CreatePublicDashboardRequest](public-dashboard.md#createpublicdashboardrequest) |
| Response |  [PublicDashboardInfo](public-dashboard.md#publicdashboardinfo)  |
 
 

 
### update
> **PUT** /cost-analysis/v1/public-dashboard/{public_dashboard_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdatePublicDashboardRequest](public-dashboard.md#updatepublicdashboardrequest) |
| Response |  [PublicDashboardInfo](public-dashboard.md#publicdashboardinfo)  |
 
 

 
### delete
> **DELETE** /cost-analysis/v1/public-dashboard/{public_dashboard_id}
>


| Type | Message |
| :--- | :--- |
| Request | [PublicDashboardRequest](public-dashboard.md#publicdashboardrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /cost-analysis/v1/public-dashboard/{public_dashboard_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetPublicDashboardRequest](public-dashboard.md#getpublicdashboardrequest) |
| Response |  [PublicDashboardInfo](public-dashboard.md#publicdashboardinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v1/public-dashboards
>
> **POST** /cost-analysis/v1/public-dashboards/search



| Type | Message |
| :--- | :--- |
| Request | [PublicDashboardQuery](public-dashboard.md#publicdashboardquery) |
| Response |  [PublicDashboardsInfo](public-dashboard.md#publicdashboardsinfo)  |
 
 

 
### stat
> **POST** /cost-analysis/v1/public-dashboards/stat
>


| Type | Message |
| :--- | :--- |
| Request | [PublicDashboardStatQuery](public-dashboard.md#publicdashboardstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreatePublicDashboardRequest
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
      <td style="text-align:left"><a href="public-dashboard.md#publicdashboardperiod">PublicDashboardPeriod</a></td>
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



### GetPublicDashboardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| public_dashboard_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### PublicDashboardInfo
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
      <td style="text-align:left">public_dashboard_id</td>
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
      <td style="text-align:left"><a href="public-dashboard.md#publicdashboardperiod">PublicDashboardPeriod</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
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



### PublicDashboardPeriod
| Field | Type |  Description |
| :--- | :--- | :--- |
| start |string | |
| end |string | |

### PublicDashboardQuery
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
      <td style="text-align:left">public_dashboard_id</td>
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
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### PublicDashboardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| public_dashboard_id |string|✅| |
| domain_id |string|✅| |

### PublicDashboardStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### PublicDashboardsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of PublicDashboardInfo](public-dashboard.md#publicdashboardinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdatePublicDashboardRequest
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
      <td style="text-align:left">public_dashboard_id</td>
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
      <td style="text-align:left"><a href="public-dashboard.md#publicdashboardperiod">PublicDashboardPeriod</a></td>
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


