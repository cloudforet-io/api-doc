---
description:  
---
# Maintenance window

>  **Package : spaceone.api.monitoring.v1**

## MaintenanceWindow

{% hint style="info" %}
**MaintenanceWindow Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](maintenance-window.md#create)|   [CreateMaintenanceWindowRequest](maintenance-window.md#createmaintenancewindowrequest) |   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo) |
| [**update**](maintenance-window.md#update)|   [UpdateMaintenanceWindowRequest](maintenance-window.md#updatemaintenancewindowrequest) |   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo) |
| [**close**](maintenance-window.md#close)|   [MaintenanceWindowRequest](maintenance-window.md#maintenancewindowrequest) |   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo) |
| [**get**](maintenance-window.md#get)|   [GetMaintenanceWindowRequest](maintenance-window.md#getmaintenancewindowrequest) |   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo) |
| [**list**](maintenance-window.md#list)|   [MaintenanceWindowQuery](maintenance-window.md#maintenancewindowquery) |   [MaintenanceWindowsInfo](maintenance-window.md#maintenancewindowsinfo) |
| [**stat**](maintenance-window.md#stat)|   [MaintenanceWindowStatQuery](maintenance-window.md#maintenancewindowstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
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
| title |string|✔| |
| projects |list of string|✔| |
| start_time |string|✔| |
| end_time |string|✔| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### GetMaintenanceWindowRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| maintenance_window_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### MaintenanceWindowInfo
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
      <td style="text-align:left; width:100px;">maintenance_window_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>OPEN</li>
          	<li>CLOSED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">start_time</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">end_time</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">projects</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_by</td>
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
      <td style="text-align:left; width:100px;">closed_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### MaintenanceWindowQuery
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
      <td style="text-align:left; width:100px;">maintenance_window_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>OPEN</li>
          	<li>CLOSED</li>
        </ul></td>
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
      <td style="text-align:left; width:100px;">created_by</td>
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



### MaintenanceWindowRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| maintenance_window_id |string|✔| |
| domain_id |string|✔| |

### MaintenanceWindowStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### MaintenanceWindowsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateMaintenanceWindowRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| maintenance_window_id |string|✔| |
| title |string|✘| |
| projects |list of string|✘| |
| start_time |string|✘| |
| end_time |string|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
