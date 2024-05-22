---
title: "WorkspaceConfig"
linkTitle: "WorkspaceConfig"
weight: 3
bookFlatSection: true
---
# [WorkspaceConfig](#WorkspaceConfig)
DomainConfig API which configure environments for domain


>  **Package : spaceone.api.config.v1**

<br>
<br>

## WorkspaceConfig





**WorkspaceConfig Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./WorkspaceConfig#create) | [CreateWorkspaceConfigRequest](WorkspaceConfig#createworkspaceconfigrequest) | [WorkspaceConfigInfo](WorkspaceConfig#workspaceconfiginfo) |
| [**update**](./WorkspaceConfig#update) | [CreateWorkspaceConfigRequest](WorkspaceConfig#createworkspaceconfigrequest) | [WorkspaceConfigInfo](WorkspaceConfig#workspaceconfiginfo) |
| [**set**](./WorkspaceConfig#set) | [CreateWorkspaceConfigRequest](WorkspaceConfig#createworkspaceconfigrequest) | [WorkspaceConfigInfo](WorkspaceConfig#workspaceconfiginfo) |
| [**delete**](./WorkspaceConfig#delete) | [WorkspaceConfigRequest](WorkspaceConfig#workspaceconfigrequest) | [Empty](WorkspaceConfig#empty) |
| [**get**](./WorkspaceConfig#get) | [WorkspaceConfigRequest](WorkspaceConfig#workspaceconfigrequest) | [WorkspaceConfigInfo](WorkspaceConfig#workspaceconfiginfo) |
| [**list**](./WorkspaceConfig#list) | [WorkspaceConfigSearchQuery](WorkspaceConfig#workspaceconfigsearchquery) | [WorkspaceConfigsInfo](WorkspaceConfig#workspaceconfigsinfo) |
| [**stat**](./WorkspaceConfig#stat) | [WorkspaceConfigStatQuery](WorkspaceConfig#workspaceconfigstatquery) | [Struct](WorkspaceConfig#struct) |



    
<br>

### create





> **POST** /config/v1/workspace-config/create
>






    
<br>

### update





> **POST** /config/v1/workspace-config/update
>






    
<br>

### set





> **POST** /config/v1/workspace-config/set
>






    
<br>

### delete





> **POST** /config/v1/workspace-config/delete
>






    
<br>

### get





> **POST** /config/v1/workspace-config/get
>






    
<br>

### list





> **POST** /config/v1/workspace-config/list
>






    
<br>

### stat





> **POST** /config/v1/workspace-config/stat
>






    


<br>
<br>

## Message



### CreateWorkspaceConfigRequest
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **tags** (Struct)  

    <br>

### UpdateWorkspaceConfigRequest
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **tags** (Struct)  

    <br>

### WorkspaceConfigInfo
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### WorkspaceConfigRequest
* **name** (string)   `Required` 

    <br>

### WorkspaceConfigSearchQuery
* **query** (Query)  

    
* **name** (string)  

    <br>

### WorkspaceConfigStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### WorkspaceConfigsInfo
* **results** (WorkspaceConfigInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
