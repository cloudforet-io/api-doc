---
title: "Job"
linkTitle: "Job"
weight: 3
bookFlatSection: true
---
# [Job](#Job)



>  **Package : spaceone.api.inventory.plugin**

<br>
<br>

## Job





**Job Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**get_tasks**](./Job#get_tasks) | [GetTaskRequest](Job#gettaskrequest) | [TasksInfo](Job#tasksinfo) |



    
<br>

### get_tasks










    


<br>
<br>

## Message



### GetTaskRequest
* **secret_data** (Struct)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **task_filter** (TaskFilter)   `Required` 

    <br>

### TaskFilter
* **providers** (string)  `Repeated`    `Required` 

    
* **cloud_service_groups** (string)  `Repeated`    `Required` 

    
* **cloud_service_types** (string)  `Repeated`    `Required` 

    
* **region_codes** (string)  `Repeated`    `Required` 

    
* **resources** (string)  `Repeated`    `Required` 

    <br>

### TaskInfo
* **task_options** (Struct)   `Required` 

    <br>

### TasksInfo
* **tasks** (TaskInfo)  `Repeated`    `Required` 

    <br>
