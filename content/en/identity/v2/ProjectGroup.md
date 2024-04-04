---
title: "ProjectGroup"
linkTitle: "ProjectGroup"
weight: 3
bookFlatSection: true
---
# [ProjectGroup](#ProjectGroup)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## ProjectGroup





**ProjectGroup Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./ProjectGroup#create) | [CreateProjectGroupRequest](ProjectGroup#createprojectgrouprequest) | [ProjectGroupInfo](ProjectGroup#projectgroupinfo) |
| [**update**](./ProjectGroup#update) | [UpdateProjectGroupRequest](ProjectGroup#updateprojectgrouprequest) | [ProjectGroupInfo](ProjectGroup#projectgroupinfo) |
| [**change_parent_group**](./ProjectGroup#change_parent_group) | [ChangeParentGroupRequest](ProjectGroup#changeparentgrouprequest) | [ProjectGroupInfo](ProjectGroup#projectgroupinfo) |
| [**delete**](./ProjectGroup#delete) | [ProjectGroupRequest](ProjectGroup#projectgrouprequest) | [Empty](ProjectGroup#empty) |
| [**add_users**](./ProjectGroup#add_users) | [UsersProjectGroupRequest](ProjectGroup#usersprojectgrouprequest) | [ProjectGroupInfo](ProjectGroup#projectgroupinfo) |
| [**remove_users**](./ProjectGroup#remove_users) | [UsersProjectGroupRequest](ProjectGroup#usersprojectgrouprequest) | [ProjectGroupInfo](ProjectGroup#projectgroupinfo) |
| [**get**](./ProjectGroup#get) | [ProjectGroupRequest](ProjectGroup#projectgrouprequest) | [ProjectGroupInfo](ProjectGroup#projectgroupinfo) |
| [**list**](./ProjectGroup#list) | [ProjectGroupSearchQuery](ProjectGroup#projectgroupsearchquery) | [ProjectGroupsInfo](ProjectGroup#projectgroupsinfo) |
| [**stat**](./ProjectGroup#stat) | [ProjectGroupStatQuery](ProjectGroup#projectgroupstatquery) | [Struct](ProjectGroup#struct) |



    
<br>

### create





> **POST** /identity/v2/project-group/create
>






    
<br>

### update





> **POST** /identity/v2/project-group/update
>






    
<br>

### change_parent_group





> **POST** /identity/v2/project-group/change-parent-group
>






    
<br>

### delete





> **POST** /identity/v2/project-group/delete
>






    
<br>

### add_users





> **POST** /identity/v2/project-group/add-users
>






    
<br>

### remove_users





> **POST** /identity/v2/project-group/remove-users
>






    
<br>

### get





> **POST** /identity/v2/project-group/get
>






    
<br>

### list





> **POST** /identity/v2/project-group/list
>






    
<br>

### stat





> **POST** /identity/v2/project-group/stat
>






    


<br>
<br>

## Message



### ChangeParentGroupRequest
* **project_group_id** (string)   `Required` 

    
* **parent_group_id** (string)   `Required` 

    <br>

### CreateProjectGroupRequest
* **name** (string)   `Required` 

    
* **tags** (Struct)  

    
* **parent_group_id** (string)  

    <br>

### ProjectGroupInfo
* **project_group_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **users** (string)  `Repeated`    `Required` 

    
* **reference_id** (string)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **parent_group_id** (string)   `Required` 

    
* **trusted_account_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_synced_at** (string)   `Required` 

    <br>

### ProjectGroupRequest
* **project_group_id** (string)   `Required` 

    <br>

### ProjectGroupSearchQuery
* **query** (Query)  

    
* **project_group_id** (string)  

    
* **name** (string)  

    
* **workspace_id** (string)  

    
* **parent_group_id** (string)  

    <br>

### ProjectGroupStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### ProjectGroupsInfo
* **results** (ProjectGroupInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateProjectGroupRequest
* **project_group_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>

### UsersProjectGroupRequest
* **project_group_id** (string)   `Required` 

    
* **users** (string)  `Repeated`    `Required` 

    <br>
