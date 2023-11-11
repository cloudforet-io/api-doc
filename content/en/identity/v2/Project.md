---
title: "Project"
linkTitle: "Project"
weight: 3
bookFlatSection: true
---
# [Project](#Project)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Project





**Project Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Project#create) | [CreateProjectRequest](Project#createprojectrequest) | [ProjectInfo](Project#projectinfo) |
| [**update**](./Project#update) | [UpdateProjectRequest](Project#updateprojectrequest) | [ProjectInfo](Project#projectinfo) |
| [**update_project_type**](./Project#update_project_type) | [UpdateProjectTypeRequest](Project#updateprojecttyperequest) | [ProjectInfo](Project#projectinfo) |
| [**change_project_group**](./Project#change_project_group) | [ChangeProjectGroupRequest](Project#changeprojectgrouprequest) | [ProjectInfo](Project#projectinfo) |
| [**delete**](./Project#delete) | [ProjectRequest](Project#projectrequest) | [Empty](Project#empty) |
| [**add_users**](./Project#add_users) | [UsersProjectRequest](Project#usersprojectrequest) | [ProjectInfo](Project#projectinfo) |
| [**remove_users**](./Project#remove_users) | [UsersProjectRequest](Project#usersprojectrequest) | [ProjectInfo](Project#projectinfo) |
| [**add_user_groups**](./Project#add_user_groups) | [UserGroupsProjectRequest](Project#usergroupsprojectrequest) | [ProjectInfo](Project#projectinfo) |
| [**remove_user_groups**](./Project#remove_user_groups) | [UserGroupsProjectRequest](Project#usergroupsprojectrequest) | [ProjectInfo](Project#projectinfo) |
| [**get**](./Project#get) | [ProjectRequest](Project#projectrequest) | [ProjectInfo](Project#projectinfo) |
| [**list**](./Project#list) | [ProjectSearchQuery](Project#projectsearchquery) | [ProjectsInfo](Project#projectsinfo) |
| [**stat**](./Project#stat) | [ProjectStatQuery](Project#projectstatquery) | [Struct](Project#struct) |



    
<br>

### create





> **POST** /identity/v2/project/create
>






    
<br>

### update





> **POST** /identity/v2/project/update
>






    
<br>

### update_project_type





> **POST** /identity/v2/project/update-project-type
>






    
<br>

### change_project_group





> **POST** /identity/v2/project/change-project-group
>






    
<br>

### delete





> **POST** /identity/v2/project/delete
>






    
<br>

### add_users





> **POST** /identity/v2/project/add-users
>






    
<br>

### remove_users





> **POST** /identity/v2/project/remove-users
>






    
<br>

### add_user_groups





> **POST** /identity/v2/project/add-user-groups
>






    
<br>

### remove_user_groups





> **POST** /identity/v2/project/remove-user-groups
>






    
<br>

### get





> **POST** /identity/v2/project/get
>






    
<br>

### list





> **POST** /identity/v2/project/list
>






    
<br>

### stat





> **POST** /identity/v2/project/stat
>






    


<br>
<br>

## Message



### ChangeProjectGroupRequest
* **project_id** (string)   `Required` 

    
* **project_group_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    <br>

### CreateProjectRequest
* **name** (string)   `Required` 

    
* **project** (ProjectType)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_group_id** (string)  

    
* **tags** (Struct)  

    <br>

### ProjectInfo
* **project_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **project_type** (ProjectType)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **users** (string)  `Repeated`    `Required` 

    
* **user_groups** (string)  `Repeated`    `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_group_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### ProjectRequest
* **project_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    <br>

### ProjectSearchQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **project_id** (string)  

    
* **name** (string)  

    
* **workspace_id** (string)  

    
* **project_group_id** (string)  

    
* **user_group_id** (string)  

    
* **user_id** (string)  

    <br>

### ProjectStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    <br>

### ProjectsInfo
* **results** (ProjectInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateProjectRequest
* **project_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>

### UpdateProjectTypeRequest
* **project_id** (string)   `Required` 

    
* **project** (ProjectType)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    <br>

### UserGroupsProjectRequest
* **project_id** (string)   `Required` 

    
* **user_groups** (string)  `Repeated`    `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    <br>

### UsersProjectRequest
* **project_id** (string)   `Required` 

    
* **users** (string)  `Repeated`    `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    <br>
