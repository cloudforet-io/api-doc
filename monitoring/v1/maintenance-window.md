---
description:  
---
# Maintenance window

>  **Package : spaceone.api.monitoring.v1**

## MaintenanceWindow

{% hint style="info" %}
**MaintenanceWindow Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](maintenance-window.md#create)|   [CreateMaintenanceWindowRequest](maintenance-window.md#createmaintenancewindowrequest) |   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo) |  |
| 2 | [**update**](maintenance-window.md#update)|   [UpdateMaintenanceWindowRequest](maintenance-window.md#updatemaintenancewindowrequest) |   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo) |  |
| 3 | [**close**](maintenance-window.md#close)|   [MaintenanceWindowRequest](maintenance-window.md#maintenancewindowrequest) |   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo) |  |
| 4 | [**get**](maintenance-window.md#get)|   [GetMaintenanceWindowRequest](maintenance-window.md#getmaintenancewindowrequest) |   [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo) |  |
| 5 | [**list**](maintenance-window.md#list)|   [MaintenanceWindowQuery](maintenance-window.md#maintenancewindowquery) |   [MaintenanceWindowsInfo](maintenance-window.md#maintenancewindowsinfo) |  |
| 6 | [**stat**](maintenance-window.md#stat)|   [MaintenanceWindowStatQuery](maintenance-window.md#maintenancewindowstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
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
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | title |string|✅| |
| 2 | projects |list of string|✅| |
| 3 | start |string|✅| |
| 4 | end |string|✅| |
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 6 | domain_id |string|✅| |

### GetMaintenanceWindowRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | maintenance_window_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### MaintenanceWindowInfo
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
      <td style="text-align:left">maintenance_window_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>OPEN</li>
          	<li>CLOSED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">start</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">end</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">projects</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
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
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">maintenance_window_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>OPEN</li>
          	<li>CLOSED</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### MaintenanceWindowRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | maintenance_window_id |string|✅| |
| 2 | domain_id |string|✅| |

### MaintenanceWindowStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### MaintenanceWindowsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateMaintenanceWindowRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | maintenance_window_id |string|✅| |
| 2 | title |string|❌| |
| 3 | projects |list of string|❌| |
| 4 | start |string|❌| |
| 5 | end |string|❌| |
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 7 | domain_id |string|✅| |
