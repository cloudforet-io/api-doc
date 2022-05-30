---
description:  
---
# Maintenance window

>  **Package : spaceone.api.monitoring.v1**

## MaintenanceWindow

{% hint style="info" %}
**MaintenanceWindow Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](maintenance-window.md#create)|   [CreateMaintenanceWindowRequest](maintenance-window.md#createmaintenancewindowrequest) |   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo) |  |
| [**update**](maintenance-window.md#update)|   [UpdateMaintenanceWindowRequest](maintenance-window.md#updatemaintenancewindowrequest) |   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo) |  |
| [**close**](maintenance-window.md#close)|   [MaintenanceWindowRequest](maintenance-window.md#maintenancewindowrequest) |   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo) |  |
| [**get**](maintenance-window.md#get)|   [GetMaintenanceWindowRequest](maintenance-window.md#getmaintenancewindowrequest) |   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo) |  |
| [**list**](maintenance-window.md#list)|   [MaintenanceWindowQuery](maintenance-window.md#maintenancewindowquery) |   [MaintenanceWindowsInfo](maintenance-window.md#maintenancewindowsinfo) |  |
| [**stat**](maintenance-window.md#stat)|   [MaintenanceWindowStatQuery](maintenance-window.md#maintenancewindowstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](maintenance-window.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateMaintenanceWindowRequest](maintenance-window.md#createmaintenancewindowrequest)  </div> | <div style="width:200px; text-align:center;">   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](maintenance-window.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateMaintenanceWindowRequest](maintenance-window.md#updatemaintenancewindowrequest)  </div> | <div style="width:200px; text-align:center;">   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**close**](maintenance-window.md#close) </div> | <div style="width:200px; text-align:center;">    [MaintenanceWindowRequest](maintenance-window.md#maintenancewindowrequest)  </div> | <div style="width:200px; text-align:center;">   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](maintenance-window.md#get) </div> | <div style="width:200px; text-align:center;">    [GetMaintenanceWindowRequest](maintenance-window.md#getmaintenancewindowrequest)  </div> | <div style="width:200px; text-align:center;">   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](maintenance-window.md#list) </div> | <div style="width:200px; text-align:center;">    [MaintenanceWindowQuery](maintenance-window.md#maintenancewindowquery)  </div> | <div style="width:200px; text-align:center;">   [MaintenanceWindowsInfo](maintenance-window.md#maintenancewindowsinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](maintenance-window.md#stat) </div> | <div style="width:200px; text-align:center;">    [MaintenanceWindowStatQuery](maintenance-window.md#maintenancewindowstatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
### create
> **POST** /monitoring/v1/maintenance-windows
>


| Type | Message |
| :--- | :--- |
| Request | [CreateMaintenanceWindowRequest](maintenance-window.md#createmaintenancewindowrequest) |
| Response |  [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo)  |
 
 

 
### update
> **PUT** /monitoring/v1/maintenance-window/{maintenance_window_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateMaintenanceWindowRequest](maintenance-window.md#updatemaintenancewindowrequest) |
| Response |  [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo)  |
 
 

 
### close
> **PUT** /monitoring/v1/maintenance-window/{maintenance_window_id}/close
>


| Type | Message |
| :--- | :--- |
| Request | [MaintenanceWindowRequest](maintenance-window.md#maintenancewindowrequest) |
| Response |  [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo)  |
 
 

 
### get
> **GET** /monitoring/v1/maintenance-window/{maintenance_window_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetMaintenanceWindowRequest](maintenance-window.md#getmaintenancewindowrequest) |
| Response |  [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo)  |
 
 

 
### list
> **GET** /monitoring/v1/maintenance-windows
>
> **POST** /monitoring/v1/maintenance-windows/search



| Type | Message |
| :--- | :--- |
| Request | [MaintenanceWindowQuery](maintenance-window.md#maintenancewindowquery) |
| Response |  [MaintenanceWindowsInfo](maintenance-window.md#maintenancewindowsinfo)  |
 
 

 
### stat
> **POST** /monitoring/v1/maintenance-windows/stat
>


| Type | Message |
| :--- | :--- |
| Request | [MaintenanceWindowStatQuery](maintenance-window.md#maintenancewindowstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateMaintenanceWindowRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| title |string|✅| |
| projects |list of string|✅| |
| start_time |string|✅| |
| end_time |string|✅| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### GetMaintenanceWindowRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| maintenance_window_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### MaintenanceWindowInfo
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
      <td style="text-align:left">maintenance_window_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>OPEN</li>
          	<li>CLOSED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">start_time</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">end_time</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">projects</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">created_by</td>
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
      <td style="text-align:left">closed_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### MaintenanceWindowQuery
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
      <td style="text-align:left">maintenance_window_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>OPEN</li>
          	<li>CLOSED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">created_by</td>
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



### MaintenanceWindowRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| maintenance_window_id |string|✅| |
| domain_id |string|✅| |

### MaintenanceWindowStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### MaintenanceWindowsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateMaintenanceWindowRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| maintenance_window_id |string|✅| |
| title |string|❌| |
| projects |list of string|❌| |
| start_time |string|❌| |
| end_time |string|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
