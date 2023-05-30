---
title: "ProjectGroup"
linkTitle: "ProjectGroup"
weight: 3
bookFlatSection: true
---
# [ProjectGroup](#ProjectGroup)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## ProjectGroup





**ProjectGroup Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./ProjectGroup#create) | [CreateProjectGroupRequest](ProjectGroup#createprojectgrouprequest) | [ProjectGroupInfo](ProjectGroup#projectgroupinfo) |
| [**update**](./ProjectGroup#update) | [UpdateProjectGroupRequest](ProjectGroup#updateprojectgrouprequest) | [ProjectGroupInfo](ProjectGroup#projectgroupinfo) |
| [**delete**](./ProjectGroup#delete) | [ProjectGroupRequest](ProjectGroup#projectgrouprequest) | [Empty](ProjectGroup#empty) |
| [**get**](./ProjectGroup#get) | [GetProjectGroupRequest](ProjectGroup#getprojectgrouprequest) | [ProjectGroupInfo](ProjectGroup#projectgroupinfo) |
| [**list**](./ProjectGroup#list) | [ProjectGroupQuery](ProjectGroup#projectgroupquery) | [ProjectGroupsInfo](ProjectGroup#projectgroupsinfo) |
| [**stat**](./ProjectGroup#stat) | [ProjectGroupStatQuery](ProjectGroup#projectgroupstatquery) | [Struct](ProjectGroup#struct) |
| [**add_member**](./ProjectGroup#add_member) | [AddProjectGroupMemberRequest](ProjectGroup#addprojectgroupmemberrequest) | [ProjectGroupRoleBindingInfo](ProjectGroup#projectgrouprolebindinginfo) |
| [**modify_member**](./ProjectGroup#modify_member) | [ModifyProjectGroupMemberRequest](ProjectGroup#modifyprojectgroupmemberrequest) | [ProjectGroupRoleBindingInfo](ProjectGroup#projectgrouprolebindinginfo) |
| [**remove_member**](./ProjectGroup#remove_member) | [RemoveProjectGroupMemberRequest](ProjectGroup#removeprojectgroupmemberrequest) | [Empty](ProjectGroup#empty) |
| [**list_members**](./ProjectGroup#list_members) | [ProjectGroupMemberQuery](ProjectGroup#projectgroupmemberquery) | [ProjectGroupRoleBindingsInfo](ProjectGroup#projectgrouprolebindingsinfo) |
| [**list_projects**](./ProjectGroup#list_projects) | [ProjectGroupProjectQuery](ProjectGroup#projectgroupprojectquery) | [ProjectGroupProjectsInfo](ProjectGroup#projectgroupprojectsinfo) |



    
<br>

### create





> **POST** /identity/v1/project-group/create
>






    
<br>

### update





> **PUT** /identity/v1/project-group/update
>






    
<br>

### delete





> **POST** /identity/v1/project-group/delete
>






    
<br>

### get





> **POST** /identity/v1/project-group/get
>






    
<br>

### list





> **POST** /identity/v1/project-group/list
>






    
<br>

### stat





> **POST** /identity/v1/project-group/stat
>






    
<br>

### add_member





> **POST** /identity/v1/project-group/add-member
>






    
<br>

### modify_member





> **POST** /identity/v1/project-group/modify-member
>






    
<br>

### remove_member





> **POST** /identity/v1/project-group/remove-member
>






    
<br>

### list_members





> **POST** /identity/v1/project-group/list-members
>






    
<br>

### list_projects





> **POST** /identity/v1/project-group/list-projects
>






    


<br>
<br>

## Message



### AddProjectGroupMemberRequest
* **project_group_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **role_id** (string)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    
* **is_external_user** (bool)  

    <br>

### CreateProjectGroupRequest
* **name** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **parent_project_group_id** (string)  

    
* **tags** (Struct)  

    <br>

### GetProjectGroupRequest
* **project_group_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### ModifyProjectGroupMemberRequest
* **project_group_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>

### ProjectGroupInfo
* **project_group_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **parent_project_group_info** (ProjectGroupInfo)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_by** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### ProjectGroupMemberQuery
* **project_group_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **user_id** (string)  

    
* **role_id** (string)  

    
* **include_parent_member** (bool)  

    <br>

### ProjectGroupProjectInfo
* **project_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **project_group_info** (ProjectGroupInfo)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_by** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### ProjectGroupProjectQuery
* **project_group_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **recursive** (bool)  

    <br>

### ProjectGroupProjectsInfo
* **results** (ProjectGroupProjectInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### ProjectGroupQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **project_group_id** (string)  

    
* **name** (string)  

    
* **parent_project_group_id** (string)  

    
* **author_within** (bool)  

    <br>

### ProjectGroupRequest
* **project_group_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### ProjectGroupRoleBindingInfo
* **role_binding_id** (string)   `Required` 

    
* **resource_type** (string)   `Required` 

    
* **resource_id** (string)   `Required` 

    
* **role_info** (RoleInfo)   `Required` 

    
* **project_group_info** (ProjectGroupInfo)   `Required` 

    
* **labels** (ListValue)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### ProjectGroupRoleBindingsInfo
* **results** (ProjectGroupRoleBindingInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### ProjectGroupStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### ProjectGroupsInfo
* **results** (ProjectGroupInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### RemoveProjectGroupMemberRequest
* **project_group_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### UpdateProjectGroupRequest
* **project_group_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **parent_project_group_id** (string)  

    
* **release_parent_project_group** (bool)  

    
* **tags** (Struct)  

    <br>
