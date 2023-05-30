---
title: "MaintenanceWindow"
linkTitle: "MaintenanceWindow"
weight: 3
bookFlatSection: true
---
# [MaintenanceWindow](#MaintenanceWindow)
A MaintenanceWindow is a resource snoozing Alerts during maintenance time.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## MaintenanceWindow





**MaintenanceWindow Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./MaintenanceWindow#create) | [CreateMaintenanceWindowRequest](MaintenanceWindow#createmaintenancewindowrequest) | [MaintenanceWindowInfo](MaintenanceWindow#maintenancewindowinfo) |
| [**update**](./MaintenanceWindow#update) | [UpdateMaintenanceWindowRequest](MaintenanceWindow#updatemaintenancewindowrequest) | [MaintenanceWindowInfo](MaintenanceWindow#maintenancewindowinfo) |
| [**close**](./MaintenanceWindow#close) | [MaintenanceWindowRequest](MaintenanceWindow#maintenancewindowrequest) | [MaintenanceWindowInfo](MaintenanceWindow#maintenancewindowinfo) |
| [**get**](./MaintenanceWindow#get) | [GetMaintenanceWindowRequest](MaintenanceWindow#getmaintenancewindowrequest) | [MaintenanceWindowInfo](MaintenanceWindow#maintenancewindowinfo) |
| [**list**](./MaintenanceWindow#list) | [MaintenanceWindowQuery](MaintenanceWindow#maintenancewindowquery) | [MaintenanceWindowsInfo](MaintenanceWindow#maintenancewindowsinfo) |
| [**stat**](./MaintenanceWindow#stat) | [MaintenanceWindowStatQuery](MaintenanceWindow#maintenancewindowstatquery) | [Struct](MaintenanceWindow#struct) |



    
<br>

### create

Creates a new MaintenanceWindow. When creating a MaintenanceWindow, you can set the title and maintenance schedule of the MaintenanceWindow. From the `start_time` to the `end_time` specified by the schedule set in this method, alerts in the Projects linked with the MaintenanceWindow are ceased.



> **POST** /monitoring/v1/maintenance-window/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateMaintenanceWindowRequest](./MaintenanceWindow#createmaintenancewindowrequest)

* **title** (string)   `Required` 


* **projects** (string)  `Repeated`    `Required` 


* **start_time** (string)   `Required` 


* **end_time** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **tags** (Struct)  





{{< highlight json >}}
{
   "title": "The dev server is under regular maintenance.",
   "projects": ["project-123456789012"],
   "start_time": "2022-01-01T09:45:00.000Z",
   "end_time": "2022-01-01T10:45:00.000Z",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[MaintenanceWindowInfo](#MAINTENANCEWINDOWINFO)
* **maintenance_window_id** (string)   `Required` 

* **title** (string)   `Required` 

* **state** (MaintenanceWindowState)   `Required` 

* **start_time** (string)   `Required` 

* **end_time** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **projects** (string)  `Repeated`   `Required` 

* **domain_id** (string)   `Required` 

* **created_by** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **closed_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific MaintenanceWindow. You can make changes in MaintenanceWindow settings including, the `title` and the schedule.



> **POST** /monitoring/v1/maintenance-window/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateMaintenanceWindowRequest](./MaintenanceWindow#updatemaintenancewindowrequest)

* **maintenance_window_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **title** (string)  


* **projects** (string)  `Repeated`   


* **start_time** (string)  


* **end_time** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "maintenance_window_id": "mw-123456789012",
   "title": "The dev server is under regular maintenance.",
   "projects": ["project-123456789012"],
   "start_time": "2022-01-03T00:00:00.000Z",
   "end_time": "2022-01-03T01:00:00.000Z",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[MaintenanceWindowInfo](#MAINTENANCEWINDOWINFO)
* **maintenance_window_id** (string)   `Required` 

* **title** (string)   `Required` 

* **state** (MaintenanceWindowState)   `Required` 

* **start_time** (string)   `Required` 

* **end_time** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **projects** (string)  `Repeated`   `Required` 

* **domain_id** (string)   `Required` 

* **created_by** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **closed_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### close

Closes a MaintenanceWindow by changing the state of the MaintenanceWindow to `CLOSED` when the maintenance is completed. As the MaintenanceWindow is not deleted but closed, the maintenance history remains undeleted.



> **POST** /monitoring/v1/maintenance-window/close
>





 {{< tabs " close " >}}

 {{< tab "Request Example" >}}



[MaintenanceWindowRequest](./MaintenanceWindow#maintenancewindowrequest)

* **maintenance_window_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "maintenance_window_id": "mw-123456789012",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[MaintenanceWindowInfo](#MAINTENANCEWINDOWINFO)
* **maintenance_window_id** (string)   `Required` 

* **title** (string)   `Required` 

* **state** (MaintenanceWindowState)   `Required` 

* **start_time** (string)   `Required` 

* **end_time** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **projects** (string)  `Repeated`   `Required` 

* **domain_id** (string)   `Required` 

* **created_by** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **closed_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get

Gets a specific MaintenanceWindow. Prints detailed information about the MaintenanceWindow, including the title and the schedule.



> **POST** /monitoring/v1/maintenance-window/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetMaintenanceWindowRequest](./MaintenanceWindow#getmaintenancewindowrequest)

* **maintenance_window_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **only** (string)  `Repeated`   





{{< highlight json >}}
{
   "maintenance_window_id": "mw-123456789012",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[MaintenanceWindowInfo](#MAINTENANCEWINDOWINFO)
* **maintenance_window_id** (string)   `Required` 

* **title** (string)   `Required` 

* **state** (MaintenanceWindowState)   `Required` 

* **start_time** (string)   `Required` 

* **end_time** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **projects** (string)  `Repeated`   `Required` 

* **domain_id** (string)   `Required` 

* **created_by** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **closed_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all MaintenanceWindows. You can use a query to get a filtered list of MaintenanceWindows.



> **POST** /monitoring/v1/maintenance-window/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[MaintenanceWindowQuery](./MaintenanceWindow#maintenancewindowquery)

* **domain_id** (string)   `Required` 


* **query** (Query)  


* **maintenance_window_id** (string)  


* **title** (string)  


* **state** (MaintenanceWindowState)  


* **project_id** (string)  


* **created_by** (string)  





{{< highlight json >}}
{
   "query": {},
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[MaintenanceWindowsInfo](#MAINTENANCEWINDOWSINFO)
* **results** (MaintenanceWindowInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /monitoring/v1/maintenance-window/stat
>






    


<br>
<br>

## Message



### CreateMaintenanceWindowRequest
* **title** (string)   `Required` 

    
* **projects** (string)  `Repeated`    `Required` 

    
* **start_time** (string)   `Required` 

    
* **end_time** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **tags** (Struct)  

    <br>

### GetMaintenanceWindowRequest
* **maintenance_window_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### MaintenanceWindowInfo
* **maintenance_window_id** (string)   `Required` 

    
* **title** (string)   `Required` 

    
* **state** (MaintenanceWindowState)   `Required` 

    
* **start_time** (string)   `Required` 

    
* **end_time** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **projects** (string)  `Repeated`    `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_by** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    
* **closed_at** (string)   `Required` 

    <br>

### MaintenanceWindowQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **maintenance_window_id** (string)  

    
* **title** (string)  

    
* **state** (MaintenanceWindowState)  

    
* **project_id** (string)  

    
* **created_by** (string)  

    <br>

### MaintenanceWindowRequest
* **maintenance_window_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### MaintenanceWindowStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### MaintenanceWindowsInfo
* **results** (MaintenanceWindowInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateMaintenanceWindowRequest
* **maintenance_window_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **title** (string)  

    
* **projects** (string)  `Repeated`   

    
* **start_time** (string)  

    
* **end_time** (string)  

    
* **tags** (Struct)  

    <br>
