---
description:  
---
# Project

>  **Package : spaceone.api.identity.v1**

## Project

{% hint style="info" %}
**Project Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](project.md#create)|   [CreateProjectRequest](project.md#createprojectrequest) |   [ProjectInfo](project.md#projectinfo) |  |
| 2 | [**update**](project.md#update)|   [UpdateProjectRequest](project.md#updateprojectrequest) |   [ProjectInfo](project.md#projectinfo) |  |
| 3 | [**delete**](project.md#delete)|   [ProjectRequest](project.md#projectrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](project.md#get)|   [GetProjectRequest](project.md#getprojectrequest) |   [ProjectInfo](project.md#projectinfo) |  |
| 5 | [**list**](project.md#list)|   [ProjectQuery](project.md#projectquery) |   [ProjectsInfo](project.md#projectsinfo) |  |
| 6 | [**stat**](project.md#stat)|   [ProjectStatQuery](project.md#projectstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| 7 | [**add_member**](project.md#add_member)|   [AddProjectMemberRequest](project.md#addprojectmemberrequest) |   [ProjectRoleBindingInfo](project.md#projectrolebindinginfo) |  |
| 8 | [**modify_member**](project.md#modify_member)|   [ModifyProjectMemberRequest](project.md#modifyprojectmemberrequest) |   [ProjectRoleBindingInfo](project.md#projectrolebindinginfo) |  |
| 9 | [**remove_member**](project.md#remove_member)|   [RemoveProjectMemberRequest](project.md#removeprojectmemberrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 10 | [**list_members**](project.md#list_members)|   [ProjectMemberQuery](project.md#projectmemberquery) |   [ProjectRoleBindingsInfo](project.md#projectrolebindingsinfo) |  | 
 

 
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
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string|✅| |
| 2 | user_id |string|✅| |
| 3 | role_id |string|❌| |
| 4 | labels |list of string|❌| |
| 5 | tags |list of spaceone.api.core.v1.Tag|❌| |
| 6 | domain_id |string|✅| |

### CreateProjectRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | project_group_id |string|✅| |
| 3 | tags |list of spaceone.api.core.v1.Tag|❌| |
| 4 | domain_id |string|✅| |

### GetProjectRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### ModifyProjectMemberRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string|✅| |
| 2 | user_id |string|✅| |
| 3 | labels |list of string|❌| |
| 4 | tags |list of spaceone.api.core.v1.Tag|❌| |
| 5 | domain_id |string|✅| |

### ProjectInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | project_id |string | |
| 2 | name |string | |
| 3 | tags |list of spaceone.api.core.v1.Tag | |
| 4 | project_group_info |[ProjectGroupInfo](project.md#projectgroupinfo) | |
| 5 | domain_id |string | |
| 6 | created_by |string | |
| 7 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |

### ProjectMemberQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | project_id |string|✅| |
| 3 | user_id |string|❌| |
| 4 | role_id |string|❌| |
| 5 | include_parent_member |string|❌| |
| 6 | domain_id |string|✅| |

### ProjectQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | project_id |string|❌| |
| 3 | name |string|❌| |
| 4 | project_group_id |string|❌| |
| 5 | user_id |string|❌| |
| 6 | domain_id |string|✅| |

### ProjectRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string|✅| |
| 2 | domain_id |string|✅| |

### ProjectRoleBindingInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | role_binding_id |string | |
| 2 | resource_type |string | |
| 3 | resource_id |string | |
| 4 | role_info |[RoleInfo](project.md#roleinfo) | |
| 5 | project_info |[ProjectInfo](project.md#projectinfo) | |
| 6 | labels |list of string | |
| 7 | tags |list of spaceone.api.core.v1.Tag | |
| 8 | domain_id |string | |
| 9 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |

### ProjectRoleBindingsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of ProjectRoleBindingInfo](project.md#projectrolebindinginfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### ProjectStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### ProjectsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of ProjectInfo](project.md#projectinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### RemoveProjectMemberRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string|✅| |
| 2 | user_id |string|✅| |
| 3 | domain_id |string|✅| |

### UpdateProjectRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string|✅| |
| 2 | project_group_id |string|❌| |
| 3 | name |string|❌| |
| 4 | tags |list of spaceone.api.core.v1.Tag|❌| |
| 5 | domain_id |string|✅| |
