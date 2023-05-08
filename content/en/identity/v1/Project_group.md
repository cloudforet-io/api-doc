---
title: "Project_group"
linkTitle: "Project_group"
weight: 3
bookFlatSection: true
---
# [Project_group](#Project_group)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## Project_group


**ProjectGroup Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./ProjectGroup#create) | [CreateProjectGroupRequest](ProjectGroup#createprojectgrouprequest) | [ProjectGroupInfo](./ProjectGroup#projectgroupinfo) |
| [**update**](./ProjectGroup#update) | [UpdateProjectGroupRequest](ProjectGroup#updateprojectgrouprequest) | [ProjectGroupInfo](./ProjectGroup#projectgroupinfo) |
| [**delete**](./ProjectGroup#delete) | [ProjectGroupRequest](ProjectGroup#projectgrouprequest) | [Empty](./ProjectGroup#empty) |
| [**get**](./ProjectGroup#get) | [GetProjectGroupRequest](ProjectGroup#getprojectgrouprequest) | [ProjectGroupInfo](./ProjectGroup#projectgroupinfo) |
| [**list**](./ProjectGroup#list) | [ProjectGroupQuery](ProjectGroup#projectgroupquery) | [ProjectGroupsInfo](./ProjectGroup#projectgroupsinfo) |
| [**stat**](./ProjectGroup#stat) | [ProjectGroupStatQuery](ProjectGroup#projectgroupstatquery) | [Struct](./ProjectGroup#struct) |
| [**add_member**](./ProjectGroup#add_member) | [AddProjectGroupMemberRequest](ProjectGroup#addprojectgroupmemberrequest) | [ProjectGroupRoleBindingInfo](./ProjectGroup#projectgrouprolebindinginfo) |
| [**modify_member**](./ProjectGroup#modify_member) | [ModifyProjectGroupMemberRequest](ProjectGroup#modifyprojectgroupmemberrequest) | [ProjectGroupRoleBindingInfo](./ProjectGroup#projectgrouprolebindinginfo) |
| [**remove_member**](./ProjectGroup#remove_member) | [RemoveProjectGroupMemberRequest](ProjectGroup#removeprojectgroupmemberrequest) | [Empty](./ProjectGroup#empty) |
| [**list_members**](./ProjectGroup#list_members) | [ProjectGroupMemberQuery](ProjectGroup#projectgroupmemberquery) | [ProjectGroupRoleBindingsInfo](./ProjectGroup#projectgrouprolebindingsinfo) |
| [**list_projects**](./ProjectGroup#list_projects) | [ProjectGroupProjectQuery](ProjectGroup#projectgroupprojectquery) | [ProjectGroupProjectsInfo](./ProjectGroup#projectgroupprojectsinfo) |



    
<br>

### create

> **POST** /identity/v1/project-group/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **PUT** /identity/v1/project-group/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /identity/v1/project-group/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /identity/v1/project-group/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /identity/v1/project-group/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /identity/v1/project-group/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    
<br>

### add_member

> **POST** /identity/v1/project-group/add-member
>




 {{< tabs " add_member " >}}




{{< /tabs >}}

    
<br>

### modify_member

> **POST** /identity/v1/project-group/modify-member
>




 {{< tabs " modify_member " >}}




{{< /tabs >}}

    
<br>

### remove_member

> **POST** /identity/v1/project-group/remove-member
>




 {{< tabs " remove_member " >}}




{{< /tabs >}}

    
<br>

### list_members

> **POST** /identity/v1/project-group/list-members
>




 {{< tabs " list_members " >}}




{{< /tabs >}}

    
<br>

### list_projects

> **POST** /identity/v1/project-group/list-projects
>




 {{< tabs " list_projects " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### AddProjectGroupMemberRequest
* **project_group_id** (string)  `Required` 

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

### CreateProjectGroupRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **parent_project_group_id** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetProjectGroupRequest
* **project_group_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### ModifyProjectGroupMemberRequest
* **project_group_id** (string)  `Required` 

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

### ProjectGroupInfo
* **project_group_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **parent_project_group_info** (ProjectGroupInfo)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_by** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### ProjectGroupMemberQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **project_group_id** (string)  `Required` 

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

### ProjectGroupProjectInfo
* **project_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **project_group_info** (ProjectGroupInfo)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_by** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### ProjectGroupProjectQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **project_group_id** (string)  `Required` 

  *is_required: true*

    
* **recursive** (bool)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProjectGroupProjectsInfo
* **results** (ProjectGroupProjectInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### ProjectGroupQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **project_group_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **parent_project_group_id** (string)  `Required` 

  *is_required: false*

    
* **author_within** (bool)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProjectGroupRequest
* **project_group_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProjectGroupRoleBindingInfo
* **role_binding_id** (string)  `Required` 

    
* **resource_type** (string)  `Required` 

    
* **resource_id** (string)  `Required` 

    
* **role_info** (RoleInfo)  `Required` 

    
* **project_group_info** (ProjectGroupInfo)  `Required` 

    
* **labels** (ListValue)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### ProjectGroupRoleBindingsInfo
* **results** (ProjectGroupRoleBindingInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### ProjectGroupStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProjectGroupsInfo
* **results** (ProjectGroupInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### RemoveProjectGroupMemberRequest
* **project_group_id** (string)  `Required` 

  *is_required: true*

    
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateProjectGroupRequest
* **project_group_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **parent_project_group_id** (string)  `Required` 

  *is_required: false*

    
* **release_parent_project_group** (bool)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
