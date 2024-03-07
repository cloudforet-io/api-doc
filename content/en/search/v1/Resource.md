---
title: "Resource"
linkTitle: "Resource"
weight: 3
bookFlatSection: true
---
# [Resource](#Resource)



>  **Package : spaceone.api.search.v1**

<br>
<br>

## Resource





**Resource Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**search**](./Resource#search) | [SearchResourceRequest](Resource#searchresourcerequest) | [ResourcesInfo](Resource#resourcesinfo) |



    
<br>

### search





> **POST** /search/v1/resource/search
>






    


<br>
<br>

## Message



### ResourceInfo
* **resource_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    <br>

### ResourcesInfo
* **results** (ResourceInfo)  `Repeated`    `Required` 

    
* **next_token** (string)   `Required` 

    <br>

### SearchResourceRequest
* **resource_type** (string)   `Required` 

  *identity.ServiceAccount*

    
* **keyword** (string)  

    
* **limit** (int32)  

  *Result limit is default 15 and max 100*

    
* **workspaces** (string)  `Repeated`   

  *List of workspace_id to search, limit of workspaces is 5*

    
* **all_workspaces** (bool)  

  *If true, search all workspaces that user has access*

    
* **next_token** (string)  

  *If you request with next_token, it will return next result.
resource_type must be same with previous request.*

    <br>
