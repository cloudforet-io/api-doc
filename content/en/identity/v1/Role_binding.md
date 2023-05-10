---
title: "Role_binding"
linkTitle: "Role_binding"
weight: 3
bookFlatSection: true
---
# [Role_binding](#Role_binding)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## Role_binding





**RoleBinding Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./RoleBinding#create) | [CreateRoleBindingRequest](RoleBinding#createrolebindingrequest) | [RoleBindingInfo](./RoleBinding#rolebindinginfo) |
| [**update**](./RoleBinding#update) | [UpdateRoleBindingRequest](RoleBinding#updaterolebindingrequest) | [RoleBindingInfo](./RoleBinding#rolebindinginfo) |
| [**delete**](./RoleBinding#delete) | [RoleBindingRequest](RoleBinding#rolebindingrequest) | [Empty](./RoleBinding#empty) |
| [**get**](./RoleBinding#get) | [GetRoleBindingRequest](RoleBinding#getrolebindingrequest) | [RoleBindingInfo](./RoleBinding#rolebindinginfo) |
| [**list**](./RoleBinding#list) | [RoleBindingQuery](RoleBinding#rolebindingquery) | [RoleBindingsInfo](./RoleBinding#rolebindingsinfo) |
| [**stat**](./RoleBinding#stat) | [RoleBindingStatQuery](RoleBinding#rolebindingstatquery) | [Struct](./RoleBinding#struct) |



    
<br>

### create





> **POST** /identity/v1/role-binding/create
>






    
<br>

### update





> **POST** /identity/v1/role-binding/update
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
* **resource_type** (string)  `Required` 

    
* **resource_id** (string)  `Required` 

    
* **role_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **project_id** (string) 

    
* **project_group_id** (string) 

    
* **labels** (ListValue) 

    
* **tags** (Struct) 

    <br>

### GetRoleBindingRequest
* **role_binding_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>

### RoleBindingInfo
* **role_binding_id** (string)  `Required` 

    
* **resource_type** (string)  `Required` 

    
* **resource_id** (string)  `Required` 

    
* **role_info** (RoleInfo)  `Required` 

    
* **project_info** (ProjectInfo)  `Required` 

    
* **project_group_info** (ProjectGroupInfo)  `Required` 

    
* **labels** (ListValue)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### RoleBindingQuery
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **role_binding_id** (string) 

    
* **resource_type** (string) 

    
* **resource_id** (string) 

    
* **role_id** (string) 

    
* **role_type** (string) 

    
* **project_id** (string) 

    
* **project_group_id** (string) 

    <br>

### RoleBindingRequest
* **role_binding_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### RoleBindingStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### RoleBindingsInfo
* **results** (RoleBindingInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateRoleBindingRequest
* **role_binding_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **labels** (ListValue) 

    
* **tags** (Struct) 

    <br>
