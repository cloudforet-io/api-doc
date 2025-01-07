---
title: "Task"
linkTitle: "Task"
weight: 3
bookFlatSection: true
---
# [Task](#Task)



>  **Package : spaceone.api.opsflow.v1**

<br>
<br>

## Task





**Task Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Task#create) | [TaskCreateRequest](Task#taskcreaterequest) | [TaskInfo](Task#taskinfo) |
| [**update**](./Task#update) | [TaskUpdateRequest](Task#taskupdaterequest) | [TaskInfo](Task#taskinfo) |
| [**update_description**](./Task#update_description) | [TaskUpdateDescriptionRequest](Task#taskupdatedescriptionrequest) | [TaskInfo](Task#taskinfo) |
| [**change_assignee**](./Task#change_assignee) | [TaskChangeAssigneeRequest](Task#taskchangeassigneerequest) | [TaskInfo](Task#taskinfo) |
| [**change_status**](./Task#change_status) | [TaskChangeStatusRequest](Task#taskchangestatusrequest) | [TaskInfo](Task#taskinfo) |
| [**delete**](./Task#delete) | [TaskRequest](Task#taskrequest) | [Empty](Task#empty) |
| [**get**](./Task#get) | [TaskRequest](Task#taskrequest) | [TaskInfo](Task#taskinfo) |
| [**list**](./Task#list) | [TaskSearchQuery](Task#tasksearchquery) | [TasksInfo](Task#tasksinfo) |
| [**stat**](./Task#stat) | [TaskStatQuery](Task#taskstatquery) | [Struct](Task#struct) |



    
<br>

### create





> **POST** /opsflow/v1/task/create
>






    
<br>

### update





> **POST** /opsflow/v1/task/update
>






    
<br>

### update_description





> **POST** /opsflow/v1/task/update_description
>






    
<br>

### change_assignee





> **POST** /opsflow/v1/task/change_assignee
>






    
<br>

### change_status





> **POST** /opsflow/v1/task/change_status
>






    
<br>

### delete





> **POST** /opsflow/v1/task/delete
>






    
<br>

### get





> **POST** /opsflow/v1/task/get
>






    
<br>

### list





> **POST** /opsflow/v1/task/list
>






    
<br>

### stat





> **POST** /opsflow/v1/task/stat
>






    


<br>
<br>

## Message



### TaskChangeAssigneeRequest
* **task_id** (string)   `Required` 

    
* **assignee** (string)   `Required` 

    <br>

### TaskChangeStatusRequest
* **task_id** (string)   `Required` 

    
* **status_id** (string)   `Required` 

    
* **assignee** (string)  

    <br>

### TaskCreateRequest
* **name** (string)   `Required` 

    
* **status_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **task_type_id** (string)   `Required` 

    
* **priority** (TaskPriority)  

    
* **description** (string)  

    
* **files** (string)  `Repeated`   

    
* **mentions** (Mentions)  

    
* **assignee** (string)  

    
* **data** (Struct)  

    
* **reference_id** (string)  

    <br>

### TaskInfo
* **task_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **status_id** (string)   `Required` 

    
* **status_type** (string)   `Required` 

    
* **priority** (TaskPriority)   `Required` 

    
* **description** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **files** (FileInfo)  `Repeated`    `Required` 

    
* **assignee** (string)   `Required` 

    
* **created_by** (string)   `Required` 

    
* **reference_id** (string)   `Required` 

    
* **related_assets** (string)  `Repeated`    `Required` 

    
* **contents_type** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **category_id** (string)   `Required` 

    
* **task_type_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **started_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    
* **completed_at** (string)   `Required` 

    
* **started_duration** (int64)   `Required` 

    
* **in_progress_duration** (int64)   `Required` 

    
* **completed_duration** (int64)   `Required` 

    <br>

### TaskRequest
* **task_id** (string)   `Required` 

    <br>

### TaskSearchQuery
* **query** (Query)  

    
* **task_id** (string)  

    
* **name** (string)  

    
* **status_id** (string)  

    
* **status_type** (string)  

    
* **priority** (TaskPriority)  

    
* **assignee** (string)  

    
* **related_asset_id** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    
* **category_id** (string)  

    
* **task_type_id** (string)  

    <br>

### TaskStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### TaskUpdateDescriptionRequest
* **task_id** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **files** (string)  `Repeated`    `Required` 

    
* **mentions** (Mentions)   `Required` 

    <br>

### TaskUpdateRequest
* **task_id** (string)   `Required` 

    
* **name** (string)  

    
* **priority** (TaskPriority)  

    
* **data** (Struct)  

    
* **project_id** (string)  

    <br>

### TasksInfo
* **results** (TaskInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
