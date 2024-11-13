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

WorkspaceUser service api are used to manage workspace users by the workspace owner.



**WorkspaceUser Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./WorkspaceUser#create) | [CreateWorkspaceUserRequest](WorkspaceUser#createworkspaceuserrequest) | [WorkspaceUserInfo](WorkspaceUser#workspaceuserinfo) |
| [**get**](./WorkspaceUser#get) | [WorkspaceUserRequest](WorkspaceUser#workspaceuserrequest) | [WorkspaceUserInfo](WorkspaceUser#workspaceuserinfo) |
| [**find**](./WorkspaceUser#find) | [WorkspaceUserFindRequest](WorkspaceUser#workspaceuserfindrequest) | [UsersSummaryInfo](WorkspaceUser#userssummaryinfo) |
| [**list**](./WorkspaceUser#list) | [WorkspaceUserSearchQuery](WorkspaceUser#workspaceusersearchquery) | [WorkspaceUsersInfo](WorkspaceUser#workspaceusersinfo) |
| [**stat**](./WorkspaceUser#stat) | [WorkspaceUserStatQuery](WorkspaceUser#workspaceuserstatquery) | [Struct](WorkspaceUser#struct) |



    
<br>

### create

Create a workspace user. If the user does not exist in your domain, the user will be created in your domain and create a workspace user with the role.
If you want to create a workspace user with the existing user, you can use role-binding create api.



> **POST** /identity/v2/workspace-user/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateWorkspaceUserRequest](./WorkspaceUser#createworkspaceuserrequest)

* **user_id** (string)   `Required` 


* **auth_type** (AuthType)   `Required` 

  *LOCAL, EXTERNAL*


* **reset_password** (bool)   `Required` 

  *If reset_password is true, send email*


* **role_id** (string)   `Required` 

  *You can use custom role or managed role something like `managed-workspace-member`, `managed-workspace-owner` ,...*


* **password** (string)  

  *When auth_type is LOCAL, password is required.*


* **name** (string)  


* **email** (string)  


* **language** (string)  

  *en,ko*


* **timezone** (string)  

  *UTC, Asia/Seoul*


* **tags** (Struct)  





{{< highlight json >}}
{
 "user_id": "wonny@cloudforet.io",
 "password": "Password0*",
 "name": "Wonny",
 "email": "wonny@cloudforet.io",
 "auth_type": "LOCAL",
 "language": "en",
 "timezone": "UTC",
 "tags": {
   "team": "cloudforet"
 },
 "reset_password": false,
 "role_id": "managed-workspace-member"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[WorkspaceUserInfo](#WORKSPACEUSERINFO)
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

* **role_binding_info** (RoleBindingInfo)   `Required` 

* **email_verified** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_accessed_at** (string)   `Required` 



{{< highlight json >}}
{
 "user_id": "wonny@cloudforet.io",
 "name": "Wonny",
 "state": "PENDING",
 "email": "wonny@cloudforet.io",
 "auth_type": "LOCAL",
 "role_type": "USER",
 "language": "en",
 "timezone": "UTC",
 "api_key_count": 0,
 "role_binding_info": {
       "user_id": "wonny@cloudforet.io",
       "workspace_id": "workspace-99d4nn0c14ae",
       "domain_id": "domain-1234ee0c14ae",
       "role_binding_id": "rb-11d4eeaa1411",
       "role_id": "managed-workspace-member",
       "role_type": "MANAGED",
       "resource_group": "WORKSPACE",
       "created_at": "2024-11-12T06:06:04.999Z"
 },
 "created_at": "2024-11-12T06:06:04.999Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get





> **POST** /identity/v2/workspace-user/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[WorkspaceUserRequest](./WorkspaceUser#workspaceuserrequest)

* **user_id** (string)   `Required` 


* **workspace_id** (string)  

  *For DOMAIN ADMIN this field is optional, but for WORKSPACE OWNER and WORKSPACE MEMBER this field is required.*





{{< highlight json >}}
{
  "user_id": "wonny@cloudforet.io",
  "workspace_id": "workspace-ab12345"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[WorkspaceUserInfo](#WORKSPACEUSERINFO)
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

* **role_binding_info** (RoleBindingInfo)   `Required` 

* **email_verified** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_accessed_at** (string)   `Required` 



{{< highlight json >}}
{
 "user_id": "wonny@cloudforet.io",
 "name": "Wonny",
 "state": "PENDING",
 "email": "wonny@cloudforet.io",
 "auth_type": "LOCAL",
 "role_type": "USER",
 "language": "en",
 "timezone": "UTC",
 "api_key_count": 0,
 "role_binding_info": {
       "user_id": "wonny@cloudforet.io",
       "workspace_id": "workspace-99d4nn0c14ae",
       "domain_id": "domain-1234ee0c14ae",
       "role_binding_id": "rb-11d4eeaa1411",
       "role_id": "managed-workspace-member",
       "role_type": "MANAGED",
       "resource_group": "WORKSPACE",
       "created_at": "2024-11-12T06:06:04.999Z"
 },
 "created_at": "2024-11-12T06:06:04.999Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### find





> **POST** /identity/v2/workspace-user/find
>





 {{< tabs " find " >}}

 {{< tab "Request Example" >}}



[WorkspaceUserFindRequest](./WorkspaceUser#workspaceuserfindrequest)

* **keyword** (string)   `Required` 


* **workspace_id** (string)   `Required` 


* **state** (State)  


* **page** (Page)  





{{< highlight json >}}
{
 "keyword": "cloudforet",
 "state": "ENABLED",
 "page": {
      "start": 1,
      "limit": 5
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UsersSummaryInfo](#USERSSUMMARYINFO)
* **results** (UserSummaryInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
   "results": [
       {
          "user_id": "wonny@cloudforet.io",
          "name": "Wonny",
          "state": "ENABLED"
       },
       {
           "user_id": "belty@cloudforet.io",
           "name": "Belty",
           "state": "ENABLED"
       },
       {
           "user_id": "bolby@cloudforet.io",
           "state": "PENDING"
       },
       {
           "user_id": "cuby@cloudforet.io",
           "state": "PENDING"
       },
       {
           "user_id": "musly@cloudforet.io",
           "state": "PENDING"
       }
   ],
   "total_count": 21
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list





> **POST** /identity/v2/workspace-user/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[WorkspaceUserSearchQuery](./WorkspaceUser#workspaceusersearchquery)

* **workspace_id** (string)   `Required` 


* **query** (Query)  


* **user_id** (string)  


* **name** (string)  


* **state** (State)  


* **email** (string)  


* **auth_type** (AuthType)  


* **role_type** (string)  





{{< highlight json >}}
{
 "query": {
   "filter": [
     {
       "k": "language",
       "v": "en",
       "o": "eq"
     }
   ]
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[WorkspaceUsersInfo](#WORKSPACEUSERSINFO)
* **results** (WorkspaceUserInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
 "results": [
     {
         "user_id": "wonny@cloudforet.io",
         "name": "Wonny",
         "state": "ENABLED",
         "email": "wonny@cloudforet.io",
         "auth_type": "LOCAL",
         "role_type": "USER",
         "language": "en",
         "timezone": "UTC",
         "api_key_count": 2,
         "role_binding_info": {
             "user_id": "wonny@cloudforet.io",
             "workspace_id": "workspace-99d4nn0c14ae",
             "domain_id": "domain-1234ee0c14ae",
             "role_binding_id": "rb-11d4eeaa1411",
             "role_id": "managed-workspace-member",
             "role_type": "MANAGED",
             "resource_group": "WORKSPACE",
             "created_at": "2024-11-12T06:06:04.999Z"
         },
         "domain_id": "domain-1234ee0c14ae",
         "created_at": "2024-11-12T06:06:04.999Z",
         "last_accessed_at": "2024-11-12T06:06:04.999Z"
     }
 ]
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
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

  *LOCAL, EXTERNAL*

    
* **reset_password** (bool)   `Required` 

  *If reset_password is true, send email*

    
* **role_id** (string)   `Required` 

  *You can use custom role or managed role something like `managed-workspace-member`, `managed-workspace-owner` ,...*

    
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

### UserSummaryInfo
* **user_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    <br>

### UsersSummaryInfo
* **results** (UserSummaryInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### WorkspaceUserFindRequest
* **keyword** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **state** (State)  

    
* **page** (Page)  

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

    
* **role_binding_info** (RoleBindingInfo)   `Required` 

    
* **email_verified** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_accessed_at** (string)   `Required` 

    <br>

### WorkspaceUserRequest
* **user_id** (string)   `Required` 

    
* **workspace_id** (string)  

  *For DOMAIN ADMIN this field is optional, but for WORKSPACE OWNER and WORKSPACE MEMBER this field is required.*

    <br>

### WorkspaceUserSearchQuery
* **workspace_id** (string)   `Required` 

    
* **query** (Query)  

    
* **user_id** (string)  

    
* **name** (string)  

    
* **state** (State)  

    
* **email** (string)  

    
* **auth_type** (AuthType)  

    
* **role_type** (string)  

    <br>

### WorkspaceUserStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **workspace_id** (string)   `Required` 

    <br>

### WorkspaceUsersInfo
* **results** (WorkspaceUserInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
