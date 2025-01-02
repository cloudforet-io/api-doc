---
title: "TaskType"
linkTitle: "TaskType"
weight: 3
bookFlatSection: true
---
# [TaskType](#TaskType)



>  **Package : spaceone.api.opsflow.v1**

<br>
<br>

## TaskType





**TaskType Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./TaskType#create) | [TaskTypeCreateRequest](TaskType#tasktypecreaterequest) | [TaskTypeInfo](TaskType#tasktypeinfo) |
| [**update**](./TaskType#update) | [TaskTypeUpdateRequest](TaskType#tasktypeupdaterequest) | [TaskTypeInfo](TaskType#tasktypeinfo) |
| [**update_fields**](./TaskType#update_fields) | [TaskTypeUpdateFieldsRequest](TaskType#tasktypeupdatefieldsrequest) | [TaskTypeInfo](TaskType#tasktypeinfo) |
| [**delete**](./TaskType#delete) | [TaskTypeDeleteRequest](TaskType#tasktypedeleterequest) | [Empty](TaskType#empty) |
| [**get**](./TaskType#get) | [TaskTypeRequest](TaskType#tasktyperequest) | [TaskTypeInfo](TaskType#tasktypeinfo) |
| [**list**](./TaskType#list) | [TaskTypeSearchQuery](TaskType#tasktypesearchquery) | [TaskTypesInfo](TaskType#tasktypesinfo) |
| [**stat**](./TaskType#stat) | [TaskTypeStatQuery](TaskType#tasktypestatquery) | [Struct](TaskType#struct) |



    
<br>

### create





> **POST** /opsflow/v1/task-type/create
>






    
<br>

### update





> **POST** /opsflow/v1/task-type/update
>






    
<br>

### update_fields





> **POST** /opsflow/v1/task-type/update_fields
>






    
<br>

### delete





> **POST** /opsflow/v1/task-type/delete
>






    
<br>

### get





> **POST** /opsflow/v1/task-type/get
>






    
<br>

### list





> **POST** /opsflow/v1/task-type/list
>






    
<br>

### stat





> **POST** /opsflow/v1/task-type/stat
>






    


<br>
<br>

## Message



### TaskTypeCreateRequest
* **name** (string)   `Required` 

    
* **category_id** (string)   `Required` 

    
* **description** (string)  

    
* **fields** (TaskField)  `Repeated`   

    
* **scope** (Scope)  

    
* **assignee_pool** (string)  `Repeated`   

    
* **vars** (Struct)  

    
* **tags** (Struct)  

    <br>

### TaskTypeDeleteRequest
* **task_type_id** (string)   `Required` 

    
* **new_task_type_id** (string)  

    <br>

### TaskTypeInfo
* **task_type_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **fields** (TaskField)  `Repeated`    `Required` 

    
* **scope** (Scope)   `Required` 

    
* **assignee_pool** (string)  `Repeated`    `Required` 

    
* **vars** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **category_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### TaskTypeRequest
* **task_type_id** (string)   `Required` 

    
* **include_category_fields** (bool)  

    <br>

### TaskTypeSearchQuery
* **query** (Query)  

    
* **task_type_id** (string)  

    
* **name** (string)  

    <br>

### TaskTypeStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### TaskTypeUpdateFieldsRequest
* **task_type_id** (string)   `Required` 

    
* **fields** (TaskField)  `Repeated`    `Required` 

    
* **force** (bool)   `Required` 

    <br>

### TaskTypeUpdateRequest
* **task_type_id** (string)   `Required` 

    
* **name** (string)  

    
* **description** (string)  

    
* **assignee_pool** (string)  `Repeated`   

    
* **vars** (Struct)  

    
* **tags** (Struct)  

    
* **category_id** (string)  

    <br>

### TaskTypesInfo
* **results** (TaskTypeInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
