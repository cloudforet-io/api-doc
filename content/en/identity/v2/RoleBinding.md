---
title: "RoleBinding"
linkTitle: "RoleBinding"
weight: 3
bookFlatSection: true
---
# [RoleBinding](#RoleBinding)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## RoleBinding





**RoleBinding Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./RoleBinding#create) | [CreateRoleBindingRequest](RoleBinding#createrolebindingrequest) | [RoleBindingInfo](RoleBinding#rolebindinginfo) |
| [**update_role**](./RoleBinding#update_role) | [UpdateRoleBindingRequest](RoleBinding#updaterolebindingrequest) | [RoleBindingInfo](RoleBinding#rolebindinginfo) |
| [**delete**](./RoleBinding#delete) | [RoleBindingRequest](RoleBinding#rolebindingrequest) | [Empty](RoleBinding#empty) |
| [**get**](./RoleBinding#get) | [RoleBindingRequest](RoleBinding#rolebindingrequest) | [RoleBindingInfo](RoleBinding#rolebindinginfo) |
| [**list**](./RoleBinding#list) | [RoleBindingSearchQuery](RoleBinding#rolebindingsearchquery) | [RoleBindingsInfo](RoleBinding#rolebindingsinfo) |
| [**stat**](./RoleBinding#stat) | [RoleBindingStatQuery](RoleBinding#rolebindingstatquery) | [Struct](RoleBinding#struct) |



    
<br>

### create





> **POST** /identity/v1/role-binding/create
>






    
<br>

### update_role





> **POST** /identity/v1/role-binding/update-role
>






    
<br>

### delete





> **POST** /identity/v1/role-binding/delete
>






    
<br>

### get





> **POST** /identity/v1/role-binding/get
>






    
<br>

### list





> **POST** /identity/v1/role-binding/list
>






    
<br>

### stat





> **POST** /identity/v1/role-binding/stat
>






    


<br>
<br>

## Message



### CreateRoleBindingRequest
* **user_id** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **workspace_id** (string)  

    <br>

### RoleBindingInfo
* **role_binding_id** (string)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_group_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### RoleBindingRequest
* **role_binding_id** (string)   `Required` 

    <br>

### RoleBindingSearchQuery
* **query** (Query)  

    
* **role_binding_id** (string)  

    
* **role_type** (RoleType)  

    
* **workspace_id** (string)  

    
* **role_id** (string)  

    
* **user_id** (string)  

    <br>

### RoleBindingStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### RoleBindingsInfo
* **results** (RoleBindingInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateRoleBindingRequest
* **role_binding_id** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    <br>
