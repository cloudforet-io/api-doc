---
title: "WorkspaceUser"
linkTitle: "WorkspaceUser"
weight: 3
bookFlatSection: true
---
# [WorkspaceUser](#WorkspaceUser)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## WorkspaceUser





**WorkspaceUser Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./WorkspaceUser#create) | [CreateWorkspaceUserRequest](WorkspaceUser#createworkspaceuserrequest) | [WorkspaceUserInfo](WorkspaceUser#workspaceuserinfo) |
| [**get**](./WorkspaceUser#get) | [WorkspaceUserRequest](WorkspaceUser#workspaceuserrequest) | [WorkspaceUserInfo](WorkspaceUser#workspaceuserinfo) |
| [**list**](./WorkspaceUser#list) | [WorkspaceUserSearchQuery](WorkspaceUser#workspaceusersearchquery) | [WorkspaceUsersInfo](WorkspaceUser#workspaceusersinfo) |
| [**stat**](./WorkspaceUser#stat) | [WorkspaceUserStatQuery](WorkspaceUser#workspaceuserstatquery) | [Struct](WorkspaceUser#struct) |



    
<br>

### create





> **POST** /identity/v2/workspace-user/create
>






    
<br>

### get





> **POST** /identity/v2/workspace-user/get
>






    
<br>

### list





> **POST** /identity/v2/workspace-user/list
>






    
<br>

### stat





> **POST** /identity/v1/workspace-user/stat
>






    


<br>
<br>

## Message



### CreateWorkspaceUserRequest
* **user_id** (string)   `Required` 

    
* **auth_type** (AuthType)   `Required` 

    
* **reset_password** (bool)   `Required` 

  *If reset_password is true, send email*

    
* **role_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **password** (string)  

  *When auth_type is LOCAL, password is required.*

    
* **name** (string)  

    
* **email** (string)  

    
* **language** (string)  

  *en,ko*

    
* **timezone** (string)  

  *UTC, Asia/Seoul*

    
* **tags** (Struct)  

    <br>

### WorkspaceUserInfo
* **user_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **email** (string)   `Required` 

    
* **auth_type** (AuthType)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **language** (string)   `Required` 

    
* **timezone** (string)   `Required` 

    
* **api_key_count** (int32)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **role_binding** (RoleBindingInfo)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_accessed_at** (string)   `Required` 

    <br>

### WorkspaceUserRequest
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    <br>

### WorkspaceUserSearchQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **user_id** (string)  

    
* **name** (string)  

    
* **state** (State)  

    
* **email** (string)  

    
* **auth_type** (AuthType)  

    
* **workspace_id** (string)  

    <br>

### WorkspaceUserStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)  

    <br>

### WorkspaceUsersInfo
* **results** (WorkspaceUserInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
