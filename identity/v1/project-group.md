---
description:  
---
# Project group

>  **Package : spaceone.api.identity.v1**

## ProjectGroup

{% hint style="info" %}
**ProjectGroup Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](project-group.md#create)|   [CreateProjectGroupRequest](project-group.md#createprojectgrouprequest) |   [ProjectGroupInfo](project-group.md#projectgroupinfo) |  |
| 2 | [**update**](project-group.md#update)|   [UpdateProjectGroupRequest](project-group.md#updateprojectgrouprequest) |   [ProjectGroupInfo](project-group.md#projectgroupinfo) |  |
| 3 | [**delete**](project-group.md#delete)|   [ProjectGroupRequest](project-group.md#projectgrouprequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**add_member**](project-group.md#add_member)|   [ProjectGroupMemberRequest](project-group.md#projectgroupmemberrequest) |   [ProjectGroupMemberInfo](project-group.md#projectgroupmemberinfo) |  |
| 5 | [**modify_member**](project-group.md#modify_member)|   [ProjectGroupMemberRequest](project-group.md#projectgroupmemberrequest) |   [ProjectGroupMemberInfo](project-group.md#projectgroupmemberinfo) |  |
| 6 | [**remove_member**](project-group.md#remove_member)|   [RemoveProjectGroupMemberRequest](project-group.md#removeprojectgroupmemberrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 7 | [**get**](project-group.md#get)|   [GetProjectGroupRequest](project-group.md#getprojectgrouprequest) |   [ProjectGroupInfo](project-group.md#projectgroupinfo) |  |
| 8 | [**list**](project-group.md#list)|   [ProjectGroupQuery](project-group.md#projectgroupquery) |   [ProjectGroupsInfo](project-group.md#projectgroupsinfo) |  |
| 9 | [**stat**](project-group.md#stat)|   [ProjectGroupStatQuery](project-group.md#projectgroupstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| 10 | [**list_members**](project-group.md#list_members)|   [ProjectGroupMemberQuery](project-group.md#projectgroupmemberquery) |   [ProjectGroupMembersInfo](project-group.md#projectgroupmembersinfo) |  |
| 11 | [**list_projects**](project-group.md#list_projects)|   [ProjectGroupProjectQuery](project-group.md#projectgroupprojectquery) |   [ProjectGroupProjectsInfo](project-group.md#projectgroupprojectsinfo) |  | 
 

 
### create
> **POST** /identity/v1/project-groups
>


| Type | Message |
| :--- | :--- |
| Request | [CreateProjectGroupRequest](project-group.md#createprojectgrouprequest) |
| Response |  [ProjectGroupInfo](project-group.md#projectgroupinfo)  |
 
 

 
### update
> **PUT** /identity/v1/project-group/{project_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateProjectGroupRequest](project-group.md#updateprojectgrouprequest) |
| Response |  [ProjectGroupInfo](project-group.md#projectgroupinfo)  |
 
 

 
### delete
> **DELETE** /identity/v1/project-group/{project_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupRequest](project-group.md#projectgrouprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### add_member
> **POST** /identity/v1/project-group/{project_group_id}/members
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupMemberRequest](project-group.md#projectgroupmemberrequest) |
| Response |  [ProjectGroupMemberInfo](project-group.md#projectgroupmemberinfo)  |
 
 

 
### modify_member
> **PUT** /identity/v1/project-group/{project_group_id}/member/{user_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupMemberRequest](project-group.md#projectgroupmemberrequest) |
| Response |  [ProjectGroupMemberInfo](project-group.md#projectgroupmemberinfo)  |
 
 

 
### remove_member
> **DELETE** /identity/v1/project-group/{project_group_id}/member/{user_id}
>


| Type | Message |
| :--- | :--- |
| Request | [RemoveProjectGroupMemberRequest](project-group.md#removeprojectgroupmemberrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /identity/v1/project-group/{project_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetProjectGroupRequest](project-group.md#getprojectgrouprequest) |
| Response |  [ProjectGroupInfo](project-group.md#projectgroupinfo)  |
 
 

 
### list
> **GET** /identity/v1/project-groups
>
> **POST** /identity/v1/project-groups/search



| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupQuery](project-group.md#projectgroupquery) |
| Response |  [ProjectGroupsInfo](project-group.md#projectgroupsinfo)  |
 
 

 
### stat
> **POST** /identity/v1/project-groups/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupStatQuery](project-group.md#projectgroupstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |
 
 

 
### list_members
> **GET** /identity/v1/project-group/{project_group_id}/members
>
> **POST** /identity/v1/project-group/{project_id}/members/search



| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupMemberQuery](project-group.md#projectgroupmemberquery) |
| Response |  [ProjectGroupMembersInfo](project-group.md#projectgroupmembersinfo)  |
 
 

 
### list_projects
> **GET** /identity/v1/project-group/{project_group_id}/projects
>
> **POST** /identity/v1/project-group/{project_id}/projects/search



| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupProjectQuery](project-group.md#projectgroupprojectquery) |
| Response |  [ProjectGroupProjectsInfo](project-group.md#projectgroupprojectsinfo)  |


## 

## Message

### CreateProjectGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | parent_project_group_id |string|❌| |
| 3 | domain_id |string|✅| |
| 4 | template_id |string|❌| |
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### GetProjectGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_group_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### ProjectGroupInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | project_group_id |string | |
| 2 | name |string | |
| 3 | parent_project_group_info |[ProjectGroupInfo](project-group.md#projectgroupinfo) | |
| 4 | domain_id |string | |
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 6 | created_by |string | |
| 7 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |
| 8 | deleted_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |

### ProjectGroupMemberInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | project_group_info |[ProjectGroupInfo](project-group.md#projectgroupinfo) | |
| 2 | user_info |[UserInfo](project-group.md#userinfo) | |
| 3 | roles |[RoleInfo](project-group.md#roleinfo) | |
| 4 | labels |list of string | |

### ProjectGroupMemberQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | project_group_id |string|✅| |
| 3 | user_id |string|❌| |
| 4 | domain_id |string|✅| |

### ProjectGroupMemberRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_group_id |string|✅| |
| 2 | user_id |string|✅| |
| 3 | domain_id |string|✅| |
| 4 | roles |list of string|❌| |
| 5 | labels |list of string|❌| |

### ProjectGroupMembersInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[ProjectGroupMemberInfo](project-group.md#projectgroupmemberinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### ProjectGroupProjectInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | project_id |string | |
| 2 | name |string | |
| 3 | state |string | |
| 4 | project_group_info |[ProjectGroupInfo](project-group.md#projectgroupinfo) | |
| 5 | domain_id |string | |
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 7 | created_by |string | |
| 8 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |
| 9 | deleted_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |

### ProjectGroupProjectQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | project_group_id |string|✅| |
| 3 | recursive |bool|❌| |
| 4 | domain_id |string|✅| |

### ProjectGroupProjectsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[ProjectGroupProjectInfo](project-group.md#projectgroupprojectinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### ProjectGroupQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | project_group_id |string|❌| |
| 3 | parent_project_group_id |string|❌| |
| 4 | name |string|❌| |
| 5 | template_id |string|❌| |
| 6 | domain_id |string|✅| |

### ProjectGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_group_id |string|✅| |
| 2 | domain_id |string|✅| |

### ProjectGroupStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### ProjectGroupsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[ProjectGroupInfo](project-group.md#projectgroupinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### RemoveProjectGroupMemberRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_group_id |string|✅| |
| 2 | user_id |string|✅| |
| 3 | domain_id |string|✅| |

### UpdateProjectGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_group_id |string|✅| |
| 2 | parent_project_group_id |string|❌| |
| 3 | name |string|❌| |
| 4 | release_parent_project_group |bool|❌| |
| 5 | domain_id |string|✅| |
| 6 | template_id |string|❌| |
| 7 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
