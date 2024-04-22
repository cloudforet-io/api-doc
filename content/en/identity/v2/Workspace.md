---
title: "Workspace"
linkTitle: "Workspace"
weight: 3
bookFlatSection: true
---
# [Workspace](#Workspace)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Workspace





**Workspace Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Workspace#create) | [CreateWorkSpaceRequest](Workspace#createworkspacerequest) | [WorkspaceInfo](Workspace#workspaceinfo) |
| [**update**](./Workspace#update) | [UpdateWorkSpaceRequest](Workspace#updateworkspacerequest) | [WorkspaceInfo](Workspace#workspaceinfo) |
| [**delete**](./Workspace#delete) | [WorkspaceDeleteRequest](Workspace#workspacedeleterequest) | [Empty](Workspace#empty) |
| [**enable**](./Workspace#enable) | [WorkspaceRequest](Workspace#workspacerequest) | [WorkspaceInfo](Workspace#workspaceinfo) |
| [**disable**](./Workspace#disable) | [WorkspaceRequest](Workspace#workspacerequest) | [WorkspaceInfo](Workspace#workspaceinfo) |
| [**get**](./Workspace#get) | [WorkspaceRequest](Workspace#workspacerequest) | [WorkspaceInfo](Workspace#workspaceinfo) |
| [**check**](./Workspace#check) | [WorkspaceCheckRequest](Workspace#workspacecheckrequest) | [Empty](Workspace#empty) |
| [**list**](./Workspace#list) | [WorkspaceSearchQuery](Workspace#workspacesearchquery) | [WorkspacesInfo](Workspace#workspacesinfo) |
| [**stat**](./Workspace#stat) | [WorkspaceStatQuery](Workspace#workspacestatquery) | [Struct](Workspace#struct) |



    
<br>

### create





> **POST** /identity/v2/workspace/create
>






    
<br>

### update





> **POST** /identity/v2/workspace/update
>






    
<br>

### delete





> **POST** /identity/v2/workspace/delete
>






    
<br>

### enable





> **POST** /identity/v2/workspace/enable
>






    
<br>

### disable





> **POST** /identity/v2/workspace/disable
>






    
<br>

### get





> **POST** /identity/v2/workspace/get
>






    
<br>

### check










    
<br>

### list





> **POST** /identity/v2/workspace/list
>






    
<br>

### stat





> **POST** /identity/v2/workspace/stat
>






    


<br>
<br>

## Message



### CreateWorkSpaceRequest
* **name** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    <br>

### UpdateWorkSpaceRequest
* **workspace_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>

### WorkspaceCheckRequest
* **workspace_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### WorkspaceDeleteRequest
* **workspace_id** (string)   `Required` 

    
* **force** (bool)   `Required` 

    <br>

### WorkspaceInfo
* **workspace_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **created_by** (string)   `Required` 

    
* **references** (string)  `Repeated`    `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **trusted_account_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_synced_at** (string)   `Required` 

    <br>

### WorkspaceRequest
* **workspace_id** (string)   `Required` 

    <br>

### WorkspaceSearchQuery
* **query** (Query)  

    
* **workspace_id** (string)  

    
* **name** (string)  

    
* **created_by** (string)  

    <br>

### WorkspaceStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### WorkspacesInfo
* **results** (WorkspaceInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
