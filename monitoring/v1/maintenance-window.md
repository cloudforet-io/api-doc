---
description: A MaintenanceWindow is a resource snoozing Alerts during maintenance time.
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

> Creates a new MaintenanceWindow. When creating a MaintenanceWindow, you can set the title and maintenance schedule of the MaintenanceWindow. From the `start_time` to the `end_time` specified by the schedule set in this method, alerts in the Projects linked with the MaintenanceWindow are ceased.

| Type | Message |
| :--- | :--- |
| Request | [CreateMaintenanceWindowRequest](maintenance-window.md#createmaintenancewindowrequest) |
| Response |  [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "title": "The dev server is under regular maintenance.",
    "projects": [
        "project-123456789012"
    ],
    "start_time": "2022-01-01T09:45:00.000Z",
    "end_time": "2022-01-01T10:45:00.000Z",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "maintenance_window_id": "mw-123456789012",
    "title": "The dev server is under regular maintenance.",
    "state": "OPEN",
    "start_time": "2022-01-01T09:45:00.000Z",
    "end_time": "2022-01-01T10:45:00.000Z",
    "tags": {},
    "projects": [
        "project-123456789012"
    ],
    "domain_id": "domain-123456789012",
    "created_by": "user1@email.com",
    "created_at": "2022-06-02T09:46:49.196Z",
    "updated_at": "2022-06-02T09:46:49.196Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /monitoring/v1/maintenance-window/{maintenance_window_id}
>

> Updates a specific MaintenanceWindow. You can make changes in MaintenanceWindow settings including, the `title` and the schedule.

| Type | Message |
| :--- | :--- |
| Request | [UpdateMaintenanceWindowRequest](maintenance-window.md#updatemaintenancewindowrequest) |
| Response |  [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "maintenance_window_id": "mw-123456789012",
    "title": "The dev server is under regular maintenance.",
    "projects": [
        "project-123456789012"
    ],
    "start_time": "2022-01-03T00:00:00.000Z",
    "end_time": "2022-01-03T01:00:00.000Z",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "maintenance_window_id": "mw-123456789012",
    "title": "The dev server is under regular maintenance.",
    "state": "OPEN",
    "start_time": "2022-06-03T00:00:00.000Z",
    "end_time": "2022-06-03T01:00:00.000Z",
    "tags": {},
    "projects": [
        "project-123456789012"
    ],
    "domain_id": "domain-123456789012",
    "created_by": "user1@email.com",
    "created_at": "2022-01-02T09:46:49.196Z",
    "updated_at": "2022-01-02T09:46:49.196Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### close
> **PUT** /monitoring/v1/maintenance-window/{maintenance_window_id}/close
>

> Closes a MaintenanceWindow by changing the state of the MaintenanceWindow to `CLOSED` when the maintenance is completed. As the MaintenanceWindow is not deleted but closed, the maintenance history remains undeleted.

| Type | Message |
| :--- | :--- |
| Request | [MaintenanceWindowRequest](maintenance-window.md#maintenancewindowrequest) |
| Response |  [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "maintenance_window_id": "mw-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "maintenance_window_id": "mw-123456789012",
    "title": "The dev server is under regular maintenance.",
    "state": "CLOSED",
    "start_time": "2022-06-03T00:00:00.000Z",
    "end_time": "2022-06-03T01:00:00.000Z",
    "tags": {},
    "projects": [
        "project-123456789012"
    ],
    "domain_id": "domain-123456789012",
    "created_by": "user1@email.com",
    "created_at": "2022-01-02T09:46:49.196Z",
    "updated_at": "2022-01-02T09:46:49.196Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /monitoring/v1/maintenance-window/{maintenance_window_id}
>

> Gets a specific MaintenanceWindow. Prints detailed information about the MaintenanceWindow, including the title and the schedule.

| Type | Message |
| :--- | :--- |
| Request | [GetMaintenanceWindowRequest](maintenance-window.md#getmaintenancewindowrequest) |
| Response |  [MaintenanceWindowInfo](maintenance-window.md#maintenancewindowinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "maintenance_window_id": "mw-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "maintenance_window_id": "mw-123456789012",
    "title": "The dev server is under regular maintenance.",
    "state": "OPEN",
    "start_time": "2022-06-03T00:00:00.000Z",
    "end_time": "2022-06-03T01:00:00.000Z",
    "tags": {},
    "projects": [
        "project-123456789012"
    ],
    "domain_id": "domain-123456789012",
    "created_by": "user1@email.com",
    "created_at": "2022-01-02T09:46:49.196Z",
    "updated_at": "2022-01-02T09:46:49.196Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /monitoring/v1/maintenance-windows
>
> **POST** /monitoring/v1/maintenance-windows/search


> Gets a list of all MaintenanceWindows. You can use a query to get a filtered list of MaintenanceWindows.

| Type | Message |
| :--- | :--- |
| Request | [MaintenanceWindowQuery](maintenance-window.md#maintenancewindowquery) |
| Response |  [MaintenanceWindowsInfo](maintenance-window.md#maintenancewindowsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {},
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "maintenance_window_id": "mw-123456789012",
            "title": "The dev server is under regular maintenance.",
            "state": "OPEN",
            "start_time": "2022-06-03T00:00:00.000Z",
            "end_time": "2022-06-03T01:00:00.000Z",
            "tags": {},
            "projects": [
                "project-123456789012"
            ],
            "domain_id": "domain-123456789012",
            "created_by": "user1@email.com",
            "created_at": "2022-01-01T09:59:01.966Z",
            "updated_at": "2022-01-01T09:59:01.966Z"
        },
        {
            "maintenance_window_id": "mw-987654321098",
            "title": "The prd server is under regular maintenance.",
            "state": "OPEN",
            "start_time": "2022-06-03T00:00:00.000Z",
            "end_time": "2022-06-03T01:00:00.000Z",
            "tags": {},
            "projects": [
                "project-123456789012"
            ],
            "domain_id": "domain-123456789012",
            "created_by": "user2@email.com",
            "created_at": "2022-01-02T09:57:28.999Z",
            "updated_at": "2022-01-02T09:57:28.999Z"
        }
    ],
    "total_count": 50
}
```
{% endtab %}
{% endtabs %}
 
 

 
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
