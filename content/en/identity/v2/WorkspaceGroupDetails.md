---
title: "WorkspaceGroupDetails"
linkTitle: "WorkspaceGroupDetails"
weight: 3
bookFlatSection: true
---
# [WorkspaceGroupDetails](#WorkspaceGroupDetails)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## WorkspaceGroupDetails





**WorkspaceGroupDetails Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**update**](./WorkspaceGroupDetails#update) | [UpdateWorkspaceGroupDetailsRequest](WorkspaceGroupDetails#updateworkspacegroupdetailsrequest) | [WorkspaceGroupDetailsInfo](WorkspaceGroupDetails#workspacegroupdetailsinfo) |
| [**delete**](./WorkspaceGroupDetails#delete) | [DeleteWorkspaceGroupDetailsRequest](WorkspaceGroupDetails#deleteworkspacegroupdetailsrequest) | [Empty](WorkspaceGroupDetails#empty) |
| [**add_workspaces**](./WorkspaceGroupDetails#add_workspaces) | [WorkspacesWorkspaceGroupDetailsRequest](WorkspaceGroupDetails#workspacesworkspacegroupdetailsrequest) | [WorkspaceGroupDetailsInfo](WorkspaceGroupDetails#workspacegroupdetailsinfo) |
| [**remove_workspaces**](./WorkspaceGroupDetails#remove_workspaces) | [WorkspacesWorkspaceGroupDetailsRequest](WorkspaceGroupDetails#workspacesworkspacegroupdetailsrequest) | [WorkspaceGroupDetailsInfo](WorkspaceGroupDetails#workspacegroupdetailsinfo) |
| [**find_users**](./WorkspaceGroupDetails#find_users) | [WorkspaceGroupDetailsFindRequest](WorkspaceGroupDetails#workspacegroupdetailsfindrequest) | [WorkspaceGroupDetailsUsersSummaryInfo](WorkspaceGroupDetails#workspacegroupdetailsuserssummaryinfo) |
| [**add_users**](./WorkspaceGroupDetails#add_users) | [AddUsersWorkspaceGroupDetailsRequest](WorkspaceGroupDetails#addusersworkspacegroupdetailsrequest) | [WorkspaceGroupDetailsInfo](WorkspaceGroupDetails#workspacegroupdetailsinfo) |
| [**remove_users**](./WorkspaceGroupDetails#remove_users) | [RemoveUsersWorkspaceGroupDetailsRequest](WorkspaceGroupDetails#removeusersworkspacegroupdetailsrequest) | [WorkspaceGroupDetailsInfo](WorkspaceGroupDetails#workspacegroupdetailsinfo) |
| [**get_workspace_groups**](./WorkspaceGroupDetails#get_workspace_groups) | [WorkspaceGroupDetailsRequest](WorkspaceGroupDetails#workspacegroupdetailsrequest) | [WorkspaceGroupsDetailsInfo](WorkspaceGroupDetails#workspacegroupsdetailsinfo) |



    
<br>

### update





> **POST** /identity/v2/workspace-group-details/update
>






    
<br>

### delete





> **POST** /identity/v2/workspace-group-details/delete
>






    
<br>

### add_workspaces





> **POST** /identity/v2/workspace-group-details/add-workspaces
>






    
<br>

### remove_workspaces





> **POST** /identity/v2/workspace-group-details/remove-workspaces
>






    
<br>

### find_users





> **POST** /identity/v2/workspace-group-details/find-users
>






    
<br>

### add_users





> **POST** /identity/v2/workspace-group-details/add-users
>






    
<br>

### remove_users





> **POST** /identity/v2/workspace-group-details/remove-users
>






    
<br>

### get_workspace_groups





> **POST** /identity/v2/workspace-group-details/get-workspace-group-details
>






    


<br>
<br>

## Message



### AddUsersWorkspaceGroupDetailsRequest
* **workspace_group_id** (string)   `Required` 

    
* **users** (WorkspaceGroupDetailsUser)  `Repeated`    `Required` 

    <br>

### DeleteWorkspaceGroupDetailsRequest
* **workspace_group_id** (string)   `Required` 

    <br>

### RemoveUsersWorkspaceGroupDetailsRequest
* **workspace_group_id** (string)   `Required` 

    
* **users** (string)  `Repeated`    `Required` 

    <br>

### UpdateWorkspaceGroupDetailsRequest
* **workspace_group_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>

### WorkspaceGroupDetailsFindRequest
* **keyword** (string)   `Required` 

    
* **workspace_group_id** (string)   `Required` 

    
* **state** (State)  

    
* **page** (Page)  

    <br>

### WorkspaceGroupDetailsInfo
* **workspace_group_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **workspaces** (string)  `Repeated`    `Required` 

    
* **users** (string)  `Repeated`    `Required` 

    
* **tags** (Struct)   `Required` 

    
* **created_by** (string)   `Required` 

    
* **updated_by** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### WorkspaceGroupDetailsRequest<br>

### WorkspaceGroupDetailsUser
* **user_id** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    
* **role_type** (string)   `Required` 

    <br>

### WorkspaceGroupDetailsUserSummaryInfo
* **user_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    <br>

### WorkspaceGroupDetailsUsersSummaryInfo
* **results** (WorkspaceGroupDetailsUserSummaryInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### WorkspaceGroupsDetailsInfo
* **results** (WorkspaceGroupDetailsInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### WorkspacesWorkspaceGroupDetailsRequest
* **workspace_group_id** (string)   `Required` 

    
* **workspaces** (string)  `Repeated`    `Required` 

    <br>
