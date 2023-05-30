---
title: "Project"
linkTitle: "Project"
weight: 3
bookFlatSection: true
---
# [Project](#Project)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## Project





**Project Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Project#create) | [CreateProjectRequest](Project#createprojectrequest) | [ProjectInfo](Project#projectinfo) |
| [**update**](./Project#update) | [UpdateProjectRequest](Project#updateprojectrequest) | [ProjectInfo](Project#projectinfo) |
| [**delete**](./Project#delete) | [ProjectRequest](Project#projectrequest) | [Empty](Project#empty) |
| [**get**](./Project#get) | [GetProjectRequest](Project#getprojectrequest) | [ProjectInfo](Project#projectinfo) |
| [**list**](./Project#list) | [ProjectQuery](Project#projectquery) | [ProjectsInfo](Project#projectsinfo) |
| [**stat**](./Project#stat) | [ProjectStatQuery](Project#projectstatquery) | [Struct](Project#struct) |
| [**add_member**](./Project#add_member) | [AddProjectMemberRequest](Project#addprojectmemberrequest) | [ProjectRoleBindingInfo](Project#projectrolebindinginfo) |
| [**modify_member**](./Project#modify_member) | [ModifyProjectMemberRequest](Project#modifyprojectmemberrequest) | [ProjectRoleBindingInfo](Project#projectrolebindinginfo) |
| [**remove_member**](./Project#remove_member) | [RemoveProjectMemberRequest](Project#removeprojectmemberrequest) | [Empty](Project#empty) |
| [**list_members**](./Project#list_members) | [ProjectMemberQuery](Project#projectmemberquery) | [ProjectRoleBindingsInfo](Project#projectrolebindingsinfo) |



    
<br>

### create





> **POST** /identity/v1/project/create
>






    
<br>

### update





> **POST** /identity/v1/project/update
>






    
<br>

### delete





> **POST** /identity/v1/project/delete
>






    
<br>

### get





> **POST** /identity/v1/project/get
>






    
<br>

### list





> **POST** /identity/v1/project/list
>






    
<br>

### stat





> **POST** /identity/v1/project/stat
>






    
<br>

### add_member





> **POST** /identity/v1/project/add-member
>






    
<br>

### modify_member





> **POST** /identity/v1/project/modify-member
>






    
<br>

### remove_member





> **POST** /identity/v1/project/remove-member
>






    
<br>

### list_members





> **POST** /identity/v1/project/list-members
>






    


<br>
<br>

## Message



### AddProjectMemberRequest
* **project_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **role_id** (string)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    
* **is_external_user** (bool)  

    <br>

### CreateProjectRequest
* **name** (string)   `Required` 

    
* **project_group_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **tags** (Struct)  

    <br>

### GetProjectRequest
* **project_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### ModifyProjectMemberRequest
* **project_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>

### ProjectInfo
* **project_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **project_group_info** (ProjectGroupInfo)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_by** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### ProjectMemberQuery
* **project_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **user_id** (string)  

    
* **role_id** (string)  

    
* **include_parent_member** (bool)  

    <br>

### ProjectQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **project_id** (string)  

    
* **name** (string)  

    
* **project_group_id** (string)  

    
* **user_id** (string)  

    <br>

### ProjectRequest
* **project_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### ProjectRoleBindingInfo
* **role_binding_id** (string)   `Required` 

    
* **resource_type** (string)   `Required` 

    
* **resource_id** (string)   `Required` 

    
* **role_info** (RoleInfo)   `Required` 

    
* **project_info** (ProjectInfo)   `Required` 

    
* **project_group_info** (ProjectGroupInfo)   `Required` 

    
* **labels** (ListValue)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### ProjectRoleBindingsInfo
* **results** (ProjectRoleBindingInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### ProjectStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### ProjectsInfo
* **results** (ProjectInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### RemoveProjectMemberRequest
* **project_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### UpdateProjectRequest
* **project_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **project_group_id** (string)  

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>
