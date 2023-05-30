---
title: "Role"
linkTitle: "Role"
weight: 3
bookFlatSection: true
---
# [Role](#Role)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## Role





**Role Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Role#create) | [CreateRoleRequest](Role#createrolerequest) | [RoleInfo](Role#roleinfo) |
| [**update**](./Role#update) | [UpdateRoleRequest](Role#updaterolerequest) | [RoleInfo](Role#roleinfo) |
| [**delete**](./Role#delete) | [RoleRequest](Role#rolerequest) | [Empty](Role#empty) |
| [**get**](./Role#get) | [GetRoleRequest](Role#getrolerequest) | [RoleInfo](Role#roleinfo) |
| [**list**](./Role#list) | [RoleQuery](Role#rolequery) | [RolesInfo](Role#rolesinfo) |
| [**stat**](./Role#stat) | [RoleStatQuery](Role#rolestatquery) | [Struct](Role#struct) |



    
<br>

### create





> **POST** /identity/v1/role/create
>






    
<br>

### update





> **POST** /identity/v1/role/update
>






    
<br>

### delete





> **POST** /identity/v1/role/delete
>






    
<br>

### get





> **POST** /identity/v1/role/get
>






    
<br>

### list





> **POST** /identity/v1/role/list
>






    
<br>

### stat





> **POST** /identity/v1/role/stat
>






    


<br>
<br>

## Message



### CreateRoleRequest
* **name** (string)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **policies** (RolePolicy)  `Repeated`    `Required` 

    
* **domain_id** (string)   `Required` 

    
* **page_permissions** (PagePermission)  `Repeated`   

    
* **tags** (Struct)  

    <br>

### GetRoleRequest
* **role_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### PagePermission
* **page** (string)   `Required` 

    
* **permission** (Permission)   `Required` 

    <br>

### RoleInfo
* **role_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **policies** (RolePolicy)  `Repeated`    `Required` 

    
* **page_permissions** (PagePermission)  `Repeated`    `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **deleted_at** (string)   `Required` 

    <br>

### RolePolicy
* **policy_type** (PolicyType)   `Required` 

    
* **policy_id** (string)   `Required` 

    <br>

### RoleQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **role_id** (string)  

    
* **name** (string)  

    
* **role_type** (RoleType)  

    
* **policy_id** (string)  

    <br>

### RoleRequest
* **role_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

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

    
* **policies** (RolePolicy)  `Repeated`   

    
* **page_permissions** (PagePermission)  `Repeated`   

    
* **tags** (Struct)  

    
* **release_page_permissions** (bool)  

    <br>
