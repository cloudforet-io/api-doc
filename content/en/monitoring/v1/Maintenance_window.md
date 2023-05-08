---
title: "Maintenance_window"
linkTitle: "Maintenance_window"
weight: 3
bookFlatSection: true
---
# [Maintenance_window](#Maintenance_window)
desc: A MaintenanceWindow is a resource snoozing Alerts during maintenance time.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## Maintenance_window


**MaintenanceWindow Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./MaintenanceWindow#create) | [CreateMaintenanceWindowRequest](MaintenanceWindow#createmaintenancewindowrequest) | [MaintenanceWindowInfo](./MaintenanceWindow#maintenancewindowinfo) |
| [**update**](./MaintenanceWindow#update) | [UpdateMaintenanceWindowRequest](MaintenanceWindow#updatemaintenancewindowrequest) | [MaintenanceWindowInfo](./MaintenanceWindow#maintenancewindowinfo) |
| [**close**](./MaintenanceWindow#close) | [MaintenanceWindowRequest](MaintenanceWindow#maintenancewindowrequest) | [MaintenanceWindowInfo](./MaintenanceWindow#maintenancewindowinfo) |
| [**get**](./MaintenanceWindow#get) | [GetMaintenanceWindowRequest](MaintenanceWindow#getmaintenancewindowrequest) | [MaintenanceWindowInfo](./MaintenanceWindow#maintenancewindowinfo) |
| [**list**](./MaintenanceWindow#list) | [MaintenanceWindowQuery](MaintenanceWindow#maintenancewindowquery) | [MaintenanceWindowsInfo](./MaintenanceWindow#maintenancewindowsinfo) |
| [**stat**](./MaintenanceWindow#stat) | [MaintenanceWindowStatQuery](MaintenanceWindow#maintenancewindowstatquery) | [Struct](./MaintenanceWindow#struct) |



    
<br>

### create

> **POST** /monitoring/v1/maintenance-window/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /monitoring/v1/maintenance-window/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### close

> **POST** /monitoring/v1/maintenance-window/close
>




 {{< tabs " close " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /monitoring/v1/maintenance-window/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /monitoring/v1/maintenance-window/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /monitoring/v1/maintenance-window/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateMaintenanceWindowRequest
* **title** (string)  `Required` 

  *is_required: true*

    
* **projects** (string)  `Required` 

  *is_required: true*

    
* **start_time** (string)  `Required` 

  *is_required: true*

    
* **end_time** (string)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetMaintenanceWindowRequest
* **maintenance_window_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### MaintenanceWindowInfo
* **maintenance_window_id** (string)  `Required` 

    
* **title** (string)  `Required` 

    
* **state** (MaintenanceWindowState)  `Required` 

    
* **start_time** (string)  `Required` 

    
* **end_time** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **projects** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_by** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    
* **closed_at** (string)  `Required` 

    <br>

### MaintenanceWindowQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **maintenance_window_id** (string)  `Required` 

  *is_required: false*

    
* **title** (string)  `Required` 

  *is_required: false*

    
* **state** (MaintenanceWindowState)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **created_by** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### MaintenanceWindowRequest
* **maintenance_window_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### MaintenanceWindowStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### MaintenanceWindowsInfo
* **results** (MaintenanceWindowInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateMaintenanceWindowRequest
* **maintenance_window_id** (string)  `Required` 

  *is_required: true*

    
* **title** (string)  `Required` 

  *is_required: false*

    
* **projects** (string)  `Required` 

  *is_required: false*

    
* **start_time** (string)  `Required` 

  *is_required: false*

    
* **end_time** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
