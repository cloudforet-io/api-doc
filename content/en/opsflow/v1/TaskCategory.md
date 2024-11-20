---
title: "TaskCategory"
linkTitle: "TaskCategory"
weight: 3
bookFlatSection: true
---
# [TaskCategory](#TaskCategory)



>  **Package : spaceone.api.opsflow.v1**

<br>
<br>

## TaskCategory





**TaskCategory Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./TaskCategory#create) | [TaskCategoryCreateRequest](TaskCategory#taskcategorycreaterequest) | [TaskCategoryInfo](TaskCategory#taskcategoryinfo) |
| [**update**](./TaskCategory#update) | [TaskCategoryUpdateRequest](TaskCategory#taskcategoryupdaterequest) | [TaskCategoryInfo](TaskCategory#taskcategoryinfo) |
| [**delete**](./TaskCategory#delete) | [TaskCategoryRequest](TaskCategory#taskcategoryrequest) | [Empty](TaskCategory#empty) |
| [**get**](./TaskCategory#get) | [TaskCategoryRequest](TaskCategory#taskcategoryrequest) | [TaskCategoryInfo](TaskCategory#taskcategoryinfo) |
| [**list**](./TaskCategory#list) | [TaskCategorySearchQuery](TaskCategory#taskcategorysearchquery) | [TaskCategoriesInfo](TaskCategory#taskcategoriesinfo) |
| [**stat**](./TaskCategory#stat) | [TaskCategoryStatQuery](TaskCategory#taskcategorystatquery) | [Struct](TaskCategory#struct) |



    
<br>

### create





> **POST** /opsflow/v1/task-category/create
>






    
<br>

### update





> **POST** /opsflow/v1/task-category/update
>






    
<br>

### delete





> **POST** /opsflow/v1/task-category/delete
>






    
<br>

### get





> **POST** /opsflow/v1/task-category/get
>






    
<br>

### list





> **POST** /opsflow/v1/task-category/list
>






    
<br>

### stat





> **POST** /opsflow/v1/task-category/stat
>






    


<br>
<br>

## Message



### StatusOption
* **status_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **color** (string)   `Required` 

    
* **is_default** (bool)   `Required` 

    <br>

### StatusOptions
* **TODO** (StatusOption)  `Repeated`    `Required` 

    
* **IN_PROGRESS** (StatusOption)  `Repeated`    `Required` 

    
* **COMPLETED** (StatusOption)  `Repeated`    `Required` 

    <br>

### TaskCategoriesInfo
* **results** (TaskCategoryInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### TaskCategoryCreateRequest
* **name** (string)   `Required` 

    
* **status_options** (StatusOptions)   `Required` 

    
* **package_id** (string)   `Required` 

    
* **description** (string)  

    
* **fields** (TaskField)  `Repeated`   

    
* **tags** (Struct)  

    <br>

### TaskCategoryInfo
* **category_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **status_options** (StatusOptions)   `Required` 

    
* **fields** (TaskField)  `Repeated`    `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **package_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### TaskCategoryRequest
* **category_id** (string)   `Required` 

    <br>

### TaskCategorySearchQuery
* **query** (Query)  

    
* **category_id** (string)  

    
* **name** (string)  

    <br>

### TaskCategoryStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### TaskCategoryUpdateRequest
* **category_id** (string)   `Required` 

    
* **name** (string)  

    
* **description** (string)  

    
* **status_options** (StatusOptions)  

    
* **fields** (TaskField)  `Repeated`   

    
* **tags** (Struct)  

    
* **package_id** (string)  

    <br>

### TaskField
* **field_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **field_type** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **selection_type** (SelectionType)   `Required` 

    
* **is_required** (bool)   `Required` 

    
* **is_primary** (bool)   `Required` 

    <br>
