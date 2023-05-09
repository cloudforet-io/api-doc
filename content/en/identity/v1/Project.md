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
| [**create**](./Project#create) | [CreateProjectRequest](Project#createprojectrequest) | [ProjectInfo](./Project#projectinfo) |
| [**update**](./Project#update) | [UpdateProjectRequest](Project#updateprojectrequest) | [ProjectInfo](./Project#projectinfo) |
| [**delete**](./Project#delete) | [ProjectRequest](Project#projectrequest) | [Empty](./Project#empty) |
| [**get**](./Project#get) | [GetProjectRequest](Project#getprojectrequest) | [ProjectInfo](./Project#projectinfo) |
| [**list**](./Project#list) | [ProjectQuery](Project#projectquery) | [ProjectsInfo](./Project#projectsinfo) |
| [**stat**](./Project#stat) | [ProjectStatQuery](Project#projectstatquery) | [Struct](./Project#struct) |
| [**add_member**](./Project#add_member) | [AddProjectMemberRequest](Project#addprojectmemberrequest) | [ProjectRoleBindingInfo](./Project#projectrolebindinginfo) |
| [**modify_member**](./Project#modify_member) | [ModifyProjectMemberRequest](Project#modifyprojectmemberrequest) | [ProjectRoleBindingInfo](./Project#projectrolebindinginfo) |
| [**remove_member**](./Project#remove_member) | [RemoveProjectMemberRequest](Project#removeprojectmemberrequest) | [Empty](./Project#empty) |
| [**list_members**](./Project#list_members) | [ProjectMemberQuery](Project#projectmemberquery) | [ProjectRoleBindingsInfo](./Project#projectrolebindingsinfo) |



    
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
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **role_id** (string)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **is_external_user** (bool)  `Required` 

  *is_required: false*

    <br>

### CreateProjectRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **project_group_id** (string)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetProjectRequest
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### ModifyProjectMemberRequest
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProjectInfo
* **project_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **project_group_info** (ProjectGroupInfo)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_by** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### ProjectMemberQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **user_id** (string)  `Required` 

  *is_required: false*

    
* **role_id** (string)  `Required` 

  *is_required: false*

    
* **include_parent_member** (bool)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProjectQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **project_group_id** (string)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProjectRequest
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProjectRoleBindingInfo
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

### ProjectRoleBindingsInfo
* **results** (ProjectRoleBindingInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### ProjectStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProjectsInfo
* **results** (ProjectInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### RemoveProjectMemberRequest
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateProjectRequest
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **project_group_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
