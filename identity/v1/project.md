---
description:  
---
# Project

>  **Package : spaceone.api.identity.v1**

## Project

{% hint style="info" %}
**Project Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](project.md#create)|   [CreateProjectRequest](project.md#createprojectrequest) |   [ProjectInfo](project.md#projectinfo) |
| [**update**](project.md#update)|   [UpdateProjectRequest](project.md#updateprojectrequest) |   [ProjectInfo](project.md#projectinfo) |
| [**delete**](project.md#delete)|   [ProjectRequest](project.md#projectrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](project.md#get)|   [GetProjectRequest](project.md#getprojectrequest) |   [ProjectInfo](project.md#projectinfo) |
| [**list**](project.md#list)|   [ProjectQuery](project.md#projectquery) |   [ProjectsInfo](project.md#projectsinfo) |
| [**stat**](project.md#stat)|   [ProjectStatQuery](project.md#projectstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|
| [**add_member**](project.md#add_member)|   [AddProjectMemberRequest](project.md#addprojectmemberrequest) |   [ProjectRoleBindingInfo](project.md#projectrolebindinginfo) |
| [**modify_member**](project.md#modify_member)|   [ModifyProjectMemberRequest](project.md#modifyprojectmemberrequest) |   [ProjectRoleBindingInfo](project.md#projectrolebindinginfo) |
| [**remove_member**](project.md#remove_member)|   [RemoveProjectMemberRequest](project.md#removeprojectmemberrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**list_members**](project.md#list_members)|   [ProjectMemberQuery](project.md#projectmemberquery) |   [ProjectRoleBindingsInfo](project.md#projectrolebindingsinfo) | 
 

 
### create
> **POST** /identity/v1/projects
>


| Type | Message |
| :--- | :--- |
| Request | [CreateProjectRequest](project.md#createprojectrequest) |
| Response |  [ProjectInfo](project.md#projectinfo)  |
 
 

 
### update
> **PUT** /identity/v1/project/{project_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateProjectRequest](project.md#updateprojectrequest) |
| Response |  [ProjectInfo](project.md#projectinfo)  |
 
 

 
### delete
> **DELETE** /identity/v1/project/{project_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectRequest](project.md#projectrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /identity/v1/project/{project_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetProjectRequest](project.md#getprojectrequest) |
| Response |  [ProjectInfo](project.md#projectinfo)  |
 
 

 
### list
> **GET** /identity/v1/projects
>
> **POST** /identity/v1/projects/search



| Type | Message |
| :--- | :--- |
| Request | [ProjectQuery](project.md#projectquery) |
| Response |  [ProjectsInfo](project.md#projectsinfo)  |
 
 

 
### stat
> **POST** /identity/v1/projects/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectStatQuery](project.md#projectstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |
 
 

 
### add_member
> **POST** /identity/v1/project/{project_id}/members
>


| Type | Message |
| :--- | :--- |
| Request | [AddProjectMemberRequest](project.md#addprojectmemberrequest) |
| Response |  [ProjectRoleBindingInfo](project.md#projectrolebindinginfo)  |
 
 

 
### modify_member
> **PUT** /identity/v1/project/{project_id}/member/{user_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ModifyProjectMemberRequest](project.md#modifyprojectmemberrequest) |
| Response |  [ProjectRoleBindingInfo](project.md#projectrolebindinginfo)  |
 
 

 
### remove_member
> **DELETE** /identity/v1/project/{project_id}/member/{user_id}
>


| Type | Message |
| :--- | :--- |
| Request | [RemoveProjectMemberRequest](project.md#removeprojectmemberrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### list_members
> **GET** /identity/v1/project/{project_id}/members
>
> **POST** /identity/v1/project/{project_id}/members/search



| Type | Message |
| :--- | :--- |
| Request | [ProjectMemberQuery](project.md#projectmemberquery) |
| Response |  [ProjectRoleBindingsInfo](project.md#projectrolebindingsinfo)  |


## 

## Message

### AddProjectMemberRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_id |string|✔| |
| user_id |string|✔| |
| role_id |string|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
| is_external_user |bool|✘| |

### CreateProjectRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| project_group_id |string|✔| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### GetProjectRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### ModifyProjectMemberRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_id |string|✔| |
| user_id |string|✔| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### ProjectInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| project_id |string | |
| name |string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| project_group_info |[ProjectGroupInfo](project.md#projectgroupinfo) | |
| domain_id |string | |
| created_by |string | |
| created_at |string | |

### ProjectMemberQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| project_id |string|✔| |
| user_id |string|✘| |
| role_id |string|✘| |
| include_parent_member |bool|✘| |
| domain_id |string|✔| |

### ProjectQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| project_id |string|✘| |
| name |string|✘| |
| project_group_id |string|✘| |
| user_id |string|✘| |
| domain_id |string|✔| |

### ProjectRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_id |string|✔| |
| domain_id |string|✔| |

### ProjectRoleBindingInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| role_binding_id |string | |
| resource_type |string | |
| resource_id |string | |
| role_info |[RoleInfo](project.md#roleinfo) | |
| project_info |[ProjectInfo](project.md#projectinfo) | |
| project_group_info |[ProjectGroupInfo](project.md#projectgroupinfo) | |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
| created_at |string | |

### ProjectRoleBindingsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ProjectRoleBindingInfo](project.md#projectrolebindinginfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### ProjectStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### ProjectsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ProjectInfo](project.md#projectinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### RemoveProjectMemberRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_id |string|✔| |
| user_id |string|✔| |
| domain_id |string|✔| |

### UpdateProjectRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_id |string|✔| |
| project_group_id |string|✘| |
| name |string|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
