---
title: "Variable"
linkTitle: "Variable"
weight: 3
bookFlatSection: true
---
# [Variable](#Variable)



>  **Package : spaceone.api.opsflow.v1**

<br>
<br>

## Variable





**Variable Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Variable#create) | [VariableCreateRequest](Variable#variablecreaterequest) | [VariableInfo](Variable#variableinfo) |
| [**update**](./Variable#update) | [VariableUpdateRequest](Variable#variableupdaterequest) | [VariableInfo](Variable#variableinfo) |
| [**delete**](./Variable#delete) | [VariableRequest](Variable#variablerequest) | [Empty](Variable#empty) |
| [**get**](./Variable#get) | [VariableRequest](Variable#variablerequest) | [VariableInfo](Variable#variableinfo) |
| [**list**](./Variable#list) | [VariableSearchQuery](Variable#variablesearchquery) | [VariablesInfo](Variable#variablesinfo) |
| [**stat**](./Variable#stat) | [VariableStatQuery](Variable#variablestatquery) | [Struct](Variable#struct) |



    
<br>

### create





> **POST** /opsflow/v1/variable/create
>






    
<br>

### update





> **POST** /opsflow/v1/variable/update
>






    
<br>

### delete





> **POST** /opsflow/v1/variable/delete
>






    
<br>

### get





> **POST** /opsflow/v1/variable/get
>






    
<br>

### list





> **POST** /opsflow/v1/variable/list
>






    
<br>

### stat





> **POST** /opsflow/v1/variable/stat
>






    


<br>
<br>

## Message



### VariableCreateRequest
* **name** (string)   `Required` 

    
* **value** (string)   `Required` 

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    <br>

### VariableInfo
* **name** (string)   `Required` 

    
* **value** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### VariableRequest
* **name** (string)   `Required` 

    <br>

### VariableSearchQuery
* **query** (Query)  

    
* **name** (string)  

    
* **workspace_id** (string)  

    <br>

### VariableStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### VariableUpdateRequest
* **name** (string)   `Required` 

    
* **value** (string)  

    
* **tags** (Struct)  

    <br>

### VariablesInfo
* **results** (VariableInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
