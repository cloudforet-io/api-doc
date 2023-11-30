---
title: "Role"
linkTitle: "Role"
weight: 3
bookFlatSection: true
---
# [Role](#Role)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Role





**Role Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Role#create) | [CreateRoleRequest](Role#createrolerequest) | [RoleInfo](Role#roleinfo) |
| [**update**](./Role#update) | [UpdateRoleRequest](Role#updaterolerequest) | [RoleInfo](Role#roleinfo) |
| [**delete**](./Role#delete) | [RoleRequest](Role#rolerequest) | [Empty](Role#empty) |
| [**get**](./Role#get) | [RoleRequest](Role#rolerequest) | [RoleInfo](Role#roleinfo) |
| [**list**](./Role#list) | [RoleSearchQuery](Role#rolesearchquery) | [RolesInfo](Role#rolesinfo) |
| [**stat**](./Role#stat) | [RoleStatQuery](Role#rolestatquery) | [Struct](Role#struct) |



    
<br>

### create





> **POST** /identity/v2/role/create
>






    
<br>

### update





> **POST** /identity/v2/role/update
>






    
<br>

### delete





> **POST** /identity/v2/role/delete
>






    
<br>

### get





> **POST** /identity/v2/role/get
>






    
<br>

### list





> **POST** /identity/v2/role/list
>






    
<br>

### stat





> **POST** /identity/v2/role/stat
>






    


<br>
<br>

## Message



### CreateRoleRequest
* **name** (string)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **api_permissions** (string)  `Repeated`   

    
* **page_permissions** (PagePermission)  `Repeated`   

    
* **tags** (Struct)  

    <br>

### PagePermission
* **page** (string)   `Required` 

    
* **permission** (Permission)   `Required` 

    <br>

### RoleInfo
* **role_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **api_permissions** (string)  `Repeated`    `Required` 

    
* **page_permissions** (PagePermission)  `Repeated`    `Required` 

    
* **tags** (Struct)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### RoleRequest
* **role_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### RoleSearchQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **role_id** (string)  

    
* **name** (string)  

    
* **role_type** (RoleType)  

    <br>

### RoleStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### RolesInfo
* **results** (RoleInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateRoleRequest
* **role_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **api_permissions** (string)  `Repeated`   

    
* **page_permissions** (PagePermission)  `Repeated`   

    
* **tags** (Struct)  

    <br>
