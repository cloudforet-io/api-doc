---
description:  
---
# Project group

>  **Package : spaceone.api.identity.v1**

## ProjectGroup

{% hint style="info" %}
**{{ service.name }} Methods:**
{{ service.description }}
{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](project-group.md#create)|   [CreateProjectGroupRequest](project-group.md#createprojectgrouprequest) |   [ProjectGroupInfo](project-group.md#projectgroupinfo) |
| [**update**](project-group.md#update)|   [UpdateProjectGroupRequest](project-group.md#updateprojectgrouprequest) |   [ProjectGroupInfo](project-group.md#projectgroupinfo) |
| [**delete**](project-group.md#delete)|   [ProjectGroupRequest](project-group.md#projectgrouprequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](project-group.md#get)|   [GetProjectGroupRequest](project-group.md#getprojectgrouprequest) |   [ProjectGroupInfo](project-group.md#projectgroupinfo) |
| [**list**](project-group.md#list)|   [ProjectGroupQuery](project-group.md#projectgroupquery) |   [ProjectGroupsInfo](project-group.md#projectgroupsinfo) |
| [**stat**](project-group.md#stat)|   [ProjectGroupStatQuery](project-group.md#projectgroupstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|
| [**add_member**](project-group.md#add_member)|   [AddProjectGroupMemberRequest](project-group.md#addprojectgroupmemberrequest) |   [ProjectGroupRoleBindingInfo](project-group.md#projectgrouprolebindinginfo) |
| [**modify_member**](project-group.md#modify_member)|   [ModifyProjectGroupMemberRequest](project-group.md#modifyprojectgroupmemberrequest) |   [ProjectGroupRoleBindingInfo](project-group.md#projectgrouprolebindinginfo) |
| [**remove_member**](project-group.md#remove_member)|   [RemoveProjectGroupMemberRequest](project-group.md#removeprojectgroupmemberrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**list_members**](project-group.md#list_members)|   [ProjectGroupMemberQuery](project-group.md#projectgroupmemberquery) |   [ProjectGroupRoleBindingsInfo](project-group.md#projectgrouprolebindingsinfo) |
| [**list_projects**](project-group.md#list_projects)|   [ProjectGroupProjectQuery](project-group.md#projectgroupprojectquery) |   [ProjectGroupProjectsInfo](project-group.md#projectgroupprojectsinfo) | 
 

 
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
 
 

 
### add_member
> **POST** /identity/v1/project-group/{project_group_id}/members
>


| Type | Message |
| :--- | :--- |
| Request | [AddProjectGroupMemberRequest](project-group.md#addprojectgroupmemberrequest) |
| Response |  [ProjectGroupRoleBindingInfo](project-group.md#projectgrouprolebindinginfo)  |
 
 

 
### modify_member
> **PUT** /identity/v1/project-group/{project_group_id}/member/{user_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ModifyProjectGroupMemberRequest](project-group.md#modifyprojectgroupmemberrequest) |
| Response |  [ProjectGroupRoleBindingInfo](project-group.md#projectgrouprolebindinginfo)  |
 
 

 
### remove_member
> **DELETE** /identity/v1/project-group/{project_group_id}/member/{user_id}
>


| Type | Message |
| :--- | :--- |
| Request | [RemoveProjectGroupMemberRequest](project-group.md#removeprojectgroupmemberrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### list_members
> **GET** /identity/v1/project-group/{project_group_id}/members
>
> **POST** /identity/v1/project-group/{project_id}/members/search



| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupMemberQuery](project-group.md#projectgroupmemberquery) |
| Response |  [ProjectGroupRoleBindingsInfo](project-group.md#projectgrouprolebindingsinfo)  |
 
 

 
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

### AddProjectGroupMemberRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_group_id |string|✔| |
| user_id |string|✔| |
| role_id |string|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
| is_external_user |bool|✘| |

### CreateProjectGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| parent_project_group_id |string|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### GetProjectGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_group_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### ModifyProjectGroupMemberRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_group_id |string|✔| |
| user_id |string|✔| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### ProjectGroupInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| project_group_id |string | |
| name |string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| parent_project_group_info |[ProjectGroupInfo](project-group.md#projectgroupinfo) | |
| domain_id |string | |
| created_by |string | |
| created_at |string | |

### ProjectGroupMemberQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| project_group_id |string|✔| |
| user_id |string|✘| |
| role_id |string|✘| |
| include_parent_member |bool|✘| |
| domain_id |string|✔| |

### ProjectGroupProjectInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| project_id |string | |
| name |string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| project_group_info |[ProjectGroupInfo](project-group.md#projectgroupinfo) | |
| domain_id |string | |
| created_by |string | |
| created_at |string | |

### ProjectGroupProjectQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| project_group_id |string|✔| |
| recursive |bool|✘| |
| domain_id |string|✔| |

### ProjectGroupProjectsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ProjectGroupProjectInfo](project-group.md#projectgroupprojectinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### ProjectGroupQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| project_group_id |string|✘| |
| name |string|✘| |
| parent_project_group_id |string|✘| |
| author_within |bool|✘| |
| domain_id |string|✔| |

### ProjectGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_group_id |string|✔| |
| domain_id |string|✔| |

### ProjectGroupRoleBindingInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| role_binding_id |string | |
| resource_type |string | |
| resource_id |string | |
| role_info |[RoleInfo](project-group.md#roleinfo) | |
| project_group_info |[ProjectGroupInfo](project-group.md#projectgroupinfo) | |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
| created_at |string | |

### ProjectGroupRoleBindingsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ProjectGroupRoleBindingInfo](project-group.md#projectgrouprolebindinginfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### ProjectGroupStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### ProjectGroupsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ProjectGroupInfo](project-group.md#projectgroupinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### RemoveProjectGroupMemberRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_group_id |string|✔| |
| user_id |string|✔| |
| domain_id |string|✔| |

### UpdateProjectGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_group_id |string|✔| |
| name |string|✘| |
| parent_project_group_id |string|✘| |
| release_parent_project_group |bool|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
