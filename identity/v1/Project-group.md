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
| 1 | [create](Project-group.md#create)| [CreateProjectGroupRequest](Project-group.md#createprojectgrouprequest) | [ProjectGroupInfo](Project-group.md#projectgroupinfo) |  |
| 2 | [update](Project-group.md#update)| [UpdateProjectGroupRequest](Project-group.md#updateprojectgrouprequest) | [ProjectGroupInfo](Project-group.md#projectgroupinfo) |  |
| 3 | [delete](Project-group.md#delete)| [ProjectGroupRequest](Project-group.md#projectgrouprequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [add_member](Project-group.md#add_member)| [ProjectGroupMemberRequest](Project-group.md#projectgroupmemberrequest) | [ProjectGroupMemberInfo](Project-group.md#projectgroupmemberinfo) |  |
| 5 | [modify_member](Project-group.md#modify_member)| [ProjectGroupMemberRequest](Project-group.md#projectgroupmemberrequest) | [ProjectGroupMemberInfo](Project-group.md#projectgroupmemberinfo) |  |
| 6 | [remove_member](Project-group.md#remove_member)| [RemoveProjectGroupMemberRequest](Project-group.md#removeprojectgroupmemberrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 7 | [get](Project-group.md#get)| [GetProjectGroupRequest](Project-group.md#getprojectgrouprequest) | [ProjectGroupInfo](Project-group.md#projectgroupinfo) |  |
| 8 | [list](Project-group.md#list)| [ProjectGroupQuery](Project-group.md#projectgroupquery) | [ProjectGroupsInfo](Project-group.md#projectgroupsinfo) |  |
| 9 | [stat](Project-group.md#stat)| [ProjectGroupStatQuery](Project-group.md#projectgroupstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| 10 | [list_members](Project-group.md#list_members)| [ProjectGroupMemberQuery](Project-group.md#projectgroupmemberquery) | [ProjectGroupMembersInfo](Project-group.md#projectgroupmembersinfo) |  |
| 11 | [list_projects](Project-group.md#list_projects)| [ProjectGroupProjectQuery](Project-group.md#projectgroupprojectquery) | [ProjectGroupProjectsInfo](Project-group.md#projectgroupprojectsinfo) |  |

### create
> **POST** /identity/v1/project-groups
>



| Type | Message |
| :--- | :--- |
| Request | [CreateProjectGroupRequest](Project-group.md#createprojectgrouprequest) |
| Response |  [ProjectGroupInfo](Project-group.md#projectgroupinfo)  |



### update
> **PUT** /identity/v1/project-group/{project_group_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateProjectGroupRequest](Project-group.md#updateprojectgrouprequest) |
| Response |  [ProjectGroupInfo](Project-group.md#projectgroupinfo)  |



### delete
> **DELETE** /identity/v1/project-group/{project_id}
>



| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupRequest](Project-group.md#projectgrouprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### add_member
> **POST** /identity/v1/project-group/{project_group_id}/members
>



| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupMemberRequest](Project-group.md#projectgroupmemberrequest) |
| Response |  [ProjectGroupMemberInfo](Project-group.md#projectgroupmemberinfo)  |



### modify_member
> **PUT** /identity/v1/project-group/{project_group_id}/member/{user_id}
>



| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupMemberRequest](Project-group.md#projectgroupmemberrequest) |
| Response |  [ProjectGroupMemberInfo](Project-group.md#projectgroupmemberinfo)  |



### remove_member
> **DELETE** /identity/v1/project-group/{project_group_id}/member/{user_id}
>



| Type | Message |
| :--- | :--- |
| Request | [RemoveProjectGroupMemberRequest](Project-group.md#removeprojectgroupmemberrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /identity/v1/project-group/{project_group_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetProjectGroupRequest](Project-group.md#getprojectgrouprequest) |
| Response |  [ProjectGroupInfo](Project-group.md#projectgroupinfo)  |



### list
> **GET** /identity/v1/project-groups
>
> **POST** /identity/v1/project-groups/search




| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupQuery](Project-group.md#projectgroupquery) |
| Response |  [ProjectGroupsInfo](Project-group.md#projectgroupsinfo)  |



### stat
> **POST** /identity/v1/project-groups/stat
>



| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupStatQuery](Project-group.md#projectgroupstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |



### list_members
> **GET** /identity/v1/project-group/{project_group_id}/members
>
> **POST** /identity/v1/project-group/{project_id}/members/search




| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupMemberQuery](Project-group.md#projectgroupmemberquery) |
| Response |  [ProjectGroupMembersInfo](Project-group.md#projectgroupmembersinfo)  |



### list_projects
> **GET** /identity/v1/project-group/{project_group_id}/projects
>
> **POST** /identity/v1/project-group/{project_id}/projects/search




| Type | Message |
| :--- | :--- |
| Request | [ProjectGroupProjectQuery](Project-group.md#projectgroupprojectquery) |
| Response |  [ProjectGroupProjectsInfo](Project-group.md#projectgroupprojectsinfo)  |





## Message

### CreateProjectGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | parent_project_group_id |string |✅ ||
| 3 | domain_id |string |✅ ||
| 4 | template_id |string |❌ ||
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||

### GetProjectGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_group_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### ProjectGroupInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_group_id |string | ||
| 2 | name |string | ||
| 3 | parent_project_group_info |[ProjectGroupInfo](Project-group.md#projectgroupinfo) | |{'repeated Template fields = 3;                 // TODO': 'Not be implemented TEMPLATE yet', 'string template_id = 4;                       // TODO': 'Not be implemented TEMPLATE yet'}|
| 4 | domain_id |string | ||
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 6 | created_by |string | ||
| 7 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||
| 8 | deleted_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### ProjectGroupMemberInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_group_info |[ProjectGroupInfo](Project-group.md#projectgroupinfo) | ||
| 2 | user_info |[UserInfo](Project-group.md#userinfo) | ||
| 3 | roles |[RoleInfo](Project-group.md#roleinfo) | ||
| 4 | labels |string | ||

### ProjectGroupMemberQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | project_group_id |string |✅ ||
| 3 | user_id |string |❌ ||
| 4 | domain_id |string |✅ ||

### ProjectGroupMemberRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_group_id |string |✅ ||
| 2 | user_id |string |✅ ||
| 3 | domain_id |string |✅ ||
| 4 | roles |string |✅ ||
| 5 | labels |string |✅ ||

### ProjectGroupMembersInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[ProjectGroupMemberInfo](Project-group.md#projectgroupmemberinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### ProjectGroupProjectInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string | ||
| 2 | name |string | ||
| 3 | state |string | ||
| 4 | project_group_info |[ProjectGroupInfo](Project-group.md#projectgroupinfo) | |{'google.protobuf.Struct template_data = 4; // TODO': 'Not be implemented template service yet'}|
| 5 | domain_id |string | ||
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 7 | created_by |string | ||
| 8 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||
| 9 | deleted_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### ProjectGroupProjectQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | project_group_id |string |✅ ||
| 3 | recursive |bool |❌ ||
| 4 | domain_id |string |✅ ||

### ProjectGroupProjectsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[ProjectGroupProjectInfo](Project-group.md#projectgroupprojectinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### ProjectGroupQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | project_group_id |string |❌ ||
| 3 | parent_project_group_id |string |❌ ||
| 4 | name |string |❌ ||
| 5 | template_id |string |❌ ||
| 6 | domain_id |string |✅ ||

### ProjectGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_group_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### ProjectGroupStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### ProjectGroupsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[ProjectGroupInfo](Project-group.md#projectgroupinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### RemoveProjectGroupMemberRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_group_id |string |✅ ||
| 2 | user_id |string |✅ ||
| 3 | domain_id |string |✅ ||

### UpdateProjectGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_group_id |string |✅ ||
| 2 | parent_project_group_id |string |✅ ||
| 3 | name |string |❌ ||
| 4 | release_parent_project_group |bool |❌ ||
| 5 | domain_id |string |✅ ||
| 6 | template_id |string |❌ ||
| 7 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
